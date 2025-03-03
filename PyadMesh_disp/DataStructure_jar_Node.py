# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import numpy as np
import math

class JarOfNodes:
    """This class is used to store all the nodes in a list.
    
    Attributes:
        nodes (list): A list of nodes.
    """
    
    def __init__(self):
        """The constructor for JarOfNodes class."""
        self.nodes = []

    def addNode(self,node):
        """This function is used to add a node to the jar.
        
        Args:
            node (Node): The node to be added.
        """       
        for i in self.nodes:
            if i.Give_x() == node.Give_x() and i.Give_y() == node.Give_y():
                if i.GiveID == node.GiveID:
                    print("Error: Node with same coordinates and ID")
                    raise "Error: Node with same coordinates and ID"
                    
                else :
                    print ("Error: Node with same coordinates but different ID")
                    raise "Error: Node with same coordinates but different ID"
        
        self.nodes.append(node)
                    
    def addNodes(self,*args):
        """This function is used to add multiple nodes to the jar.
        
        Args:
            *args (Node): The nodes to be added.
        """
        for i in args:
            self.addNode(i)
            
    def GiveNodes(self):
        """This function is used to return the nodes in the jar.
        
        Returns:
            list: The nodes in the jar.
        """
        return self.nodes
    
    def GiveNodeWithID(self,id):
        """This function is used to return the node with the given ID.
        
        Args:
            id (int): The ID of the node.
            
        Returns:
            Node: The node with the given ID.
        """
        for i in self.nodes:
            if i.GiveID() == id:
                return i
                break
        
        print ("Error: Node with " + str(id) + " not found")
        raise "Error: Node with ID not found"
    
    def GiveNodeWithCoordinates(self,x,y):
        """This function is used to return the node with the given coordinates.
        
        Args:
            x (float): The x coordinate of the node.
            y (float): The y coordinate of the node.
            
        Returns:
            Node: The node with the given coordinates.
        """
        telerance=1e-7
        for i in self.nodes:
            if abs(i.Give_x() - x)<telerance and abs(i.Give_y() -y)<telerance:
                return i
            else:
                pass
        print ("Error: Node with coordinates not found")
        raise "Error: Node with coordinates not found"
    
    def GiveNodeWithIndex(self,index):
        """This function is used to return the node with the given index.
        
        Args:
            index (int): The index of the node.
            
        Returns:
            Node: The node with the given index.
        """
        return self.nodes[index]
    
    def GiveSize(self):
        """This function is used to return the size of the jar.
        
        Returns:
            int: The size of the jar.
        """
        return len(self.nodes)
    
    def ToMatrix(self):
        """This function is used to return the nodes in the jar as a matrix.
        
        Returns:
            list: The nodes in the jar as a matrix.
        """
        return [i.ToMatrix() for i in self.nodes]
    
    def ToMatrixWithID(self):
        """This function is used to return the nodes in the jar as a matrix with ID.
        
        Returns:
            list: The nodes in the jar as a matrix with ID.
        """ 
        return [i.ToMatrixWithID() for i in self.nodes]
    
    def ToMatrixWithDisplacement(self):
        """This function is used to return the nodes in the jar as a matrix with displacement.
        
        Returns:
            list: The nodes in the jar as a matrix.
        """ 
        return [i.ToMatrixWithDisplacement() for i in self.nodes]
    
    def ToMatrixWithIDAndDisplacement(self):
        """This function is used to return the nodes in the jar as a matrix with ID and displacement.
        
        Returns:
            list: The nodes in the jar as a matrix.
        """
        return [i.ToMatrixWithIDAndDisplacement() for i in self.nodes]
      
    def ToNumPyArray(self):
        """This function is used to return the nodes in the jar as a numpy array.
        
        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array.
        """
        return np.array(self.ToMatrix())
    
    def ToNumPyArrayWithID(self):
        """This function is used to return the nodes in the jar as a numpy array with ID.
        
        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array with ID.
        """
        return np.array(self.ToMatrixWithID())
    
    def ToNumPyArrayWithDisplacement(self):
        """This function is used to return the nodes in the jar as a numpy array with displacement.
        
        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array.
        """
        return np.array(self.ToMatrixWithDisplacement())
    
    def ToNumPyArrayWithIDAndDisplacement(self):
        """This function is used to return the nodes in the jar as a numpy array with ID and displacement.
        
        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array.
        """
        return np.array(self.ToMatrixWithIDAndDisplacement())
    