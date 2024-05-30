# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import math
import numpy as np

class GaussianPoint:
    """This class is used to store all the Gaussian points.

    Attributes:
        x (float): The x coordinate of the Gaussian point.
        y (float): The y coordinate of the Gaussian point.
        gradient (float): The gradient of the Gaussian point.
        element (Element): The element that the Gaussian point belongs to.
    """
    def __init__(self,  x, y, gradient):
        """The constructor for GaussianPoint class."""
        self.x = x
        self.y = y
        self.element=None
        self.gradient=gradient 
        
    def set_gradient(self, gradient):
        """Set the gradient of the Gaussian point.
        
        Args:
            gradient (float): The gradient of the Gaussian point.
        """
        self.gradient = gradient

    def Give_x(self):
        """Return the x coordinate of the Gaussian point.

        Returns:
            float: The x coordinate of the Gaussian point.
        """
        return self.x
    
    def Give_y(self):
        """Return the y coordinate of the Gaussian point.

        Returns:
            float: The y coordinate of the Gaussian point.
        """
        return self.y
    
    def Give_gradient(self):
        """Return the gradient of the Gaussian point.

        Returns:
            float: The gradient of the Gaussian point.
        """
        return self.gradient
    
    def  setElement(self, element):
        """Set the element that the Gaussian point belongs to.
        
        Args:
            element (Element): The element that the Gaussian point belongs to.
        """
        self.element=element
    
    def distanceToCenter(self):
        """Return the distance of the Gaussian point to the center of the element.

        Returns:
            float: The distance of the Gaussian point to the center of the element.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def distanceToPoint(self, other):
        """Return the distance of the Gaussian point to another Gaussian point.

        Args:
            other (GaussianPoint): The other Gaussian point.

        Returns:
            float: The distance of the Gaussian point to the other Gaussian point.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def ToMatrix(self):
        """Return the Gaussian point as a matrix.

        Returns:
            list: The Gaussian point as a matrix.
        """
        return [self.x, self.y , self.gradient]
    
    def ToMatrixWithCoordinates(self):
        """Return the Gaussian point as a matrix with coordinates.

        Returns:
            list: The Gaussian point as a matrix with coordinates.
        """
        return [self.x, self.y, self.gradient]
    
    def ToNumPyArray(self):
        """Return the Gaussian point as a numpy array.

        Returns:
            numpy.ndarray: The Gaussian point as a numpy array.
        """
        return np.array([self.x, self.y, self.gradient])
    
    def ToNumPyArrayWithCoordinates(self):
        """Return the Gaussian point as a numpy array with coordinates.

        Returns:
            numpy.ndarray: The Gaussian point as a numpy array with coordinates.
        """
        return np.array([self.x, self.y, self.gradient])
