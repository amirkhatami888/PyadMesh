# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
from plot_tecplot_pltWriter import write_plt_tecplot
import numpy as np
import os

def plotPureError(Mesh,path,name_plot):
    """this function is used to plot the error
    Args:
        Mesh (Mesh): the mesh
        path (str): the path
        name_plot (str): the name of the plot
    """
    index_li=[]
    x=[]
    y=[]
    li_value_point=[]
    for element in Mesh.GiveJarOfElement().GiveElements():
        index_li.append([element.n1.id,element.n2.id,element.n3.id])
    for node in Mesh.JarOfNodes.nodes:
        for element in Mesh.JarOfElement.elements:
            if node.id==element.n1.id or node.id==element.n2.id or node.id==element.n3.id:
                     node.nearestElements.add(element)              
    for node in Mesh.GiveJarOfNodes().GiveNodes():
        x.append(node.x)
        y.append(node.y)
        li=[element.Error_pure for element in node.nearestElements]
        li_value_point.append(np.mean(li))    
    if not os.path.exists(f"{path}/plot"):
        os.makedirs(f"{path}/plot")    
    write_plt_tecplot(f"{path}/plot/{name_plot}.plt" ,name_plot,x,y,li_value_point,index_li)

 