import matplotlib

from   matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
import pandas as pd



def quatplot(verts, values, ax=None, **kwargs):
    """this function is used to plot the contour
    Args:
        verts(list): the list of the vertices
        values(list): the list of the values
        ax(matplotlib.axes): the axes
        **kwargs: the other parameters
    Returns:
        pc(matplotlib.collections.PolyCollection): the PolyCollection
    """
    pc = matplotlib.collections.PolyCollection(verts, **kwargs)
    pc.set_array(values)
    ax.add_collection(pc)
    ax.autoscale()
    return pc


        
def show_countourError(Mesh,path,name,min_colorbar,max_colorbar):
    """this function is used to save the displacement of the mesh
    Args:
        Mesh(Mesh): the mesh
        path(str): the path to save the displacement
        name(str): the name of the displacement
    """
    verts_li = []
    li_node=[]
    li_srp=[]
    li_fem=[]
    li_ids=[]
    Error_li=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        verts_li.append([[element.n1.x,element.n1.y],[element.n2.x,element.n2.y],[element.n3.x,element.n3.y]])
        Error_li.append(element.Error)
        gaussNodeCoord=element.GaussianPoint_coordinate
        li_node.append(gaussNodeCoord)
        li_srp.append(element.srp_value)
        li_fem.append(element.fem_value)
        li_ids.append(element.id)
    x=[]
    y=[]
    
    
    li_node_df=pd.DataFrame(li_node,columns=['x','y'])
    li_node_df['id']=li_ids
    #add srp and fem value and ids to the dataframe
    li_node_df['srp']=li_srp
    li_node_df['fem']=li_fem
    #add error column to the dataframe
    li_node_df['Error']=Error_li
    #sort the dataframe by Error
    li_node_df=li_node_df.sort_values(by=['Error'])

    
    
    for node in Mesh.GiveJarOfNodes().GiveNodes():
        x.append(node.x)
        y.append(node.y)
    #showing the plot
    fig = Figure()
    fig.set_size_inches(10, 10)
    ax= fig.add_subplot(111)
    min_colorbar=min(Error_li)
    max_colorbar=max(Error_li)
    Error_li=np.array(Error_li)*100
    # colorbar=np.linspace(min_colorbar,max_colorbar,100)
    colorbar=np.linspace(0,100,100)


    #set the aspect ratio
    ax.set_aspect('equal')
    #remove the axis
    ax.axis('off')

    #plot the contour
    pc = quatplot(verts_li, Error_li, ax=ax,edgecolors='k', cmap='jet', linewidths=0.1)
    pc.set_clim(min(colorbar),max(colorbar))
    
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    #precentage of the error for each element with format %.1f 
    cbar = fig.colorbar(pc, cax=cax,ticks=[0,20,40,60,80,100],format='%.1f')
    cbar.set_ticklabels(['%0','%20','%40','%60','%80','%100'])
    
    # ax.plot(x,y, marker='o', linestyle='', markersize=2, color='k')
    print(f"info: saving {name}")
    
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")
    
    
    fig.savefig(f"{path}/plot/{name}.jpg",dpi=300)
    plt.close(fig)
    
