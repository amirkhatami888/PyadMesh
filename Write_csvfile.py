# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
import os
def Write_csvfile(Mesh,path):
    """write the csv file

    Args:
        Mesh (instance of mesh class): the mesh

    Returns:
        str: name of the csv file
    """
    li=[]
    file=open(fr"{path}/final_mat.csv","w")
    for element in Mesh.GiveJarOfElement().GiveElements():
        id=element.id
        pointCoord=element.GaussianPoint_coordinate
        value=element.srp_value
        li.append([float(id),float(pointCoord[0]),float(pointCoord[1]),float(value)])
    

    final_mat=np.array(li)
    np.savetxt(os.path.join(path, 'final_mat.csv'),final_mat,delimiter=',')

    file.close()
    return os.path.join(path, 'final_mat.csv')