import numpy as np
from numba import cuda
import numba as nb

@cuda.jit('int32(int32,int32,int32,int32,int32,int32)',device=True)
def checker(id_n1,id_n2,id_n3,id_tri_n1,id_tri_n2,id_tri_n3):
    """this function check if   a element have sharing vertex with a triangle

    Args:
        id_n1 (np.int32): id of vertex 1 of element
        id_n2 (np.int32): id of vertex 2 of element
        id_n3 (np.int32): id of vertex 3 of element
        id_tri_n1 (np.int32): id of vertex 1 of triangle
        id_tri_n2 (np.int32): id of vertex 2 of triangle
        id_tri_n3 (np.int32): id of vertex 3 of triangle

    Returns:
        int : 1 if element have sharing vertex with triangle else -1
    """
    if  id_n1==id_tri_n1 or id_n1==id_tri_n2 or id_n1==id_tri_n3 or\
        id_n2==id_tri_n1 or id_n2==id_tri_n2 or id_n2==id_tri_n3 or\
        id_n3==id_tri_n1 or id_n3==id_tri_n2 or id_n3==id_tri_n3:
        return 1
    else:
        return -1

@cuda.jit('void(int32[:],int32[:],int32[:],int32[:],int32[:],int32[:],int32[:,:])')
def mul_check_PointIsInsideTriangles(id_n1s,id_n2s,id_n3s,id_tri_n1,id_tri_n2,id_tri_n3,ans):
    """this function check if   a element have sharing vertex with a triangle

    Args:
        id_n1s (numpy array int32): id of vertex 1 of element
        id_n2s (numpy array int32): id of vertex 2 of element
        id_n3s (numpy array int32): id of vertex 3 of element
        id_tri_n1 (numpy array int32): id of vertex 1 of triangle
        id_tri_n2 (numpy array int32): id of vertex 2 of triangle
        id_tri_n3 (numpy array int32): id of vertex 3 of triangle
        ans (numpy array int32): array of result
    """
    i, j = cuda.grid(2)
    if i < len(id_n1s) and j < len(id_tri_n1):
        ans[i,j]=checker(id_n1s[i],id_n2s[i],id_n3s[i],id_tri_n1[j],id_tri_n2[j],id_tri_n3[j])
    
    
def mul_kernel_check_PointIsInsideElementssearch_element(MeshElementsNumpyArray,Elements,thread_x=32,thread_y=32):
    """this function check if   a element have sharing vertex with a triangle

    Args:
        MeshElementsNumpyArray (numpy array int32): array of elements
        Elements (numpy array int32): array of triangles
    
    Returns:
        list of list of int : list of id of elements that have sharing vertex with a triangle
    """
    d_id_n1s    = cuda.to_device(np.ascontiguousarray(MeshElementsNumpyArray[:,1],dtype=np.int32))
    d_id_n2s    = cuda.to_device(np.ascontiguousarray(MeshElementsNumpyArray[:,2],dtype=np.int32))
    d_id_n3s    = cuda.to_device(np.ascontiguousarray(MeshElementsNumpyArray[:,3],dtype=np.int32))
    d_id_tri_n1 = cuda.to_device(np.ascontiguousarray(Elements[:,1],dtype=np.int32))
    d_id_tri_n2 = cuda.to_device(np.ascontiguousarray(Elements[:,2],dtype=np.int32))
    d_id_tri_n3 = cuda.to_device(np.ascontiguousarray(Elements[:,3],dtype=np.int32))
    ans         = np.zeros((len(MeshElementsNumpyArray),len(Elements)),dtype=np.int32)
    d_ans       = cuda.to_device(ans)
    
    
    threadsperblock = (int(thread_x), int(thread_y))
    blockspergrid_x = int(np.ceil(d_id_n1s.shape[0]    / threadsperblock[0]))
    blockspergrid_y = int(np.ceil(d_id_tri_n1.shape[0] / threadsperblock[1]))
    blockspergrid = (blockspergrid_x, blockspergrid_y) 

    mul_check_PointIsInsideTriangles[blockspergrid, threadsperblock](d_id_n1s,d_id_n2s,d_id_n3s,d_id_tri_n1,d_id_tri_n2,d_id_tri_n3,d_ans)
    ans=d_ans.copy_to_host()
    ans=np.array(ans)
    ans=np.transpose(ans)
    li_ans=[]
    for i in range (len(ans)):
            idx=np.argwhere(ans[i] == 1).flatten()
            ids=MeshElementsNumpyArray[idx, 0].flatten()
            li_ans.append(list(ids))
    


    return li_ans



@cuda.jit('void(int32[:],int32[:],int32[:],int32,int32,int32,int32[:])')
def one_check_PointIsInsideTriangles(id_n1s,id_n2s,id_n3s,id_tri_n1,id_tri_n2,id_tri_n3,ans):
    """this function check if   a element have sharing vertex with a triangle

    Args:
        id_n1s (numpy array int32): id of vertex 1 of element
        id_n2s (numpy array int32): id of vertex 2 of element
        id_n3s (numpy array int32): id of vertex 3 of element
        id_tri_n1 (int32): id of vertex 1 of triangle
        id_tri_n2 (int32): id of vertex 2 of triangle
        id_tri_n3 (int32): id of vertex 3 of triangle
        ans (numpy array int32): array of result
    """
    i = cuda.grid(1)
    if i < len(id_n1s):
        ans[i]=checker(id_n1s[i],id_n2s[i],id_n3s[i],id_tri_n1,id_tri_n2,id_tri_n3)


def one_search_element(mesh,Element,thread_x=32,thread_y=32):
    """this function check if   a element have sharing vertex with a triangle

    Args:
        mesh (Mesh): mesh
        Element (Triangle): triangle
    
    Returns:
        list of int : list of id of elements that have sharing vertex with a triangle
    """
    ElementsNumpyArray=mesh.GiveJarOfElement().ToNumPyArrayWithIDs()
    tr=ElementsNumpyArray[:,1]
    id_elements=ElementsNumpyArray[:,0]
    id_n1s=ElementsNumpyArray[:,1]
    id_n2s=ElementsNumpyArray[:,2]
    id_n3s=ElementsNumpyArray[:,3]
    id_tri_n1=Element.Give_n1().GiveID()
    id_tri_n2=Element.Give_n2().GiveID()
    id_tri_n3=Element.Give_n3().GiveID()
    
    d_id_n1s    = cuda.to_device(np.array(id_n1s,dtype=np.int32))
    d_id_n2s    = cuda.to_device(np.array(id_n2s,dtype=np.int32))
    d_id_n3s    = cuda.to_device(np.array(id_n3s,dtype=np.int32))
    d_id_tri_n1 = np.int32(id_tri_n1)
    d_id_tri_n2 = np.int32(id_tri_n2)
    d_id_tri_n3 = np.int32(id_tri_n3)
    d_ans       = np.zeros(len(id_n1s),dtype=np.int32)
    d_ans       = cuda.to_device(d_ans)
    threadsperblock = thread_x
    blockspergrid = (len(id_n1s) + (threadsperblock - 1)) // threadsperblock
    one_check_PointIsInsideTriangles[blockspergrid, threadsperblock](d_id_n1s,d_id_n2s,d_id_n3s,d_id_tri_n1,d_id_tri_n2,d_id_tri_n3,d_ans)
    ans=d_ans.copy_to_host()
    ans=np.array(ans)
    idx=np.argwhere(ans==1)
    ids=ElementsNumpyArray[idx,0]
    ans=np.array(ids,dtype=np.int32) 
    del ElementsNumpyArray,tr,id_n1s,id_n2s,id_n3s,id_tri_n1,id_tri_n2,id_tri_n3,d_id_n1s,d_id_n2s,d_id_n3s,d_id_tri_n1,d_id_tri_n2,d_id_tri_n3,d_ans,threadsperblock,blockspergrid
    return ans
    