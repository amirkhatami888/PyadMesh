# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
# import cupy as cp
import numpy as cp

def regressor(Data,x,y):
    """this fuction for fitting data with two input variables   

    Args:
        Data (numpy array): input data with two input variables and one output variable
        x (float): first input variable  
        y (float): second input variable

    Returns:
        float: prediction of output variable
    """
    #discrete data in to input and output
    X=Data[:,:-1]
    Y=Data[:,-1]
    # convert to cupy array
    X=cp.asarray(X,dtype=cp.float64)
    Y=cp.asarray(Y,dtype=cp.float64)

    x=cp.float64(x)
    y=cp.float64(y)
 
    # least square fitting with two input variables
    X=cp.hstack((X,cp.ones((X.shape[0],1))))
    
    # x^T*x
    XTX=cp.dot(X.T,X)
    # (x^T*x)^-1
    XTX_inv=cp.linalg.inv(XTX)
    # x^T*y
    XTY=cp.dot(X.T,Y)
    # (x^T*x)^-1*x^T*y
    coeff=cp.dot(XTX_inv,XTY)
    # coeff=cp.asnumpy(coeff)
    # prediction
    prediction=coeff[0]*x+coeff[1]*y+coeff[2]
    # convert to numpy array
    del X,Y,XTX,XTX_inv,XTY,coeff
    return float(prediction)
    
