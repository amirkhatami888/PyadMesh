# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import os
import math
from DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from DataStructure_Point_Node import NodePoint as Node


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
    def read(self):
        """function to read the csv file from abaqus
        """
        reader = open(self.path, 'r')
        line = reader.readline().split(',')
        line2=[]
        for i in line:
            line2.append(i.strip(' ').lower())
        line=line2
        elemenet_label_index=line.index('node label')
        x_index=line.index('x')
        y_index=line.index('y')
        value_index_U2=len(line)-1
        value_index_U1=len(line)-2
        for i in reader:
            if not i[:3]=="odb":
                id=int(i.split(',')[elemenet_label_index])
                x=float(i.split(',')[x_index])
                y=float(i.split(',')[y_index])
                U1=float(i.split(',')[value_index_U1])
                U2=float(i.split(',')[value_index_U2])
                NODE=self.mesh.JarOfNodes.GiveNodeWithID(id) 
                if NODE.x-x<1e-3 and NODE.y-y<1e-3:
                    NODE.U1=U1
                    NODE.U2=U2
                else:
                    for nodeMesh in  self.mesh .JarOfNodes.nodes :
                        if nodeMesh.x-x<1e-3 and nodeMesh.y-y<1e-3:
                            nodeMesh.U1=U1
                            nodeMesh.U2=U2
                            break
               
        reader.close()
    
