# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
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
    X=np.array(X,dtype=np.float64)
    Y=np.array(Y,dtype=np.float64)
    x=np.float64(x)
    y=np.float64(y)

    # finding the best degree for polynomial fitting using cross-validation for least squre method
    degrees = range(1, len(X[0]))

    # degrees = [1]
    MSEs = []
    for degree in degrees :
        coef = np.polyfit(X[:,0], Y, degree)
        y_pred = np.polyval(coef, X[:,0])
        MSE = np.mean((Y - y_pred)**2)
        MSEs.append(MSE)
    bestdegree = degrees[MSEs.index(min(MSEs))]
    # fitting the data with the best degree
    coef = np.polyfit(X[:,0], Y, bestdegree)
    y_pred = np.polyval(coef, X[:,0])
    y_ = np.polyval(coef, x)
    return float(y_)
        