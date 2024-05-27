import numpy as np
import math
import numba as nb
from numba import cuda

@cuda.jit('float64(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def calculator_N1(x1,y1,x2,y2,x3,y3,x_A,y_A):
    """this function is used to calculate the N1 of the point
    Args:
        x1 (float): x of point first vertex
        y1 (float): y of point first vertex
        x2 (float): x of point second vertex
        y2 (float): y of point second vertex
        x3 (float): x of point third vertex
        y3 (float): y of point third vertex
        x_A (float): x of point A
        y_A (float): y of point A
    Returns:
        float: the N1 of the point
    """
    return (x2*y3-y2*x3-x_A*y3+x_A*y2+y_A*x3-y_A*x2)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)

@cuda.jit('float64(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def calculator_N2(x1,y1,x2,y2,x3,y3,x_A,y_A):
    """this function is used to calculate the N2 of the point
    Args:
        x1 (float): x of point first vertex
        y1 (float): y of point first vertex
        x2 (float): x of point second vertex
        y2 (float): y of point second vertex
        x3 (float): x of point third vertex
        y3 (float): y of point third vertex
        x_A (float): x of point A
        y_A (float): y of point A
    Returns:
        float: the N2 of the point
    """
    return (x_A*y3-y_A*x3-x1*y3+x1*y_A+y1*x3-y1*x_A)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)

@cuda.jit('float64(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def calculator_N3(x1,y1,x2,y2,x3,y3,x_A,y_A):
    """this function is used to calculate the N3 of the point
    Args:
        x1 (float): x of point first vertex
        y1 (float): y of point first vertex
        x2 (float): x of point second vertex
        y2 (float): y of point second vertex
        x3 (float): x of point third vertex
        y3 (float): y of point third vertex
        x_A (float): x of point A
        y_A (float): y of point A
    Returns:
        float: the N3 of the point
    """
    return (x2*y_A-y2*x_A-x1*y_A+x1*y2+y1*x_A-y1*x2)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)



@cuda.jit('void(float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:,:])')
def calculator_N(point_x,point_y,x_a,y_a,x_b,y_b,x_c,y_c,N):
    """this function is used to calculate the N of the point
    Args:
        point_x (numpy array float64): x of point O
        point_y (numpy array float64): y of point O
        x_a (numpy array float64): x of point first vertex
        y_a (numpy array float64): y of point first vertex
        x_b (numpy array float64): x of point second vertex
        y_b (numpy array float64): y of point second vertex
        x_c (numpy array float64): x of point third vertex
        y_c (numpy array float64): y of point third vertex
        N (numpy array float64): the N of the point
    """
    i = cuda.grid(1)
    if i < len(point_x):
        N[i,0]=calculator_N1(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x[i],point_y[i])
        N[i,1]=calculator_N2(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x[i],point_y[i])
        N[i,2]=calculator_N3(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x[i],point_y[i])



def mul_calculator_N(points, Elements,thread_x=32,thread_y=32):
    """this function is used to calculate the N of the point
    Args:
        points (numpy array float64): the points
        Elements (numpy array float64): the elements
    Returns:
        numpy array float64: the N of the point
    """
    d_N = cuda.device_array((len(points), 3), dtype=np.float64)
    d_element_n1_xs = cuda.to_device(np.ascontiguousarray(Elements[:, 1].flatten(), dtype=np.float64))
    d_element_n1_ys = cuda.to_device(np.ascontiguousarray(Elements[:, 2].flatten(), dtype=np.float64))
    d_element_n2_xs = cuda.to_device(np.ascontiguousarray(Elements[:, 3].flatten(), dtype=np.float64))
    d_element_n2_ys = cuda.to_device(np.ascontiguousarray(Elements[:, 4].flatten(), dtype=np.float64))
    d_element_n3_xs = cuda.to_device(np.ascontiguousarray(Elements[:, 5].flatten(), dtype=np.float64))
    d_element_n3_ys = cuda.to_device(np.ascontiguousarray(Elements[:, 6].flatten(), dtype=np.float64))
    d_point_x = cuda.to_device(np.ascontiguousarray(points[:, 0], dtype=np.float64))
    d_point_y = cuda.to_device(np.ascontiguousarray(points[:, 1], dtype=np.float64))
    threadsperblock = (int(thread_x), int(thread_y))
    blockspergrid_x = math.ceil(len(Elements) / threadsperblock[0])
    blockspergrid_y = math.ceil(len(points) / threadsperblock[1])
    blockspergrid = (blockspergrid_x, blockspergrid_y)
    calculator_N[blockspergrid, threadsperblock](d_point_x, d_point_y, d_element_n1_xs, d_element_n1_ys,
                                                                 d_element_n2_xs, d_element_n2_ys, d_element_n3_xs,
                                                                 d_element_n3_ys, d_N)


    return d_N


#test

def validation(point,element):
    x=point[0]
    y=point[1]
    x1=element[1]
    y1=element[2]
    x2=element[3]
    y2=element[4]
    x3=element[5]
    y3=element[6]
    area=np.linalg.det(np.array([[1,x1,y1],[1,x2,y2],[1,x3,y3]],dtype=np.float64))
    N1=np.float64(np.linalg.det(np.array([[1,x,y],[1,x2,y2],[1,x3,y3]],dtype=np.float64))/area)
    N2=np.float64(np.linalg.det(np.array([[1,x1,y1],[1,x,y],[1,x3,y3]],dtype=np.float64))/area)
    N3=np.float64(np.linalg.det(np.array([[1,x1,y1],[1,x2,y2],[1,x,y]],dtype=np.float64))/area)
    return [N1,N2,N3]


def wr(point,element):
    x_A=point[0]
    y_A=point[1]
    x1=element[1]
    y1=element[2]
    x2=element[3]
    y2=element[4]
    x3=element[5]
    y3=element[6]
    N1=(x2*y3-y2*x3-x_A*y3+x_A*y2+y_A*x3-y_A*x2)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)
    N2=(x_A*y3-y_A*x3-x1*y3+x1*y_A+y1*x3-y1*x_A)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)
    N3=(x2*y_A-y2*x_A-x1*y_A+x1*y2+y1*x_A-y1*x2)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)
    return [N1,N2,N3]
    
point = np.array([0.1,0.1],dtype=np.float64)
element = np.array([1,0,0,1,0,0,1],dtype=np.float64)
N=mul_calculator_N(np.array([point]),np.array([element]))
print(N.copy_to_host())
print(validation(point,element))
print(wr(point,element))

