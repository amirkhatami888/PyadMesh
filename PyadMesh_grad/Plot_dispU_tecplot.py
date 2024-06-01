# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import os
from plot_tecplot_pltWriter import write_plt_tecplot


        
def save_countourDisplacement(Mesh,path,name,name_plot):
    """this function is used to save the contour of the displacement
    Args:
        Mesh (Mesh): the mesh
        path (str): the path
        name (str): the name
        name_plot (str): the name of the plot
    """
    U1_lis=[]
    U2_lis=[]
    U_lis=[]
    X_lis=[]
    Y_lis=[]
    for node in Mesh.GiveJarOfNodes().nodes:
        U1_lis.append(node.U1)
        U2_lis.append(node.U2)
        temp=np.sqrt(node.U1**2+node.U2**2)
        U_lis.append(temp)
        X_lis.append(node.x)
        Y_lis.append(node.y)
        
    index_li=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        index_li.append([element.n1.id,element.n2.id,element.n3.id])
    

    write_plt_tecplot(f"{path}/plot/U1_step{name}.plt"\
                      ,name_plot,X_lis,Y_lis,U1_lis,index_li)
    write_plt_tecplot(f"{path}/plot/U2_step{name}.plt"\
                      ,name_plot,X_lis,Y_lis,U2_lis,index_li)
    write_plt_tecplot(f"{path}/plot/U_step{name}.plt"\
                        ,name_plot,X_lis,Y_lis,U_lis,index_li)
        
        
   
   
   
   
   
   