# author: amirhossein khatami
# mail: amirkhatami@gmail.com
import os
import math
from DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from DataStructure_Point_Node import NodePoint as Node
from DataStructure_Point_Gaussian import GaussianPoint as GaussianPoint


class GmeshDAT:
    """this class is used to read the dat file from gmesh
    """
    
    def __init__(self,mesh,path):
        self.path     = path
        self.mesh     = mesh
    
    def readNode(self):

        with open(self.path, 'r') as f:
            reader = open(self.path, 'r')
            for i in reader:
                if i[0:5] == "node ":
                    id=int(i.split()[1])
                    x=float(i.split()[2])
                    y=float(i.split()[3])
                    self.mesh.JarOfNodes.addNode( Node(id,x,y))
                    del(id,x,y)
            reader.close()
    def readElement(self):
            """function to read the dat file from gmesh
            """
            reader = open(self.path  , 'r')
            for i in reader:
                if i[0:8] == "element ":
                    id=int(i.split()[1])
                    
                    n1_id=int(i.split()[3])
                    n1=self.mesh.JarOfNodes.GiveNodeWithID(n1_id)
                
                    n2_id=int(i.split()[4])
                    n2=self.mesh.JarOfNodes.GiveNodeWithID(n2_id)
                    
                    n3_id=int(i.split()[5])
                    n3=self.mesh.JarOfNodes.GiveNodeWithID(n3_id)
                    
                    
                    self.mesh.JarOfElement.addElement( Element(id,n1,n2,n3))
                    del(id,n1,n2,n3,n1_id,n2_id,n3_id)
            reader.close()
            
            
