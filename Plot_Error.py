import matplotlib

from   matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import os


def quatplot(verts, values, ax=None, **kwargs):
    """Plot a 2D triangulation."""
    pc = matplotlib.collections.PolyCollection(verts, **kwargs)
    pc.set_array(values)
    ax.add_collection(pc)
    ax.autoscale()
    return pc


        
def show_countourError(Mesh,path,name,name_plot,min_colorbar,max_colorbar):
    """this function plot the error of mesh
    Args:
        Mesh (class): mesh class
        path (str): save path
        name (str): file name
        name_plot (str): plot name
        min_colorbar (float): minimum value of colorbar
        max_colorbar (float): maximum value of colorbar
    """
    verts_li = []
    Error_li=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        verts_li.append([[element.n1.x,element.n1.y],[element.n2.x,element.n2.y],[element.n3.x,element.n3.y]])
        Error_li.append(element.Error)
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
    # colorbar=np.linspace(min_colorbar,max_colorbar,100)
    colorbar=np.linspace(0,1,100)


    #set the aspect ratio
    ax.set_aspect('equal')
    #remove the axis
    ax.axis('off')

    #plot the contour
    pc = quatplot(verts_li, Error_li, ax=ax,edgecolors='k', cmap='jet', linewidths=0.5)
    pc.set_clim(min(colorbar),max(colorbar))
    fig.colorbar(pc, ax=ax)
    # ax.plot(x,y, marker='o', linestyle='', markersize=2, color='k')
    ax.set_title(str(name_plot))
    print(f"info: saving {name}")
    
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")
    
    # fig.savefig(f"{path}/plot/{name}.pdf",dpi=300)
    fig.savefig(f"{path}/plot/{name}.png",dpi=300)
    plt.close(fig)



