# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import math
import numpy as np


class NodePoint:
    """This class represents a node point in a mesh.

    Attributes:
        id (int): The id of the node.
        x (float): The x coordinate of the node.
        y (float): The y coordinate of the node.
        U1 (float): Displacement in the x-direction.
        U2 (float): Displacement in the y-direction.
        nearestElements (set): Set of nearest elements to the node.
    """
    def __init__(self,id, x, y,displacement=None,stepSize=None):
        """Constructor for NodePoint class.

        Args:
            id (int): The id of the node.
            x (float): The x coordinate of the node.
            y (float): The y coordinate of the node.
            displacement (array, optional): The displacement of the node. Defaults to None.
            stepSize (float, optional): The step size. Defaults to None.
        """
        self.id = id
        self.x = x
        self.y = y
        self.U1=None
        self.U2=None
        self.nearestElements=set()

    @property
    def adjacentNodes(self):
        """Return the adjacent nodes of the node.

        Returns:
            list: The adjacent nodes of the node.
        """
        liadjacentNodes=[]
        for element in self.nearestElements:
            for node in element.nodes:
                if node.id!=self.id:
                   liadjacentNodes.append(node)
        return list(set(liadjacentNodes))
        
    @property
    def elementSize(self):
        """Return the element size of the node.

        Returns:
            float: The element size of the node.
        """
        li=[element.elementSize for element in self.nearestElements]
        return np.mean(li)
    
    @property
    def dervirative_phi(self):
        """Return the derivative of phi of the node.

        Returns:
            float: The derivative of phi of the node.
        """
        li_phi=[]
        li_distance=[]
        li_dervirative_phi=[]
        for node in self.adjacentNodes:
            li_phi.append(node.phi)
            li_distance.append(self.distanceToPoint(node))
        for i in range(len(li_phi)):
            li_dervirative_phi.append(abs(li_phi[i]-self.phi)/li_distance[i])
        return np.max(li_dervirative_phi)

    @property
    def displacement(self):
        """Return the displacement of the node.

        Returns:
            np.array: The displacement of the node.
        """
        return np.array([[self.U1],[self.U2]])
    
    @property
    def phi(self):
        """Return the phi of the node.

        Returns:
            float: The phi of the node.
        """
        return math.sqrt(self.U1**2+self.U2**2)
    

    def distanceToPoint(self, other):
        """Return the distance of the node to another node.

        Args:
            other (NodePoint): The other node.

        Returns:
            float: The distance of the node to the other node.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def GiveID(self):
        """Return the id of the node.

        Returns:
            int: The id of the node.
        """
        return self.id
    
    def SetID(self, ID):
        """Set the id of the node.

        Args:
            ID (int): The id of the node.
        """
        self.id = id
        
    def Give_x(self):
        """Return the x coordinate of the node.

        Returns:
            float: The x coordinate of the node.
        """
        return self.x
    
    def Give_y(self):
        """Return the y coordinate of the node.

        Returns:
            float: The y coordinate of the node.
        """
        return self.y
    
    def Give_displacement(self):
        """Return the displacement of the node.

        Returns:
            float: The displacement of the node.
        """
        return self.displacement

    def ToMatrix(self):
        """Return the node as a matrix.

        Returns:
            list: The node as a matrix.
        """
        return [self.x, self.y]
    
    def ToMatrixWithID(self):
        """Return the node as a matrix with id.

        Returns:
            list: The node as a matrix with id.
        """
        return [self.id, self.x, self.y]
    
    def ToMatrixWithDisplacement(self):
        """Return the node as a matrix with displacement.

        Returns:
            list: The node as a matrix with displacement.
        """
        return [self.x, self.y, self.displacement]
    
    def ToMatrixWithIDAndDisplacement(self):
        """Return the node as a matrix with id and displacement.

        Returns:
            list: The node as a matrix with id and displacement.
        """
        return [self.id, self.x, self.y, self.displacement]
    
    def set_displacement(self, U1, U2):
        """this function is used to set the displacement of the node
        
        Args:
            displacement(float): the displacement of the node
        """
        self.U1 = U1
        self.U2 = U2