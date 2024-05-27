# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
import math

class JarOfElement:
    """this class is used to store all the elements in a list

    Attributes:
        elements: a list of elements
        name: the name of the jar
    """
    def __init__(self):
        """the constructor for JarOfElement class
        
        Attributes:
            elements: a list of elements
        """
        self.elements = []
    def addElement(self, element):
        """this function is used to add an element to the jar
        args:
            element(Element): the element to be added
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
        """this function is used to add multiple elements to the jar
        args:
            *args(Element): the elements to be added
        """
        for i in args:
            self.addElement(i)
      
    def GiveElements(self):
        """this function is used to return the elements in the jar
        Returns:
            list: the elements in the jar
        """
        return self.elements
    
    def GiveElementWithID(self, id):
        """this function is used to return the element with the given ID
        Args:
            id(int): the ID of the element
        Returns:
            Element: the element with the given ID
        """
        try:
            if (self.elements[int(id-1)].id == id):
                return self.elements[int(id)-1]
            else:
                raise "Error: Element with ID not found"
        except:
            for i in self.elements:
                if i.GiveID() == id:
                    return i
            print ("Error: Element with ID not found")
            raise "Error: Element with ID not found"
    
    def GiveElementWithNodes(self, n1, n2, n3):
        """this function is used to return the element with the given nodes
        Args:
            n1(Node): the first node of the element
            n2(Node): the second node of the element
            n3(Node): the third node of the element
        Returns:    
            Element: the element with the given nodes
        """
        for i in self.elements:
            if i.Give_n1() == n1 and i.Give_n2() == n2 and i.Give_n3() == n3:
                return i
            else:
                pass
        print ("Error: Element with nodes not found")
        raise "Error: Element with nodes not found"
    
    def GiveElementWithIndex(self, index):
        """this function is used to return the element with the given index
        Args:
            index(int): the index of the element
        Returns:    
            Element: the element with the given index
        """
        return self.elements[index]
    
    def GiveSize(self):
        """this function is used to return the size of the jar
        Returns:    
            int: the size of the jar
        """
        return len(self.elements)
    
    def ToMatrixWithIDs(self):
        """this function is used to return the elements in the jar in a matrix form
        Returns:    
            list: the elements in the jar in a matrix form
        """
        matrix = []
        for i in self.elements:
            matrix.append([i.GiveID(), i.Give_n1().GiveID(), i.Give_n2().GiveID(), i.Give_n3().GiveID()])
        return matrix
    
    def ToMatrixWithCoordinates(self):
        """this function is used to return the elements in the jar in a matrix form with coordinates
        Returns:    
            list: the elements in the jar in a matrix form with coordinates
        """
        matrix = []
        for i in self.elements:
            matrix.append([i.GiveID(), i.Give_n1().Give_x(), i.Give_n1().Give_y(), i.Give_n2().Give_x(), i.Give_n2().Give_y(), i.Give_n3().Give_x(), i.Give_n3().Give_y()])
        return matrix
    
    def ToNumPyArrayWithIDs(self):
        """this function is used to return the elements in the jar in a numpy array form
        Returns:    
            numpy array: the elements in the jar in a numpy array form
        """
        return np.array(self.ToMatrixWithIDs())
    
    def ToNumPyArrayWithCoordinates(self):
        """this function is used to return the elements in the jar in a numpy array form with coordinates
        Returns:    
            numpy array: the elements in the jar in a numpy array form with coordinates
        """
        return np.array(self.ToMatrixWithCoordinates())
    
    