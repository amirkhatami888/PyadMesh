# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np

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
    
    #convert data to numpy array
    X=np.array(X,dtype=np.float64)
    Y=np.array(Y,dtype=np.float64)
    x=np.float64(x)
    y=np.float64(y)
 
    # least square fitting with two input variables
    X=np.hstack((X,np.ones((X.shape[0],1))))
    # x^T*x
    XTX=np.dot(X.T,X)
    # (x^T*x)^-1
    XTX_inv=np.linalg.inv(XTX)
    # x^T*y
    XTY=np.dot(X.T,Y)
    # (x^T*x)^-1*x^T*y
    coeff=np.dot(XTX_inv,XTY)
    # prediction
    prediction=coeff[0]*x+coeff[1]*y+coeff[2]
    del X,XTX,XTX_inv,XTY,coeff
    return prediction

    
