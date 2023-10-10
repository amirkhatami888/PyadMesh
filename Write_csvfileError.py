# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
import os
def Write_csvfileError(Mesh,path):
    """write the csv file

    Args:
        Mesh (instance of mesh class): the mesh

    Returns:
        str: name of the csv file
    """
    li=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        temp=element.ToMatrix_Coordinates()
        value=element.Error
        temp.append(value)
        li.append(temp)
    

    final_mat=np.array(li)
    np.savetxt(os.path.join(path, 'ERROR_mat.csv'),final_mat,delimiter=',')


    return "ERROR_mat.csv"