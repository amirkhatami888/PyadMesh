# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import numpy as np
import numba as nb
from numba import cuda, float64
import math

@cuda.jit('float64(float64,float64,float64,float64,float64,float64)',device=True)
def U1_calculator_kernel(N1,N2,N3,U1_1,U1_2,U1_3):
    """this function is used to calculate the U1 of the point
    Args:
        N1 (float): N1 of the point
        N2 (float): N2 of the point
        N3 (float): N3 of the point
        U1_1 (float): U1 of the first vertex
        U1_2 (float): U1 of the second vertex
        U1_3 (float): U1 of the third vertex
    Returns:
        float: the U1 of the point
    """
    return N1*U1_1+N2*U1_2+N3*U1_3

@cuda.jit('float64(float64,float64,float64,float64,float64,float64)',device=True)
def U2_calculator_kernel(N1,N2,N3,U2_1,U2_2,U2_3):
    """this function is used to calculate the U2 of the point
    Args:
        N1 (float): N1 of the point
        N2 (float): N2 of the point
        N3 (float): N3 of the point
        U2_1 (float): U2 of the first vertex
        U2_2 (float): U2 of the second vertex
        U2_3 (float): U2 of the third vertex
    Returns:
        float: the U2 of the point
    """
    return N1*U2_1+N2*U2_2+N3*U2_3

@cuda.jit('void(float64[:,:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:,:])')
def U_calculator_kernel(N,U1_1,U1_2,U1_3,U2_1,U2_2,U2_3,U_ans):
    """this function is used to calculate the U of the point
    Args:
        N (numpy array float64): N of the point
        U1_1 (numpy array float64): U1 of the first vertex
        U1_2 (numpy array float64): U1 of the second vertex
        U1_3 (numpy array float64): U1 of the third vertex
        U2_1 (numpy array float64): U2 of the first vertex
        U2_2 (numpy array float64): U2 of the second vertex
        U2_3 (numpy array float64): U2 of the third vertex
        U_ans (numpy array float64): U of the point
    """
    i = cuda.grid(1)
    if i < len(U1_1):
        U_ans[i,0]=U1_calculator_kernel(N[i,1],N[i,2],N[i,3],U1_1[i],U1_2[i],U1_3[i])
        U_ans[i,1]=U2_calculator_kernel(N[i,1],N[i,2],N[i,3],U2_1[i],U2_2[i],U2_3[i])

def mul_calculator_U(N,U,thread=32):
    """this function is used to calculate the U of the point
    Args:
        N (numpy array float64): N of the point
        U (numpy array float64): U of the point
    Returns:
        numpy array float64: U of the point
    """
    U1_1=cuda.to_device(np.ascontiguousarray(U[:, 0].flatten(), dtype=np.float64))
    U2_1=cuda.to_device(np.ascontiguousarray(U[:, 1].flatten(), dtype=np.float64))
    U1_2=cuda.to_device(np.ascontiguousarray(U[:, 2].flatten(), dtype=np.float64))
    U2_2=cuda.to_device(np.ascontiguousarray(U[:, 3].flatten(), dtype=np.float64))
    U1_3=cuda.to_device(np.ascontiguousarray(U[:, 4].flatten(), dtype=np.float64))
    U2_3=cuda.to_device(np.ascontiguousarray(U[:, 5].flatten(), dtype=np.float64))
    U_ans = cuda.device_array((len(U1_1), 2), dtype=np.float64)
    threadsperblock = int(thread)
    blockspergrid = math.ceil(len(U1_1) / threadsperblock)
    U_calculator_kernel[blockspergrid, threadsperblock](N,U1_1,U1_2,U1_3,U2_1,U2_2,U2_3,U_ans)
    ans = U_ans.copy_to_host()
    ans=np.array(ans,dtype=np.float64)
    return ans