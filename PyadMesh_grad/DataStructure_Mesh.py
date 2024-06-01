# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import math
import numpy as np

class Mesh:
    """this class is used to store all mesh data
    attributes:
        name: the name of the mesh
        JarOfNodes: a jar of nodes
        JarOfGussianPoint: a jar of gussian points
        JarOfElement: a jar of elements
    """ 
    def __init__(self,JarOfNodes=None,JarOfGussianPoint=None,JarOfElement=None):
        """
        the constructor for Mesh class
        """
        self.name = None
        self.JarOfNodes = JarOfNodes
        self.JarOfGussianPoint = JarOfGussianPoint
        self.JarOfElement = JarOfElement

    def GiveJarOfNodes(self):
        """ this function is used to return the jar of nodes

        Returns:
            list: the jar of nodes
        """
        return self.JarOfNodes
    
    def GiveJarOfGussianPoint(self):
        """ this function is used to return the jar of gussian points
    
        Returns:
            list: the jar of gussian points
        """
        return self.JarOfGussianPoint
    
    def GiveJarOfElement(self):
        """ this function is used to return the jar of elements

        Returns:
            list: the jar of elements
        """
        return self.JarOfElement
    
    def GiveNodes(self):
        """ this function is used to return the nodes in the jar
    
        Returns:
            nodes  : the nodes in the jar
        """
        return self.JarOfNodes.GiveNodes()
    
    def GiveGussianPoints(self):
        """ this function is used to return the gussian points in the jar

        Returns:
            list: the gussian points in the jar
        """
        return self.JarOfGussianPoint.GiveGussianPoints()   
    
    def GiveElements(self):
        """ this function is used to return the elements in the jar

        Returns:
            list: the elements in the jar
        """
        return self.JarOfElement.GiveElements() 
    
    def GiveNodeMatrix(self):
        """ this function is used to return the nodes in the jar as a matrix

        Returns:
            list: the nodes in the jar as a matrix
        """
        return self.JarOfNodes.ToMatrix()
    
    def GiveNodeMatrixWithID(self):
        """ this function is used to return the nodes in the jar as a matrix with ID

        Returns:
            list: the nodes in the jar as a matrix with ID
        """
        return self.JarOfNodes.ToMatrixWithID()
    
    def GiveNodeMatrixwithDisplacement(self):
        """ this function is used to return the nodes in the jar as a matrix with displacement
    
        Returns:
            list: the nodes in the jar as a matrix with displacement
        """
        return self.JarOfNodes.ToMatrixWithDisplacement()
    
    def GiveNodeNumpyArray(self):
        """ this function is used to return the nodes in the jar as a numpy array
    
        Returns:
            numpyarray: the nodes in the jar as a numpy array
        """
        return self.JarOfNodes.ToNumPyArray()
    
    def GiveNodeNumpyArrayWithID(self):
        """ this function is used to return the nodes in the jar as a numpy array with ID
    
        Returns:
            numpyarray: the nodes in the jar as a numpy array with ID
        """
        return self.JarOfNodes.ToNumPyArrayWithID()
    
    def GiveNodeCyWithDisplacement(self):
        """ this function is used to return the nodes in the jar as a numpy array with displacement
    
        Returns:
            numpyarray: the nodes in the jar as a numpy array with displacement
        """
        return self.JarOfNodes.ToMatrixWithDisplacement()
    
    def GiveNodeNumpyArrayWithDisplacementAndID(self):
        """ this function is used to return the nodes in the jar as a numpy array with displacement and ID
        
        Returns:
            numpyarray: the nodes in the jar as a numpy array with displacement and ID
        """
        return self.JarOfNodes.ToNumPyArrayWithIDAndDisplacement()
    
    def GiveElementsMatrix(self):
        """ this function is used to return the elements in the jar as a matrix

        Returns:
            list: the elements in the jar as a matrix
        """
        return self.JarOfElement.ToMatrixWithIDs()
    
    def GiveElementsMatrixWithCoordinates(self):
        """ this function is used to return the elements in the jar as a matrix with coordinates
    
        Returns:
            list: the elements in the jar as a matrix with coordinates
        """
        return self.JarOfElement.ToMatrixWithCoordinates()
    
    def GiveElementsNumpyArray(self):
        """ this function is used to return the elements in the jar as a numpy array
    
        Returns:
            numpyarray: the elements in the jar as a numpy array
        """
        return self.JarOfElement.ToNumPyArrayWithIDs()
    
    def GiveElementsNumpyArrayWithCoordinates(self):
        """ this function is used to return the elements in the jar as a numpy array with coordinates
    
        Returns:
            numpyarray: the elements in the jar as a numpy array with coordinates
        """
        return self.JarOfElement.ToNumPyArrayWithCoordinates()
    
    
    