# author: amirhossein khatami
# mail: amirkhatami@gmail.com
import numpy as np
from numba import cuda



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



def search_element(mesh,Element):
    ElementsNumpyArray=mesh.GiveJarOfElement().ToNumPyArrayWithIDs()
    id_elements=ElementsNumpyArray[:,0]
    id_n1s=ElementsNumpyArray[:,1]
    id_n2s=ElementsNumpyArray[:,2]
    id_n3s=ElementsNumpyArray[:,3]
    id_tri_n1=Element.Give_n1().GiveID()
    id_tri_n2=Element.Give_n2().GiveID()
    id_tri_n3=Element.Give_n3().GiveID()
    
    id_n1s    =np.array(id_n1s,dtype=np.int32)
    id_n2s    =np.array(id_n2s,dtype=np.int32)
    id_n3s    =np.array(id_n3s,dtype=np.int32)
    id_tri_n1 = np.int32(id_tri_n1)
    id_tri_n2 = np.int32(id_tri_n2)
    id_tri_n3 = np.int32(id_tri_n3)
    ans       = np.zeros(len(id_n1s),dtype=np.int32)

    for i in range(len(ans)):
        ans[i]=checker(id_n1s[i],id_n2s[i],id_n3s[i],id_tri_n1,id_tri_n2,id_tri_n3)
        
    idx=np.argwhere(ans==1)
    ids=ElementsNumpyArray[idx,0]
    ans=np.array(ids,dtype=np.int32)

    return ans