# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math

class JarOfGussianPoint:
    """this class is used to store all the GussianPoints in a list
    attributes:
        GussianPoints: a list of GussianPoints
        name: the name of the jar
    """
    def __init__(self):
        """the constructor for JarOfGussianPoint class
        """
        self.GussianPoints = []
        self.name = None
    
    def addGussianPoint(self, GussianPoint):
        """this function is used to add a GussianPoint to the jar
        args:
            GussianPoint(GussianPoint): the GussianPoint to be added
        """
        self.GussianPoints.append(GussianPoint)
        
    def addGussianPoints(self, *args):
        """this function is used to add multiple GussianPoints to the jar
        args:
            *args(GussianPoint): the GussianPoints to be added
        """
        for i in args:
            self.addGussianPoint(i)
    
    def GiveGussianPoints(self):
        """this function is used to return the GussianPoints in the jar

        Returns:
            list: the GussianPoints in the jar
        """ 
        return self.GussianPoints
    
    def GiveGussianPointWithID(self, id):
        """this function is used to return the GussianPoint with the given ID
        Args:
            id(int): the ID of the GussianPoint
        Returns:    
            GussianPoint: the GussianPoint with the given ID
        """
        for i in self.GussianPoints:
            if i.GiveID() == id:
                return i
            else:
                pass
        print ("Error: GussianPoint with ID not found")
        raise "Error: GussianPoint with ID not found"
    
    
    def GiveGussianPointWithIndex(self, index):
        """this function is used to return the GussianPoint with the given index
        Args:
            index(int): the index of the GussianPoint
        Returns:    
            GussianPoint: the GussianPoint with the given index
        """
        return self.GussianPoints[index]
    
    def GiveSize(self):
        """this function is used to return the size of the jar
        Returns:
            int: the size of the jar
        """
        return len(self.GussianPoints)
    
    def  ToMatrix(self):
        """this function is used to return the GussianPoints in the jar as a matrix
        Returns:
            list: the GussianPoints in the jar as a matrix
        """
        matrix = []
        for i in self.GussianPoints:
            matrix.append(i.ToMatrix())
        return matrix
  
    def ToMatrixWithCoordinates(self):
        """this function is used to return the GussianPoints in the jar as a matrix with coordinates
        Returns:
            list: the GussianPoints in the jar as a matrix with coordinates
        """
        matrix = []
        for i in self.GussianPoints:
            matrix.append(i.ToMatrixWithCoordinates())
        return matrix
    
    def TONumPyArray(self):
        """this function is used to return the GussianPoints in the jar as a numpy array
        Returns:
            numpy array: the GussianPoints in the jar as a numpy array
        """
        return np.array(self.ToMatrix())
    
    def TONumPyArrayWithID(self):
        """this function is used to return the GussianPoints in the jar as a numpy array with ID
        Returns:
            numpy array: the GussianPoints in the jar as a numpy array with ID
        """
        return np.array(self.ToMatrixWithID())
    
    def TONumPyArrayWithCoordinates(self):
        """this function is used to return the GussianPoints in the jar as a numpy array with coordinates
        Returns:
            numpy array: the GussianPoints in the jar as a numpy array with coordinates
        """
        return np.array(self.ToMatrixWithCoordinates())