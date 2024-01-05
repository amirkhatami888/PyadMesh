# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import math
import numpy as np
class NodePoint:
    

    def __init__(self,id, x, y,displacement=None,stepSize=None):
        """
        the constructor for NodePoint class
        Args:
            id(int): the id of the node
            x(float): the x coordinate of the node
            y(float): the y coordinate of the node        
        """
        self.id = id
        self.x = x
        self.y = y
        self.U1=None
        self.U2=None
        self.nearestElements=set()

    @property
    def adjacentNodes(self):
        """this function is used to return the adjacent nodes of the node
        Returns:
            list: the adjacent nodes of the node
        """
        liadjacentNodes=[]
        for element in self.nearestElements:
            for node in element.nodes:
                if node.id!=self.id:
                   liadjacentNodes.append(node)
        return list(set(liadjacentNodes))
        

        
    @property
    def elementSize(self):
        """this function is used to return the element size of the node
        Returns:
            float: the element size of the node
        """
        li=[element.elementSize for element in self.nearestElements]
        return np.mean(li)
    @property
    def dervirative_phi(self):
        """this function is used to return the dervirative of phi of the node
        Returns:
            float: the dervirative of phi of the node
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
        """this function is used to return the displacement of the node
        Returns:
            np.array: the displacement of the node
        """
        return np.array([[self.U1],[self.U2]])
    @property
    def phi(self):
        """this function is used to return the phi of the node
        Returns:
            float: the phi of the node
        """
        return math.sqrt(self.U1**2+self.U2**2)
    

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
    
    def set_displacement(self, U1, U2):
        """this function is used to set the displacement of the node
        Args:
            displacement(float): the displacement of the node
        """
        self.U1 = U1
        self.U2 = U2