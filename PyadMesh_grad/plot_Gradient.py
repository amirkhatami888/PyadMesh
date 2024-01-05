# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import pandas as pd
import warnings
import sys
import copy

import matplotlib
from   matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from plot_tecplot_pltWriter import write_plt_tecplot
import numpy as np
import os
from Func_parallel_calPointSRP import one_point

def quatplot(verts, values, ax=None, **kwargs):
    """Plot a 2D triangulation as a color-coded quadrilateral mesh.
    Arguments:
        verts: a list of the vertices of each quadrilateral
        values: the value of each quadrilateral
        ax: the matplotlib axes to plot on
        kwargs: keyword arguments passed on to matplotlib.collections.PolyCollection
    Returns:
        pc: the matplotlib PolyCollection instance plotted on ax
    """
    pc = matplotlib.collections.PolyCollection(verts, **kwargs)
    pc.set_array(values)
    ax.add_collection(pc)
    ax.autoscale()
    return pc

def plotMESH(Mesh,li_value,path,name_plot):
    """this function is used to plot the mesh
    Args:
        Mesh (Mesh): the mesh
        path (str): the path
        name_plot (str): the name of the plot
    """
    verts_li = []
    index_li=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        verts_li.append([[element.n1.x,element.n1.y],[element.n2.x,element.n2.y],[element.n3.x,element.n3.y]])
        index_li.append([element.n1.id,element.n2.id,element.n3.id])
    x=[]
    y=[]

    #showing the plot
    fig = Figure()
    fig.set_size_inches(10, 10)
    ax= fig.add_subplot(111)
    li_value=np.array(li_value)
    min_colorbar=min(li_value)
    max_colorbar=max(li_value)

    #set the aspect ratio
    ax.set_aspect('equal')
    #remove the axis
    ax.axis('off')

    #plot the contour
    colorbar=np.linspace(min_colorbar,max_colorbar,100)
    pc = quatplot(verts_li, li_value, ax=ax,edgecolors='k', cmap='jet', linewidths=0.1)
    pc.set_clim(min(colorbar),max(colorbar))
    #PRECENTAGE OF THE ERROR FOR EACH ELEMENT with micro strain with greek letter \mu
    pc.set_clim(min(colorbar),max(colorbar))
    fig.colorbar(pc, ax=ax)
    ax.plot(x,y, marker='o', linestyle='', markersize=0.5, color='k')    
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")
    

    fig.savefig(f"{path}/plot/gradientCountor-step{name_plot}.jpg",dpi=300)
    plt.close(fig)



