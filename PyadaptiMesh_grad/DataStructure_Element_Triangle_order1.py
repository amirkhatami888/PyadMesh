# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import math
import numpy as np
class Triangle_order1:
    """
    This class is used to create a triangle element of order 1
    Attributes:
        id: id of the element
        n1: node 1
        n2: node 2
        n3: node 3
        A: area of the triangle
        GaussianPoint_coordinate: coordinate of the Gaussian point
        GaussianPoints: list of Gaussian points
    """
    def __init__(self,id,n1,n2,n3):
        """
        The constructor for Triangle_order1 class.
        args:
            id(int): id of the element
            n1(Node): node 1
            n2(Node): node 2
            n3(Node): node 3          
            A(float): area of the triangle
            GaussianPoint_coordinate(list): coordinate of the Gaussian point
            GaussianPoints(list): list of Gaussian points
        """
        
        
        self.id=id

        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        
        self.A = 0.5*abs((n2.Give_x()-n1.Give_x())*(n3.Give_y()-n1.Give_y())-(n3.Give_x()-n1.Give_x())*(n2.Give_y()-n1.Give_y()))
        
        
        self.GaussianPoint_coordinate = [(n1.Give_x()+n2.Give_x()+n3.Give_x())/3,((n1.Give_y()+n2.Give_y()+n3.Give_y()))/3]
        #calculate element size of triangle element
        dx1=n1.Give_x()-n2.Give_x()
        dy1=n1.Give_y()-n2.Give_y()
        dx2=n1.Give_x()-n3.Give_x()
        dy2=n1.Give_y()-n3.Give_y()
        dx3=n2.Give_x()-n3.Give_x()
        dy3=n2.Give_y()-n3.Give_y()
        self.elementSize=math.sqrt((dx1**2+dy1**2+dx2**2+dy2**2+dx3**2+dy3**2)/3)
    

        self.GaussianPoints = []
        self.srp_value = None
        self.fem_value = None
        self.nodes=[n1,n2,n3]
        self._GSH = None
        
    @property
    def Error_pure(self):
        return abs(self.srp_value-self.fem_value)
    
    
    @property
    def Error(self):
        """this property is used to return the error of the element
        Returns:
            float: the error of the element
        """
        error_thereshold =0.001

        e=abs(self.fem_value-self.srp_value)/abs(self.srp_value)
        if abs(self.srp_value-self.fem_value) < error_thereshold:
            return 0

        return e

    def shape_function(self,xi,yi):
        """this property is used to return the shape function of the element
        Returns:
            list: the shape function of the element
        """
        N1 = (self.n2.y-self.n3.y)*xi+(self.n3.x-self.n2.x)*yi+self.n2.x*self.n3.y-self.n3.x*self.n2.y
        N2 = (self.n3.y-self.n1.y)*xi+(self.n1.x-self.n3.x)*yi+self.n3.x*self.n1.y-self.n1.x*self.n3.y
        N3 = (self.n1.y-self.n2.y)*xi+(self.n2.x-self.n1.x)*yi+self.n1.x*self.n2.y-self.n2.x*self.n1.y
        N = [N1/(2*self.A),N2/(2*self.A),N3/(2*self.A)]
        return N

    def shape_function_derivative(self):
        """this property is used to return the derivative of the shape function of the element
        Returns:
            list: the derivative of the shape function of the element
        """
        N1 = [self.n2.y-self.n3.y,self.n3.x-self.n2.x]
        N2 = [self.n3.y-self.n1.y,self.n1.x-self.n3.x]
        N3 = [self.n1.y-self.n2.y,self.n2.x-self.n1.x]
        N = [N1,N2,N3]
        return N

    def scaler_displacement(self,xi,yi):
        """this property is used to return the scaler displacement of the element
        Returns:
            float: the scaler displacement of the element
        """
        N = self.shape_function(xi,yi)
        U1 = N[0]*self.n1.U1+N[1]*self.n2.U1+N[2]*self.n3.U1
        U2 = N[0]*self.n1.U2+N[1]*self.n2.U2+N[2]*self.n3.U2
        return u

    def displacement_derivative(self,direction):
        """this property is used to return the derivative of the displacement of the element
        Returns:
            list: the derivative of the displacement of the element
        """
        N = self.shape_function_derivative()
        U1 = N[0][0]*self.n1.U1+N[1][0]*self.n2.U1+N[2][0]*self.n3.U1
        U2 = N[0][0]*self.n1.U2+N[1][0]*self.n2.U2+N[2][0]*self.n3.U2
        
        U=math.sqrt(U1**2+U2**2)
        return U
    

    
        
        
    def Give_GaussianPoint(self):
        """this function is used to return the Gaussian point of the element
        
        Returns:
            GaussianPoint: the Gaussian point of the element
        """
        return self.GaussianPoints
    
    def Give_n1(self):
        """this function is used to return the first node of the element
        Returns:
            n1: the first node of the element
        """
        return self.n1
    def Give_n2(self):
        """this function is used to return the second node of the element

        Returns:
            n2: the second node of the element
        """
        return self.n2
    
    def Give_n3(self):
        """this function is used to return the third node of the element

        Returns:
            n3: the third node of the element
        """  
        return self.n3
    
    def GiveID(self):
        """this function is used to return the id of the element
        Returns:
            id: the id of the element
        """
        return self.id
    
    def Give_Area(self):
        """this function is used to return the area of the element
        Returns:
            A: the area of the element
        """
        return self.A
    
    def ToMatrix_IDs(self):
        """this function is used to return the ids of the nodes of the element in a matrix form
        Returns:
           list: the ids of the nodes of the element in a matrix form
        """
        return [self.id ,self.n1.GiveID(), self.n2.GiveID(), self.n3.GiveID()]
    
    def ToMatrix_Coordinates(self):
        """this function is used to return the coordinates of the nodes of the element in a matrix form

        Returns:
            list: the coordinates of the nodes of the element in a matrix form
        """
        return [self.n1.Give_x(), self.n1.Give_y(), self.n2.Give_x(), self.n2.Give_y(), self.n3.Give_x(), self.n3.Give_y()]

    def Give_Coordinates(self):
        """this function is used to return the coordinates of the nodes of the element in a list form
        
        Returns:
            list: the coordinates of the nodes of the element in a list form
        """
        return [self.n1.Give_x(), self.n1.Give_y(), self.n2.Give_x(), self.n2.Give_y(), self.n3.Give_x(), self.n3.Give_y()]
    
    def Give_GaussianPoint_coordinate(self):
        """this function is used to return the coordinates of the Gaussian point of the element
    
        Returns:
            list: the coordinates of the Gaussian point of the element
        """
        return self.GaussianPoint_coordinate
    
    def is_inside(self, point):
        """
        Check if a point is inside the triangle.

        Args:
            point (node): The point to be checked.

        Returns:
            bool: True if the point is inside the triangle, False otherwise.
        """
        epsilon = 1e-12
        term1=(self.n2.x-self.n1.x)*(point.y-self.n1.y)-(self.n2.y-self.n1.y)*(point.x-self.n1.x)
        term2=(self.n3.x-self.n2.x)*(point.y-self.n2.y)-(self.n3.y-self.n2.y)*(point.x-self.n2.x)
        term3=(self.n1.x-self.n3.x)*(point.y-self.n3.y)-(self.n1.y-self.n3.y)*(point.x-self.n3.x)
        
        if( term1>epsilon and term2>epsilon and term3>epsilon) or (term1<-epsilon and term2<-epsilon and term3<-epsilon):
            return True
        else:
            return False
    
    def add_GaussianPoint(self,Gpoint):
        """this function is used to add a Gaussian point to the element object
    
        Args:
            Gpoint (GaussianPoint): the Gaussian point to be added
        """
        self.GaussianPoints.append(Gpoint)
        
    def  Give_GaussianPoints(self):
        """this function is used to return the Gaussian points of the element

        Returns:
            list: the Gaussian points of the element
        """
        return self.GaussianPoints
 