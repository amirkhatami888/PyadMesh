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
import numpy as np
import os

def quatplot(verts, values, ax=None, **kwargs):
    pc = matplotlib.collections.PolyCollection(verts, **kwargs)
    pc.set_array(values)
    ax.add_collection(pc)
    ax.autoscale()
    return pc

def plotMESH(Mesh,li_value,path,name_plot):
    verts_li = []

    for element in Mesh.GiveJarOfElement().GiveElements():
        verts_li.append([[element.n1.x,element.n1.y],[element.n2.x,element.n2.y],[element.n3.x,element.n3.y]])
    x=[]
    y=[]
    for node in Mesh.GiveJarOfNodes().GiveNodes():
        x.append(node.x)
        y.append(node.y)
    #showing the plot
    fig = Figure()
    fig.set_size_inches(10, 10)
    ax= fig.add_subplot(111)
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
    fig.colorbar(pc, ax=ax)
    # ax.plot(x,y, marker='o', linestyle='', markersize=0.5, color='k')
    ax.set_title(str(name_plot))
    print(f"info: saving {name_plot}")\
    
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")
    
    # fig.savefig(f"{path}/plot/{name_plot}.pdf",dpi=300)
    fig.savefig(f"{path}/plot/{name_plot}.png",dpi=700)
    print(f"info: {name_plot} saved")
    plt.close(fig)

 


