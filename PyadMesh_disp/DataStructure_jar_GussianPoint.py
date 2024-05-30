# author: amirhossein khatami
# mail: amirkhatami@gmail.com

#importing libraries
import numpy as np
import math

class JarOfGussianPoint:
    """This class is used to store all the GussianPoints in a list.

    Attributes:
        GussianPoints (list): A list of GussianPoints.
        name (str): The name of the jar.
    """
    def __init__(self):
        """The constructor for JarOfGussianPoint class."""

        self.GussianPoints = []
        self.name = None
    
    def addGussianPoint(self, GussianPoint):
        """This function is used to add a GussianPoint to the jar.

        Args:
            GussianPoint (GussianPoint): The GussianPoint to be added.
        """
        self.GussianPoints.append(GussianPoint)
        
    def addGussianPoints(self, *args):
        """This function is used to add multiple GussianPoints to the jar.

        Args:
            *args (GussianPoint): The GussianPoints to be added.
        """
        for i in args:
            self.addGussianPoint(i)
    
    def GiveGussianPoints(self):
        """This function is used to return the GussianPoints in the jar.

        Returns:
            list: The GussianPoints in the jar.
        """ 
        return self.GussianPoints
    
    def GiveGussianPointWithID(self, id):
        """This function is used to return the GussianPoint with the given ID.

        Args:
            id (int): The ID of the GussianPoint.

        Returns:
            GussianPoint: The GussianPoint with the given ID.
        """
        for i in self.GussianPoints:
            if i.GiveID() == id:
                return i
            else:
                pass
        print ("Error: GussianPoint with ID not found")
        raise "Error: GussianPoint with ID not found"
    
    
    def GiveGussianPointWithIndex(self, index):
        """This function is used to return the GussianPoint with the given index.

        Args:
            index (int): The index of the GussianPoint.

        Returns:
            GussianPoint: The GussianPoint with the given index.
        """
        return self.GussianPoints[index]
    
    def GiveSize(self):
        """This function is used to return the size of the jar.

        Returns:
            int: The size of the jar.
        """
        return len(self.GussianPoints)
    
    def  ToMatrix(self):
        """This function is used to return the GussianPoints in the jar as a matrix.

        Returns:
            list: The GussianPoints in the jar as a matrix.
        """
        matrix = []
        for i in self.GussianPoints:
            matrix.append(i.ToMatrix())
        return matrix
  
    def ToMatrixWithCoordinates(self):
        """This function is used to return the GussianPoints in the jar as a matrix with coordinates.

        Returns:
            list: The GussianPoints in the jar as a matrix with coordinates.
        """
        matrix = []
        for i in self.GussianPoints:
            matrix.append(i.ToMatrixWithCoordinates())
        return matrix
    
    def TONumPyArray(self):
        """This function is used to return the GussianPoints in the jar as a numpy array.

        Returns:
            numpy array: The GussianPoints in the jar as a numpy array.
        """
        return np.array(self.ToMatrix())
    
    def TONumPyArrayWithID(self):
        """This function is used to return the GussianPoints in the jar as a numpy array with ID.

        Returns:
            numpy array: The GussianPoints in the jar as a numpy array with ID.
        """
        return np.array(self.ToMatrixWithID())
    
    def TONumPyArrayWithCoordinates(self):
        """This function is used to return the GussianPoints in the jar as a numpy array with coordinates.

        Returns:
            numpy array: The GussianPoints in the jar as a numpy array with coordinates.
        """
        return np.array(self.ToMatrixWithCoordinates())