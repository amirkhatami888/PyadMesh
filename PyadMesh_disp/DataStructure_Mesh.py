# author: amirhossein khatami

# mail: amirkhatami@gmail.com
# importing libraries
import math
import numpy as np

class Mesh:
    """This class is used to store all mesh data.
    
    Attributes:
        name (str): The name of the mesh.
        JarOfNodes (JarOfNodes): A jar of nodes.
        JarOfGussianPoint (JarOfGussianPoint): A jar of Gaussian points.
        JarOfElement (JarOfElement): A jar of elements.
    """ 
    def __init__(self,JarOfNodes=None,JarOfGussianPoint=None,JarOfElement=None):
        """The constructor for Mesh class."""
        self.name = None
        self.JarOfNodes = JarOfNodes
        self.JarOfGussianPoint = JarOfGussianPoint
        self.JarOfElement = JarOfElement

    def GiveJarOfNodes(self):
        """This function is used to return the jar of nodes.

        Returns:
            list: The jar of nodes.
        """
        return self.JarOfNodes
    
    def GiveJarOfGussianPoint(self):
        """This function is used to return the jar of Gaussian points.

        Returns:
            list: The jar of Gaussian points.
        """
        return self.JarOfGussianPoint
    
    def GiveJarOfElement(self):
        """This function is used to return the jar of elements.

        Returns:
            list: The jar of elements.
        """
        return self.JarOfElement
    
    def GiveNodes(self):
        """This function is used to return the nodes in the jar.

        Returns:
            list: The nodes in the jar.
        """
        return self.JarOfNodes.GiveNodes()
    
    def GiveGussianPoints(self):
        """This function is used to return the Gaussian points in the jar.

        Returns:
            list: The Gaussian points in the jar.
        """
        return self.JarOfGussianPoint.GiveGussianPoints()   
    
    def GiveElements(self):
        """This function is used to return the elements in the jar.

        Returns:
            list: The elements in the jar.
        """
        return self.JarOfElement.GiveElements() 
    
    def GiveNodeMatrix(self):
        """This function is used to return the nodes in the jar as a matrix.

        Returns:
            list: The nodes in the jar as a matrix.
        """
        return self.JarOfNodes.ToMatrix()
    
    def GiveNodeMatrixWithID(self):
        """This function is used to return the nodes in the jar as a matrix with ID.

        Returns:
            list: The nodes in the jar as a matrix with ID.
        """
        return self.JarOfNodes.ToMatrixWithID()
    
    def GiveNodeMatrixwithDisplacement(self):
        """This function is used to return the nodes in the jar as a matrix with displacement.

        Returns:
            list: The nodes in the jar as a matrix with displacement.
        """
        return self.JarOfNodes.ToMatrixWithDisplacement()
    
    def GiveNodeNumpyArray(self):
        """This function is used to return the nodes in the jar as a numpy array.

        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array.
        """
        return self.JarOfNodes.ToNumPyArray()
    
    def GiveNodeNumpyArrayWithID(self):
        """This function is used to return the nodes in the jar as a numpy array with ID.

        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array with ID.
        """
        return self.JarOfNodes.ToNumPyArrayWithID()
    
    def GiveNodeCyWithDisplacement(self):
        """This function is used to return the nodes in the jar as a numpy array with displacement.

        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array with displacement.
        """
        return self.JarOfNodes.ToMatrixWithDisplacement()
    
    def GiveNodeNumpyArrayWithDisplacementAndID(self):
        """This function is used to return the nodes in the jar as a numpy array with displacement and ID.

        Returns:
            numpy.ndarray: The nodes in the jar as a numpy array with displacement and ID.
        """
        return self.JarOfNodes.ToNumPyArrayWithIDAndDisplacement()
    
    def GiveElementsMatrix(self):
        """This function is used to return the elements in the jar as a matrix.

        Returns:
            list: The elements in the jar as a matrix.
        """
        return self.JarOfElement.ToMatrixWithIDs()
    
    def GiveElementsMatrixWithCoordinates(self):
        """This function is used to return the elements in the jar as a matrix with coordinates.

        Returns:
            list: The elements in the jar as a matrix with coordinates.
        """
        return self.JarOfElement.ToMatrixWithCoordinates()
    
    def GiveElementsNumpyArray(self):
        """This function is used to return the elements in the jar as a numpy array.

        Returns:
            numpy.ndarray: The elements in the jar as a numpy array.
        """
        return self.JarOfElement.ToNumPyArrayWithIDs()
    
    def GiveElementsNumpyArrayWithCoordinates(self):
        """This function is used to return the elements in the jar as a numpy array with coordinates.

        Returns:
            numpy.ndarray: The elements in the jar as a numpy array with coordinates.
        """
        return self.JarOfElement.ToNumPyArrayWithCoordinates()
    
    
    