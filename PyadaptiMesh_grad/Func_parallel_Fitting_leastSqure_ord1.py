# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
import cupy as cp
def regressor(Data,x,y):
    """
    This function fits data with two input variables using the least squares method with Cupy.

    Args:
        Data (cupy array): Input data with two input variables and one output variable
        x (float): First input variable
        y (float): Second input variable

    Returns:
        float: Prediction of output variable
    """
    # Discrete data into input and output
    X = Data[:, :-1]
    Y = Data[:, -1]
    X = cp.array(X, dtype=cp.float32)
    Y = cp.array(Y, dtype=cp.float32)
    # Augmenting X with bias term
    X = cp.hstack((X, cp.ones((X.shape[0], 1))))

    # Finding the parameters using the least squares method
    X_transpose = cp.transpose(X)
    XTX_inv = cp.linalg.inv(cp.dot(X_transpose, X))
    XTY = cp.dot(X_transpose, Y)
    theta = cp.dot(XTX_inv, XTY)

    # Creating input array for prediction
    x_ = cp.array([[x, y, 1]])

    # Predicting the output variable
    y_ = cp.dot(x_, theta)

    return float(y_[0])