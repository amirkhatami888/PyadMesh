import matplotlib

from   matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
import pandas as pd


def quatplot(verts, values, ax=None, **kwargs):
    pc = matplotlib.collections.PolyCollection(verts, **kwargs)
    pc.set_array(values)
    ax.add_collection(pc)
    ax.autoscale()
    return pc


        
def show_countourPureError(Mesh,path,name,min_colorbar,max_colorbar):
    verts_li = []
    li_node=[]
    li_srp=[]
    li_fem=[]
    li_ids=[]
    Error_li=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        verts_li.append([[element.n1.x,element.n1.y],[element.n2.x,element.n2.y],[element.n3.x,element.n3.y]])
        Error_li.append(element.Error_pure)
        gaussNodeCoord=element.GaussianPoint_coordinate
        li_node.append(gaussNodeCoord)
        li_srp.append(element.srp_value)
        li_fem.append(element.fem_value)
        li_ids.append(element.id)
 
    x=[]
    y=[]
    

    
    for node in Mesh.GiveJarOfNodes().GiveNodes():
        x.append(node.x)
        y.append(node.y)
    #showing the plot
    fig = Figure()
    fig.set_size_inches(10, 10)
    ax= fig.add_subplot(111)
    min_colorbar=min(Error_li)
    max_colorbar=max(Error_li)
 
    colorbar=np.linspace(min_colorbar,max_colorbar,100)


    #set the aspect ratio
    ax.set_aspect('equal')
    #remove the axis
    ax.axis('off')

    #plot the contour
    pc = quatplot(verts_li, Error_li, ax=ax,edgecolors='k', cmap='jet', linewidths=0.5)
    pc.set_clim(min(colorbar),max(colorbar))
    
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    #precentage of the error for each element with format %.1f 
    cbar = fig.colorbar(pc, cax=cax)
    

    print(f"info: saving {name}")
    
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")
    fig.savefig(f"{path}/plot/{name}.jpg",dpi=300)
    plt.close(fig)
    


