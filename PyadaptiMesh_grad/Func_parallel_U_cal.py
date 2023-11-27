import numpy as np
import numba as nb
from numba import cuda, float64
import math
@cuda.jit('float64(float64,float64,float64,float64,float64,float64)',device=True)
def U1_calculator_kernel(N1,N2,N3,U1_1,U1_2,U1_3):
    return N1*U1_1+N2*U1_2+N3*U1_3

@cuda.jit('float64(float64,float64,float64,float64,float64,float64)',device=True)
def U2_calculator_kernel(N1,N2,N3,U2_1,U2_2,U2_3):
    return N1*U2_1+N2*U2_2+N3*U2_3

@cuda.jit('void(float64[:,:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:],float64[:,:])')
def U_calculator_kernel(N,U1_1,U1_2,U1_3,U2_1,U2_2,U2_3,U_ans):
    i = cuda.grid(1)
    if i < len(U1_1):
        U_ans[i,0]=U1_calculator_kernel(N[i,1],N[i,2],N[i,3],U1_1[i],U1_2[i],U1_3[i])
        U_ans[i,1]=U2_calculator_kernel(N[i,1],N[i,2],N[i,3],U2_1[i],U2_2[i],U2_3[i])

def mul_calculator_U(N,U,thread=32):
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