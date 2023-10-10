# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import os
import math
from DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from DataStructure_Point_Node import NodePoint as Node
from DataStructure_Point_Gaussian import GaussianPoint as GaussianPoint


class abaqusCSV:
    """class to read the csv file from abaqus
    """ 
    def __init__(self,mesh ,path):
        """constructor of the class

        Args:
            path (string): the path of the csv file
            mesh (instance of mesh class): the mesh
        """
        self.path     = path
        self.mesh     = mesh
    def readGaussianPoint(self):
        """function to read the csv file from abaqus
        """
        reader = open(self.path, 'r')
        line = reader.readline().split(',')
        line2=[]
        for i in line:
            line2.append(i.strip(' '))
        line=line2
        value_index_gradient=len(line)-1
        elemenet_label_index=line.index('Element Label')
        x_index=line.index('X')
        y_index=line.index('Y')
        for i in reader:
            if not i[:3]=="ODB":
                x=float(i.split(',')[x_index])
                y=float(i.split(',')[y_index])
                
                gradient=float(i.split(',')[value_index_gradient])
                self.mesh.JarOfGussianPoint.addGussianPoint(GaussianPoint(x,y,gradient))

        reader.close()
    
    def connectGaussianPointTOElement(self):
        """function to connect the gaussian points to the elements
        """
        for i in self.mesh.JarOfGussianPoint.GiveGussianPoints():
            for j in self.mesh.JarOfElement.GiveElements():
                if j.is_inside(i):
                    j.add_GaussianPoint(i)
                    break
                  