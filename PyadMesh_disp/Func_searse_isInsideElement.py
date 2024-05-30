# author: amirhossein khatami
# mail: amirkhatami@gmail.com
import numpy as np
import math

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

def kernel_check_PointIsInsideElements(point,ElementsMatrixWithCoordinates):
    """this function is used to check if the point is inside the triangle or not
    Args:
        point (numpy array float64): x and y of point O
        ElementsMatrixWithCoordinates (numpy array float64): the elements matrix with coordinates
    Returns:
        numpy array int32: 1 if the point is inside the triangle and -1 if the point is outside the triangle
    """
    ans           = np.array  (np.empty(len(ElementsMatrixWithCoordinates)), dtype=np.int32 )
    element_n1_xs = np.array  (ElementsMatrixWithCoordinates[:,1].flatten(), dtype=np.float64)
    element_n1_ys = np.array  (ElementsMatrixWithCoordinates[:,2].flatten(), dtype=np.float64)
    element_n2_xs = np.array  (ElementsMatrixWithCoordinates[:,3].flatten(), dtype=np.float64)
    element_n2_ys = np.array  (ElementsMatrixWithCoordinates[:,4].flatten(), dtype=np.float64)
    element_n3_xs = np.array  (ElementsMatrixWithCoordinates[:,5].flatten(), dtype=np.float64)
    element_n3_ys = np.array  (ElementsMatrixWithCoordinates[:,6].flatten(), dtype=np.float64)
    point_x       = float(point[0])
    point_y       = float(point[1])
    for i in range(len(element_n1_xs)):
        ans[i]=checker(element_n1_xs[i],element_n1_ys[i],element_n2_xs[i],element_n2_ys[i],element_n3_xs[i],element_n3_ys[i],point_x,point_y)
    
    index=np.argwhere(ans==1).flatten()
    element_id=ElementsMatrixWithCoordinates[index,0].flatten()
    return element_id

