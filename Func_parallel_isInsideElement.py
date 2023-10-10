import numpy as np
import math
import numba as nb
from numba import cuda

@cuda.jit('int32(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def checker(x_a,y_a,x_b,y_b,x_c,y_c,O_x,O_y):
    """this function is used to check if the point is inside the triangle or not

    Args:
        x_a (float): x of point first vertex
        y_a (float): y of point first vertex
        x_b (float): x of point second vertex
        y_b (float): y of point second vertex
        x_c (float): x of point third vertex
        y_c (float): y of point third vertex
        O_x (float): x of point O
        O_y (float): y of point O

    Returns:
        int: 1 if the point is inside the triangle and -1 if the point is outside the triangle
    """
    telerance=1e-10
    if ((x_b-x_a)*(O_y-y_a)-(y_b-y_a)*(O_x-x_a) <= telerance and
        (x_c-x_b)*(O_y-y_b)-(y_c-y_b)*(O_x-x_b) <= telerance and
        (x_a-x_c)*(O_y-y_c)-(y_a-y_c)*(O_x-x_c) <= telerance) or\
        ((x_b-x_a)*(O_y-y_a)-(y_b-y_a)*(O_x-x_a) >= -telerance and 
         (x_c-x_b)*(O_y-y_b)-(y_c-y_b)*(O_x-x_b) >= -telerance and 
         (x_a-x_c)*(O_y-y_c)-(y_a-y_c)*(O_x-x_c) >= -telerance):
        return 1
    else:
        return -1
        



@cuda.jit('void(float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],int32[:,:])')
def mul_check_PointIsInsideTriangles(point_x, point_y, x_a, y_a, x_b, y_b, x_c, y_c, ans):
    """this function is used to check if the point is inside the triangle or not

    Args:
        point_x (numpy array float64): x of point O
        point_y (numpy array float64): y of point O
        x_a (numpy array float64): x of point first vertex
        y_a (numpy array float64): y of point first vertex
        x_b (numpy array float64): x of point second vertex
        y_b (numpy array float64): y of point second vertex
        x_c (numpy array float64): x of point third vertex
        y_c (numpy array float64): y of point third vertex
        ans (numpy array int32): 1 if the point is inside the triangle and -1 if the point is outside the triangle
    """
    i, j = cuda.grid(2)
    if i < ans.shape[0] and j < ans.shape[1]:
        ans[i, j] = checker(x_a[i], y_a[i], x_b[i], y_b[i], x_c[i], y_c[i], point_x[j], point_y[j])


@cuda.jit('void(float64,float64,float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],int32[:])')
def one_check_PointIsInsideTriangles(point_x,point_y,x_a,y_a,x_b,y_b,x_c,y_c,ans):
    """this function is used to check if the point is inside the triangle or not

    Args:
        point_x (float): x of point O
        point_y (float): y of point O
        x_a (numpy array float64): x of point first vertex
        y_a (numpy array float64): y of point first vertex
        x_b (numpy array float64): x of point second vertex
        y_b (numpy array float64): y of point second vertex
        x_c (numpy array float64): x of point third vertex
        y_c (numpy array float64): y of point third vertex
        ans (numpy array int32): 1 if the point is inside the triangle and -1 if the point is outside the triangle
    """
    i = cuda.grid(1)
    if i < len(x_a):
        ans[i]=checker(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x,point_y)



def mul_kernel_check_PointIsInsideElements(points, ElementsMatrixWithCoordinates,thread_x=32,thread_y=32):
    """this function is used to check if the point is inside the triangle or not

    Args:
        points (numpy array float64): x and y of points
        ElementsMatrixWithCoordinates (numpy array float64): x and y of vertices of triangles

    Returns:
        numpy array int32: 1 if the point is inside the triangle and -1 if the point is outside the triangle
    """
    d_ans = cuda.device_array((len(ElementsMatrixWithCoordinates), len(points)), dtype=np.int32)
    d_element_n1_xs = cuda.to_device(np.ascontiguousarray(ElementsMatrixWithCoordinates[:, 1].flatten(), dtype=np.float64))
    d_element_n1_ys = cuda.to_device(np.ascontiguousarray(ElementsMatrixWithCoordinates[:, 2].flatten(), dtype=np.float64))
    d_element_n2_xs = cuda.to_device(np.ascontiguousarray(ElementsMatrixWithCoordinates[:, 3].flatten(), dtype=np.float64))
    d_element_n2_ys = cuda.to_device(np.ascontiguousarray(ElementsMatrixWithCoordinates[:, 4].flatten(), dtype=np.float64))
    d_element_n3_xs = cuda.to_device(np.ascontiguousarray(ElementsMatrixWithCoordinates[:, 5].flatten(), dtype=np.float64))
    d_element_n3_ys = cuda.to_device(np.ascontiguousarray(ElementsMatrixWithCoordinates[:, 6].flatten(), dtype=np.float64))
    d_point_x = cuda.to_device(np.ascontiguousarray(points[:, 0], dtype=np.float64))
    d_point_y = cuda.to_device(np.ascontiguousarray(points[:, 1], dtype=np.float64))
    threadsperblock = (int(thread_x), int(thread_y))
    blockspergrid_x = math.ceil(len(ElementsMatrixWithCoordinates) / threadsperblock[0])
    blockspergrid_y = math.ceil(len(points) / threadsperblock[1])
    blockspergrid = (blockspergrid_x, blockspergrid_y)
    mul_check_PointIsInsideTriangles[blockspergrid, threadsperblock](d_point_x, d_point_y, d_element_n1_xs, d_element_n1_ys,
                                                                 d_element_n2_xs, d_element_n2_ys, d_element_n3_xs,
                                                                 d_element_n3_ys, d_ans)
    ans = d_ans.copy_to_host()
    ans=np.array(ans,dtype=np.int32)
    li=[]
    
    shape = (len(ElementsMatrixWithCoordinates), len(points))
    for j in range(shape[1]):
        indx=np.argwhere(ans[:,j]==1).flatten()
        if len(indx)>0:
            li.append(ElementsMatrixWithCoordinates[indx[0],0])
        else:
            li.append(None)
    
    return li




def one_kernel_check_PointIsInsideElements(point,ElementsMatrixWithCoordinates,thread_x=32,thread_y=32):
    """this function is used to check if the point is inside the triangle or not

    Args:
        point (numpy array float64): x and y of point
        ElementsMatrixWithCoordinates (numpy array float64): x and y of vertices of triangles

    Returns:
        numpy array int32: 1 if the point is inside the triangle and -1 if the point is outside the triangle
    
    """
    d_ans           = cuda.to_device(np.array  (np.empty(len(ElementsMatrixWithCoordinates)), dtype=np.int32 ))
    d_element_n1_xs = cuda.to_device(np.array  (ElementsMatrixWithCoordinates[:,1].flatten(), dtype=np.float64))
    d_element_n1_ys = cuda.to_device(np.array  (ElementsMatrixWithCoordinates[:,2].flatten(), dtype=np.float64))
    d_element_n2_xs = cuda.to_device(np.array  (ElementsMatrixWithCoordinates[:,3].flatten(), dtype=np.float64))
    d_element_n2_ys = cuda.to_device(np.array  (ElementsMatrixWithCoordinates[:,4].flatten(), dtype=np.float64))
    d_element_n3_xs = cuda.to_device(np.array  (ElementsMatrixWithCoordinates[:,5].flatten(), dtype=np.float64))
    d_element_n3_ys = cuda.to_device(np.array  (ElementsMatrixWithCoordinates[:,6].flatten(), dtype=np.float64))
    d_point_x       = float(point[0])
    d_point_y       = float(point[1])
    threadsperblock = thread_x
    blockspergrid = (len(ElementsMatrixWithCoordinates) + (threadsperblock - 1)) // threadsperblock
    one_check_PointIsInsideTriangles[blockspergrid,threadsperblock](d_point_x,d_point_y,d_element_n1_xs,d_element_n1_ys,d_element_n2_xs,d_element_n2_ys,d_element_n3_xs,d_element_n3_ys,d_ans)
    ans=d_ans.copy_to_host()
    index=np.argwhere(ans==1).flatten()
    element_id=ElementsMatrixWithCoordinates[index,0].flatten()
    del d_ans,d_element_n1_xs,d_element_n1_ys,d_element_n2_xs,d_element_n2_ys,d_element_n3_xs,d_element_n3_ys,ans,index,blockspergrid,threadsperblock,d_point_x,d_point_y,point,ElementsMatrixWithCoordinates
    return element_id

    
    
