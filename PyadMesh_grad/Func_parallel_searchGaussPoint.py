import numpy as np
from numba import cuda

@cuda.jit('int32(float64,float64,float64,float64,float64,float64,float64,float64)', device=True)
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
    tolerance = 1e-12
    if ((x_b - x_a) * (O_y - y_a) - (y_b - y_a) * (O_x - x_a) <=    tolerance and
        (x_c - x_b) * (O_y - y_b) - (y_c - y_b) * (O_x - x_b) <=    tolerance and
        (x_a - x_c) * (O_y - y_c) - (y_a - y_c) * (O_x - x_c) <=    tolerance) or (
        (x_b - x_a) * (O_y - y_a) - (y_b - y_a) * (O_x - x_a) >= -1*tolerance and
        (x_c - x_b) * (O_y - y_b) - (y_c - y_b) * (O_x - x_b) >= -1*tolerance and
        (x_a - x_c) * (O_y - y_c) - (y_a - y_c) * (O_x - x_c) >= -1*tolerance):
        return 1
    else:
        return -1

@cuda.jit('void(float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],int32[:,:])')
def mul_check_PointIsInsideTriangles(point_xs, point_ys, x_a, y_a, x_b, y_b, x_c, y_c, ans):
    """this function by using checker ,check elements points inside them or not 

    Args:
        point_xs (numpy array float64): x of points
        point_ys (numpy array float64): y of points
        x_a (numpy array float64): xs of a vertex a's 
        y_a (numpy array float64): ys of a vertex a's    
        x_b (numpy array float64): xs of a vertex b's
        y_b (numpy array float64): ys of a vertex b's 
        x_c (numpy array float64): xs of a vertex c's
        y_c (numpy array float64): ys of a vertex c's
        ans (2D numpy array float64): array of answer of result
    """
    # Get the thread's location in the grid]
    i, j = cuda.grid(2)
    # Check array boundaries
    if i < point_xs.shape[0] and j < x_a.shape[0]:
    # Check if the point is inside the triangle
        ans[i, j] = checker(x_a[j], y_a[j], x_b[j], y_b[j], x_c[j], y_c[j], point_xs[i], point_ys[i])

def mul_search_GaussPoint(Elements, Gpoints,thread_x=32,thread_y=32):
    """this function using checker and check_PointIsInsideTriangles is 

    Args:
        Elements (2d numpy array float64):numpy array of coordinate of vertexs
        Gpoints (2d numpy array ): numpy array of coordinate of point checking

    Returns:
        numpy array : numpy array of answer of result
    """
    ans =cuda.to_device(np.zeros((Gpoints.shape[0], Elements.shape[0]), dtype=np.int32))
    element_n1_xs = cuda.to_device(np.array(Elements[:, 0], dtype=np.float64).flatten())
    element_n1_ys = cuda.to_device(np.array(Elements[:, 1], dtype=np.float64).flatten())
    element_n2_xs = cuda.to_device(np.array(Elements[:, 2], dtype=np.float64).flatten())
    element_n2_ys = cuda.to_device(np.array(Elements[:, 3], dtype=np.float64).flatten())
    element_n3_xs = cuda.to_device(np.array(Elements[:, 4], dtype=np.float64).flatten())
    element_n3_ys = cuda.to_device(np.array(Elements[:, 5], dtype=np.float64).flatten())
    d_point_xs = cuda.to_device(np.array(Gpoints[:, 0], dtype=np.float64).flatten())
    d_point_ys = cuda.to_device(np.array(Gpoints[:, 1], dtype=np.float64).flatten())

    # Define the grid and block dimensions
    threadsperblock = (int(thread_x), int(thread_y))
    blockspergrid_x = (Gpoints.shape[0] + threadsperblock[0] - 1) // threadsperblock[0]
    blockspergrid_y = (Elements.shape[0] + threadsperblock[1] - 1) // threadsperblock[1]
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    # Start the kernel
    mul_check_PointIsInsideTriangles[blockspergrid, threadsperblock](d_point_xs, d_point_ys, element_n1_xs, element_n1_ys, element_n2_xs, element_n2_ys, element_n3_xs, element_n3_ys, ans)
    ans= ans.copy_to_host()
    li_ans=[]
    for i in range(ans.shape[1]):
        idx=np.argwhere(ans[:, i] == 1)
        idx=idx.flatten()
        li_ans.extend(Gpoints[idx, :])
    return np.array(li_ans, dtype=np.float64)
            
        


@cuda.jit('void(float64[:],float64[:],float64,float64,float64,float64,float64,float64,int32[:])')
def one_check_PointIsInsideTriangles(point_xs,point_ys,x_a,y_a,x_b,y_b,x_c,y_c,ans):
    """this function by using checker ,check elements points inside them or not
    
    Args:
        point_xs (numpy array float64): x of points
        point_ys (numpy array float64): y of points
        x_a (float64): xs of a vertex a's
        y_a (float64): ys of a vertex a's
        x_b (float64): xs of a vertex b's
        y_b (float64): ys of a vertex b's
        x_c (float64): xs of a vertex c's
        y_c (float64): ys of a vertex c's
        ans (numpy array float64): array of answer of result
    """
    i = cuda.grid(1)
    if i < len(point_xs):
        ans[i]=checker(x_a,y_a,x_b,y_b,x_c,y_c,point_xs[i],point_ys[i])
    


def one_search_GaussPoint(Element,Gpoints,thread_x=32,thread_y=32):
    """this function using checker and check_PointIsInsideTriangles is
    
    Args:
        Element (Element): element that we want to check
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

    d_point_xs=cuda.to_device(np.array(Gpoints[:,0],dtype=np.float64).flatten())
    d_point_ys=cuda.to_device(np.array(Gpoints[:,1],dtype=np.float64).flatten())

    threadsperblock =thread_x
    blockspergrid = (len(Gpoints) + (threadsperblock - 1)) // threadsperblock
    
    one_check_PointIsInsideTriangles[blockspergrid,threadsperblock](d_point_xs,d_point_ys,element_n1_x,element_n1_y,element_n2_x,element_n2_y,element_n3_x,element_n3_y,ans)

    index=np.argwhere(ans==1).flatten()
    Gpoint=list(Gpoints[index])
    del ans ,element_n1_x ,element_n1_y ,element_n2_x ,element_n2_y ,element_n3_x ,element_n3_y ,d_point_xs ,d_point_ys ,threadsperblock ,blockspergrid ,index
    return Gpoint

    