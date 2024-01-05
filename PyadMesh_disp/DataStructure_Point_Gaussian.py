# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import math
import numpy as np

class GaussianPoint:
    """this class is used to store all the gussian points in a list
    attributes:
        x: the x coordinate of the gussian point
        y: the y coordinate of the gussian point
        gradient: the gradient of the gussian point
        element: the element that the gussian point belongs to
    """
    def __init__(self,  x, y, gradient):
        """
        the constructor for GaussianPoint class
        """
        self.x = x
        self.y = y
        self.element=None
        self.gradient=gradient 
        
    def set_gradient(self, gradient):
        """this function is used to set the gradient of the gussian point
        Args:
            gradient(float): the gradient of the gussian point
        """
        self.gradient = gradient

    def Give_x(self):
        """this function is used to return the x coordinate of the gussian point
        Returns:
            float: the x coordinate of the gussian point
        """
        return self.x
    
    def Give_y(self):
        """this function is used to return the y coordinate of the gussian point
        Returns:
            float: the y coordinate of the gussian point
        """
        return self.y
    
    def Give_gradient(self):
        """this function is used to return the gradient of the gussian point
        Returns:
            float: the gradient of the gussian point
        """
        return self.gradient
    
    def  setElement(self, element):
        """this function is used to set the element that the gussian point belongs to
        Args:
            element(Element): the element that the gussian point belongs to
        """
        self.element=element
    
    def distanceToCenter(self):
        """this function is used to return the distance of the gussian point to the center of the element
        Returns:
            float: the distance of the gussian point to the center of the element
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def distanceToPoint(self, other):
        """this function is used to return the distance of the gussian point to another gussian point
        Args:
            other(GussianPoint): the other gussian point
        Returns:
            float: the distance of the gussian point to the other gussian point
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def ToMatrix(self):
        """this function is used to return the gussian point as a matrix
    
        Returns:
            list: the gussian point as a matrix
        """
        return [self.x, self.y , self.gradient]
    
    def ToMatrixWithCoordinates(self):
        """this function is used to return the gussian point as a matrix with coordinates

        Returns:
            list: the gussian point as a matrix with coordinates
        """
        return [self.x, self.y, self.gradient]
    
    def ToNumPyArray(self):
        """this function is used to return the gussian point as a numpy array

        Returns:
            numpy array: the gussian point as a numpy array
        """
        return np.array([self.x, self.y, self.gradient])
    
    def ToNumPyArrayWithCoordinates(self):
        """this function is used to return the gussian point as a numpy array with coordinates

        Returns:
            numpy array: the gussian point as a numpy array with coordinates
        """
        return np.array([self.x, self.y, self.gradient])
