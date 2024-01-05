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
    for point in Mesh.GiveJarOfNodes().nodes:
        id=point.id
        x=point.x
        y=point.y
        u1=point.U1
        u2=point.U2
        li.append([float(id),float(x),float(y),float(u1),float(u2)])
    

    final_mat=np.array(li)
    np.savetxt(os.path.join(path, 'final_mat.csv'),final_mat,delimiter=',')

    file.close()
    return os.path.join(path, 'final_mat.csv')