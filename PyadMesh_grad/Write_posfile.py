# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np


def write_pos(Mesh,scalefactor,step ):
    """this function is used to write the pos file
    Args:
        Mesh (Mesh): the mesh
        scalefactor (float): the scale factor
        step (int): the step
    Returns:
        str: the name of the pos file
    """
    for node in Mesh.JarOfNodes.nodes:
        for element in Mesh.JarOfElement.elements:
            if node.id==element.n1.id or node.id==element.n2.id or node.id==element.n3.id:
                     node.nearestElements.add(element)  



  
    li_r=[]
    for node in Mesh.JarOfNodes.nodes:
        li_r.append(node.dervirative_phi*node.elementSize)
    r_tile=np.max(li_r)*scalefactor
    li_new_size=[]
    for node in Mesh.JarOfNodes.nodes:
        li_new_size.append(r_tile/node.dervirative_phi)
        
        
 
  
    
    li_points=Mesh.JarOfNodes.ToMatrix()
    li_points=np.array(li_points)
    file=open("posfile.pos","w")
    li=[]
    li.append('View "background mesh" {\n')
    for i in range(len(li_points)):
        temp="SP("+str(li_points[i][0])+","+str(li_points[i][1])+",0){"+str(li_new_size[i])+"};\n"
        
        

        li.append(temp)
    li.append('};\n')
    file.writelines(li)
    file.close()
    return "posfile.pos"