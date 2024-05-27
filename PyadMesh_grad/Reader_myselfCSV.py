# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import os
import math
from DataStructure_Point_Node import NodePoint as Node
from DataStructure_Point_Gaussian import GaussianPoint as GaussianPoint

class myselfCSV_Gradient:
    """class to read the csv file 
    """
    def __init__(self,mesh ,filename="final_mat.csv",path=os.getcwd()):
        """constructor of the class

        Args:
            mesh (instance of mesh class): the mesh
            filename (str, optional): _description_. Defaults to "final_mat.csv".
            path (str, optional): _description_. Defaults to os.getcwd().
        """
        self.filename = filename
        self.path     = path
        self.mesh     = mesh
        
    def read(self):
        """function to read the csv file 
        """
        with open(self.filename, 'r') as f:
            reader = open(os.path.join(self.path, self.filename), 'r')
            for row in reader:
                row=row.strip('\n')
                row=row.split(',')
                X_temp   = row[1]
                Y_temp   = row[2]
                val_temp = row[3]
                self.mesh.JarOfGussianPoint.addGussianPoint( GaussianPoint( X_temp , Y_temp , val_temp ))
                del( X_temp , Y_temp , val_temp)
            reader.close()


class myselfCSV_displacement:
    """class to read the csv file 
    """
    
    def __init__(self,mesh ,filename="final_mat.csv",path=os.getcwd()):
        """constructor of the class

        Args:
            mesh (instance of mesh class): the mesh
            filename (str, optional): _description_. Defaults to "final_mat.csv".
            path (str, optional): _description_. Defaults to os.getcwd().
        """
        self.filename = filename
        self.path     = path
        self.mesh     = mesh
    
    def read(self):
        """function to read the csv file
        """
        with open(self.filename, 'r') as f:
            reader = open(os.path.join(self.path, self.filename), 'r')
            for row in reader:
                id_temp  = row[0]
                X_temp   = row[1]
                Y_temp   = row[2]
                val_temp = row[3]
                
                epsilon=0.001
                for i in self.mesh.JarOfNodes:
                    if math.abs(i.Give_x()-X_temp)<epsilon and math.abs(i.Give_y()-Y_temp)<epsilon:
                        i.set_displacement(val_temp)
                        break
                del(id_temp , X_temp , Y_temp , val_temp)
    
            reader.close()