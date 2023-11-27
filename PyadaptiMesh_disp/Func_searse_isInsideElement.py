# author: amirhossein khatami
# mail: amirkhatami@gmail.com
import numpy as np
import math





def checker(x_a,y_a,x_b,y_b,x_c,y_c,O_x,O_y):
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

