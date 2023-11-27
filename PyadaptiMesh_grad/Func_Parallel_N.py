import numpy as np
import math
import numba as nb
from numba import cuda

@cuda.jit('float64(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def calculator_N1(x1,y1,x2,y2,x3,y3,x_A,y_A):
    return (x2*y3-y2*x3-x_A*y3+x_A*y2+y_A*x3-y_A*x2)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)

@cuda.jit('float64(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def calculator_N2(x1,y1,x2,y2,x3,y3,x_A,y_A):
    return (x_A*y3-y_A*x3-x1*y3+x1*y_A+y1*x3-y1*x_A)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)

@cuda.jit('float64(float64,float64,float64,float64,float64,float64,float64,float64)',device=True)
def calculator_N3(x1,y1,x2,y2,x3,y3,x_A,y_A):
    return (x2*y_A-y2*x_A-x1*y_A+x1*y2+y1*x_A-y1*x2)/(x2*y3-y2*x3-x1*y3+x1*y2+y1*x3-y1*x2)



@cuda.jit('void(float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:,:])')
def calculator_N(point_x,point_y,x_a,y_a,x_b,y_b,x_c,y_c,N):
    i = cuda.grid(1)
    if i < len(point_x):
        N[i,1]=calculator_N1(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x[i],point_y[i])
        N[i,2]=calculator_N2(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x[i],point_y[i])
        N[i,3]=calculator_N3(x_a[i],y_a[i],x_b[i],y_b[i],x_c[i],y_c[i],point_x[i],point_y[i])



def mul_calculator_N(points, Elements,thread_x=32,thread_y=32):

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


