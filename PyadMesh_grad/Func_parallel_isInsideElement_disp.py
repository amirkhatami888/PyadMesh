# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import numba as nb
from numba import cuda

@cuda.jit('int32(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def checker(x_a,y_a,x_b,y_b,x_c,y_c,O_x,O_y):
    """this function is used to check if the point is inside the element
    Args:
        x_a (float): the x coordinate of the first node of the element
        y_a (float): the y coordinate of the first node of the element
        x_b (float): the x coordinate of the second node of the element
        y_b (float): the y coordinate of the second node of the element
        x_c (float): the x coordinate of the third node of the element
        y_c (float): the y coordinate of the third node of the element
        O_x (float): the x coordinate of the point
        O_y (float): the y coordinate of the point
    Returns:
        int: 1 if the point is inside the element and -1 if the point is outside the element
    """
    telerance=1e-12
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
    """this function is used to check if the points are inside the elements
    Args:
        point_x (numpy array): the x coordinates of the points
        point_y (numpy array): the y coordinates of the points
        x_a (numpy array): the x coordinates of the first node of the elements
        y_a (numpy array): the y coordinates of the first node of the elements
        x_b (numpy array): the x coordinates of the second node of the elements
        y_b (numpy array): the y coordinates of the second node of the elements
        x_c (numpy array): the x coordinates of the third node of the elements
        y_c (numpy array): the y coordinates of the third node of the elements
        ans (numpy array): the answer
    """
    i, j = cuda.grid(2)
    if i < ans.shape[0] and j < ans.shape[1]:
        ans[i, j] = checker(x_a[i], y_a[i], x_b[i], y_b[i], x_c[i], y_c[i], point_x[j], point_y[j])




def mul_kernel_check_PointIsInsideElements(points, ElementsMatrixWithCoordinates,thread_x=32,thread_y=32):
    """this function is used to check if the points are inside the elements
    Args:
        points (numpy array): the points
        ElementsMatrixWithCoordinates (numpy array): the elements
    Returns:
        list: the list of elements that the points are inside
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
            li.append(list(ElementsMatrixWithCoordinates[indx[0],:]))
        else:
            li.append(None)
    
    return li



