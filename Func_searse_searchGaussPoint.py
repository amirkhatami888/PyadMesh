# author: amirhossein khatami
# mail: amirkhatami@gmail.com
import numpy as np
import math



def checker(x_a, y_a, x_b, y_b, x_c, y_c, O_x, O_y):
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

    Returns:
        int: if inside element 1 otherwise -1
    """
    tolerance = 1e-10
    if     ((x_b - x_a) * (O_y - y_a) - (y_b - y_a) * (O_x - x_a) <= tolerance and
            (x_c - x_b) * (O_y - y_b) - (y_c - y_b) * (O_x - x_b) <= tolerance and
            (x_a - x_c) * (O_y - y_c) - (y_a - y_c) * (O_x - x_c) <= tolerance) or (
            (x_b - x_a) * (O_y - y_a) - (y_b - y_a) * (O_x - x_a) >= -1*tolerance and
            (x_c - x_b) * (O_y - y_b) - (y_c - y_b) * (O_x - x_b) >= -1*tolerance and
            (x_a - x_c) * (O_y - y_c) - (y_a - y_c) * (O_x - x_c) >= -1*tolerance):
        return 1
    else:
        return -1

        


def search_GaussPoint(Element,Gpoints):
    """this function using checker and check_PointIsInsideTriangles is
    
    Args:
        Element (Triangle_order1): element of triangle
        Gpoints (2d numpy array ): numpy array of coordinate of point checking
    
    Returns:
        numpy array : numpy array of answer of result
    """

    ans           = np.empty(len(Gpoints), dtype=np.int32)
    element_n1_x = np.float64(Element.Give_n1().Give_x())
    element_n1_y = np.float64(Element.Give_n1().Give_y())
    element_n2_x = np.float64(Element.Give_n2().Give_x())
    element_n2_y = np.float64(Element.Give_n2().Give_y())
    element_n3_x = np.float64(Element.Give_n3().Give_x())
    element_n3_y = np.float64(Element.Give_n3().Give_y())

    point_xs=np.array(Gpoints[:,0],dtype=np.float64).flatten()
    point_ys=np.array(Gpoints[:,1],dtype=np.float64).flatten()

    
    for i in range(len(point_xs)):
        ans[i]=checker(element_n1_x,element_n1_y,element_n2_x,element_n2_y,element_n3_x,element_n3_y,point_xs[i],point_ys[i])

    index=np.argwhere(ans==1).flatten()
    Gpoint=list(Gpoints[index])
    return Gpoint

    
    



