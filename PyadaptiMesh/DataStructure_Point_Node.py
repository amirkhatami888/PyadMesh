# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import math

class NodePoint:
    """this class is used to store the data of a node
    attributes:
        id: the id of the node
        x: the x coordinate of the node
        y: the y coordinate of the node
        displacement: the displacement of the node
    """
    def __init__(self,id, x, y,displacement=None,stepSize=None):
        """
        the constructor for NodePoint class
        """
        self.id = id
        self.x = x
        self.y = y
        self.displacement=displacement
        self.stepSize=stepSize

    def distanceToCenter(self):
        """this function is used to return the distance of the node to the center of the element
        Returns:
            float: the distance of the node to the center of the element
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def distanceToPoint(self, other):
        """this function is used to return the distance of the node to another node
        Args:
            other(NodePoint): the other node
        Returns:    
            float: the distance of the node to another node
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def GiveID(self):
        """this function is used to return the id of the node
        Returns:
            int: the id of the node
        """
        return self.id
    
    def SetID(self, ID):
        """this function is used to set the id of the node
        Args:
            ID(int): the id of the node
        """ 
        self.id = id
        
    def Give_x(self):
        """this function is used to return the x coordinate of the node
        Returns:
            float: the x coordinate of the node
        """ 
        return self.x
    
    def Give_y(self):
        """this function is used to return the y coordinate of the node
        Returns:
            float: the y coordinate of the node
        """

        return self.y
    
    def Give_displacement(self):
        """this function is used to return the displacement of the node
        Returns:
            float: the displacement of the node
        """
        return self.displacement
    
    def set_displacement(self, displacement):
        """this function is used to set the displacement of the node
        Args:
            displacement(float): the displacement of the node
        """
        self.displacement = displacement
    
    
    
    def ToMatrix(self):
        """this function is used to return the node as a matrix
        Returns:
            list: the node as a matrix
        """
        
        return [self.x, self.y]
    
    def ToMatrixWithID(self):
        """this function is used to return the node as a matrix with id
        Returns:
            list: the node as a matrix with id
        """
        
        return [self.id, self.x, self.y]
    
    def ToMatrixWithDisplacement(self):
        """this function is used to return the node as a matrix with displacement
        Returns:
            list: the node as a matrix with displacement
        """
        return [self.x, self.y, self.displacement]
    
    def ToMatrixWithIDAndDisplacement(self):
        """this function is used to return the node as a matrix with id and displacement
        Returns:
            list: the node as a matrix with id and displacement
        """
        return [self.id, self.x, self.y, self.displacement]
    
