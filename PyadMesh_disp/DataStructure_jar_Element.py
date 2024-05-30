
# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import numpy as np
import math

class JarOfElement:
    """This class is used to store all the elements in a list.

    Attributes:
        elements (list): A list of elements.
        name (str): The name of the jar.
    """
    def __init__(self):
        """The constructor for JarOfElement class."""
        self.elements = []
        
    def addElement(self, element):
        """This function is used to add an element to the jar.

        Args:
            element (Element): The element to be added.
        """
        for i in self.elements:
            if i.Give_n1() == element.Give_n1() and i.Give_n2() == element.Give_n2() and i.Give_n3() == element.Give_n3():
                
                if i.GiveID() == element.GiveID():
                    print("Error: Element with same nodes and ID")
                    raise "Error: Element with same nodes and ID"
                    
                else:
                    print ("Error: Element with same nodes but different ID")
                    raise "Error: Element with same nodes but different ID"
        self.elements.append(element)
        
    
    def addElements(self, *args):
        """This function is used to add multiple elements to the jar.

        Args:
            *args (Element): The elements to be added.
        """
        for i in args:
            self.addElement(i)
      
    def GiveElements(self):
        """This function is used to return the elements in the jar.

        Returns:
            list: The elements in the jar.
        """
        return self.elements
    
    def GiveElementWithID(self, id):
        """This function is used to return the element with the given ID.

        Args:
            id (int): The ID of the element.

        Returns:
            Element: The element with the given ID.
        """
        for i in self.elements:
            if i.GiveID() == id:
                return i
            else:
                pass
        print ("Error: Element with ID not found")
        raise "Error: Element with ID not found"
    
    def GiveElementWithNodes(self, n1, n2, n3):
        """This function is used to return the element with the given nodes.

        Args:
            n1 (Node): The first node of the element.
            n2 (Node): The second node of the element.
            n3 (Node): The third node of the element.

        Returns:
            Element: The element with the given nodes.
        """
        for i in self.elements:
            if i.Give_n1() == n1 and i.Give_n2() == n2 and i.Give_n3() == n3:
                return i
            else:
                pass
        print ("Error: Element with nodes not found")
        raise "Error: Element with nodes not found"
    
    def GiveElementWithIndex(self, index):
        """This function is used to return the element with the given index.

        Args:
            index (int): The index of the element.

        Returns:
            Element: The element with the given index.
        """
        return self.elements[index]
    
    def GiveSize(self):
        """This function is used to return the size of the jar.

        Returns:
            int: The size of the jar.
        """
        return len(self.elements)
    
    def ToMatrixWithIDs(self):
        """This function is used to return the elements in the jar in a matrix form.

        Returns:
            list: The elements in the jar in a matrix form.
        """
        matrix = []
        for i in self.elements:
            matrix.append([i.GiveID(), i.Give_n1().GiveID(), i.Give_n2().GiveID(), i.Give_n3().GiveID()])
        return matrix
    
    def ToMatrixWithCoordinates(self):
        """This function is used to return the elements in the jar in a matrix form with coordinates.

        Returns:
            list: The elements in the jar in a matrix form with coordinates.
        """
        matrix = []
        for i in self.elements:
            matrix.append([i.GiveID(), i.Give_n1().Give_x(), i.Give_n1().Give_y(), i.Give_n2().Give_x(), i.Give_n2().Give_y(), i.Give_n3().Give_x(), i.Give_n3().Give_y()])
        return matrix
    
    def ToNumPyArrayWithIDs(self):
        """This function is used to return the elements in the jar in a numpy array form.

        Returns:
            numpy array: The elements in the jar in a numpy array form.
        """
        return np.array(self.ToMatrixWithIDs())
    
    def ToNumPyArrayWithCoordinates(self):
        """This function is used to return the elements in the jar in a numpy array form with coordinates.

        Returns:
            numpy array: The elements in the jar in a numpy array form with coordinates.
        """
        return np.array(self.ToMatrixWithCoordinates())
    
    