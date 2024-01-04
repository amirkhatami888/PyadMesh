import matplotlib

from   matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import os


from plot_tecplot_pltWriter import write_plt_tecplot


        
def save_countourDisplacement(Mesh,path,name,name_plot):
    """this function is used to save the displacement of the mesh
    Args:
        Mesh(Mesh): the mesh
        path(str): the path to save the displacement
        name(str): the name of the displacement
    """
    U1_lis=[]
    U2_lis=[]
    X_lis=[]
    Y_lis=[]
    for node in Mesh.GiveJarOfNodes().nodes:
        U1_lis.append(node.U1)
        U2_lis.append(node.U2)
        X_lis.append(node.x)
        Y_lis.append(node.y)
        
    element_connectivity=[]
    for element in Mesh.GiveJarOfElement().elements:
        element_connectivity.append([element.n1.id-1,element.n2.id-1,element.n3.id-1])
    triang = mtri.Triangulation(X_lis, Y_lis, element_connectivity) 
    fig = Figure()
    fig.set_size_inches(10, 10)
    ax= fig.add_subplot(111)
    ax.set_aspect('equal')
    fig.colorbar(ax.tricontourf(X_lis, Y_lis, element_connectivity, U1_lis, cmap='jet'))
    ax.tricontourf(X_lis, Y_lis, element_connectivity, U1_lis, cmap='jet')
    ax.triplot(triang, 'ko-', lw=1,ms=1,c='black')
    #plot mesh and node



    
    ax.set_title(str(name_plot))
    print(f"info: saving {name}")
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")
    fig.savefig(f"{path}/plot/{name}.jpg",dpi=300) 
     

   
   
   
   
   
   