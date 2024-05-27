# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
from DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from DataStructure_Point_Node              import NodePoint       as Node
from DataStructure_Point_Gaussian          import GaussianPoint   as GaussianPoint

from DataStructure_jar_Element             import JarOfElement
from DataStructure_jar_Node                import JarOfNodes
from DataStructure_jar_GussianPoint        import JarOfGussianPoint

from DataStructure_Mesh                    import Mesh


from Reader_abaqusCSV   import abaqusCSV
from Reader_abaqusINP   import abaqusINP
from Reader_GmeshDAT    import GmeshDAT
from Reader_myselfCSV   import myselfCSV_Gradient 

class reader:
    """class to read the mesh and the data files
    """
    def __init__(self,mesh,relative_error_thereshold=0.001):
        """constructor of the class
        """
        self.mesh = mesh
        self.relative_error_thereshold=relative_error_thereshold
    def read(self,path):
        """function to read the mesh and the data files
        """
        
        self.path = path
        self.prefix_file=self.path.split(".")[-1]
        self.name_file=self.path.split("/")[-1].split(".")[0]
        
        if self.prefix_file == "inp":
            inp=abaqusINP(self.mesh, self.path)
            inp.readNode()
            inp.readElement(self.relative_error_thereshold)
            
        elif self.prefix_file == "csv":
            if self.name_file == "final_mat":
                csv=myselfCSV_Gradient(self.mesh,  self.path)
                csv.read()
            else:
                csv=abaqusCSV(self.mesh,  self.path)
                csv.readGaussianPoint()
                
        elif self.prefix_file == "dat":
            dat=GmeshDAT(self.mesh, self.path)
            dat.readNode()
            dat.readElement(self.relative_error_thereshold)
        else:
            print("Error: File type not supported")
