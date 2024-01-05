# author: amirhossein khatami
# mail: amirkhatami@gmail.com
import numpy as np
import math





def checker(x_a,y_a,x_b,y_b,x_c,y_c,O_x,O_y):
    """this function check one point is inside of triangle or not?
    
    Args:
        x_a (np.float64 ): x of Vertex a
        y_a (np.float64):  y of Vertex a
        x_b (np.float64):  x of Vertex b
        y_b (np.float64):  y of Vertex b
        x_c (np.float64):  x of Vertex c
        y_c (np.float64):  y of Vertex c
        O_x (np.float64):  x of point
        O_y (np.float64):  y of point
    
    returns:
        int: if inside element 1 otherwise -1
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
        
        



def kernel_check_PointIsInsideElements(point,ElementsMatrixWithCoordinates):
    """
    this function by using checker ,check elements points inside them or not

    Args:
        point (list): list of coordinate of point
        ElementsMatrixWithCoordinates (2d numpy array float64):numpy array of coordinate of vertexs
    
    Returns:
        numpy array : numpy array of answer of result
    """
    
    
    ans           = np.array  (np.zeros(len(ElementsMatrixWithCoordinates)), dtype=np.int32 )
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

