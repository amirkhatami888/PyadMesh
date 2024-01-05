# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import os
import math
from DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from DataStructure_Point_Node import NodePoint as Node


class abaqusINP:
    """class to read the inp file from abaqus
    """
    def __init__(self,mesh,path):
        """constructor of the class

        Args:
            path (string): the path of the inp file
            mesh (instance of mesh class): the mesh
        """
        self.path     = path
        self.mesh     = mesh
        
        
    def readNode(self):
        """function to read the inp file from abaqus
        """
        reader = open(self.path, 'r')
        lines = reader.readlines()
        
        for i in lines:
            if i[0:5].lower() == "*node":
                node_index_start=lines.index(i)
                break

        for i in lines[node_index_start+1:]:
            if i[0:1] == "*":
                break
            if i =='  \n':
                continue
            
            id=int (i.split(',')[0])
            
            x =float(i.split(',')[1])
            y =float(i.split(',')[2])
            
            self.mesh.JarOfNodes.addNode( Node(id,x,y))
            del(id,x,y)
            
        reader.close()
        
    def readElement(self):
        """function to read the inp file from abaqus
        """
        
        reader = open(self.path, 'r')
        
        
        lines = reader.readlines()
                
        
        for i in lines:
            if i[0:8].lower() == "*element":
                element_index_start=lines.index(i)            
                break
  
        for i in lines[element_index_start+1:]:
            if i[0:1] == "*":
                break
            if i =='  \n':
                continue
            id=int(i.split(',')[0])
            
            n1_id=int(i.split(',')[1])
            n1=self.mesh.JarOfNodes.GiveNodeWithID(n1_id)
            
            n2_id=int(i.split(',')[2])
            n2=self.mesh.JarOfNodes.GiveNodeWithID(n2_id)
            
            n3_id=int(i.split(',')[3])
            n3=self.mesh.JarOfNodes.GiveNodeWithID(n3_id)
            
            self.mesh.JarOfElement.addElement( Element(id,n1,n2,n3))
            del(id,n1,n2,n3,n1_id,n2_id,n3_id)
            
        reader.close()
    