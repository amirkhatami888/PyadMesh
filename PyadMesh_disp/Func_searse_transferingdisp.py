# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import numpy as np

def transfering(element,node):
    """this function is used to transfer the displacement from element to node
    Args:
        element (Element): the element
        node (NodePoint): the node
    Returns:
        float: the displacement of the node
    """
    x=np.float64(node[0])
    y=np.float64(node[1])
    x1=np.float64(element.n1.x)
    y1=np.float64(element.n1.y)
    x2=np.float64(element.n2.x)
    y2=np.float64(element.n2.y)
    x3=np.float64(element.n3.x)
    y3=np.float64(element.n3.y)
    area=np.linalg.det(np.array([[1,x1,y1],[1,x2,y2],[1,x3,y3]],dtype=np.float64))
    N1=np.float64(np.linalg.det(np.array([[1,x,y],[1,x2,y2],[1,x3,y3]],dtype=np.float64))/area)
    N2=np.float64(np.linalg.det(np.array([[1,x1,y1],[1,x,y],[1,x3,y3]],dtype=np.float64))/area)
    N3=np.float64(np.linalg.det(np.array([[1,x1,y1],[1,x2,y2],[1,x,y]],dtype=np.float64))/area)
    N=np.array([[N1,0,N2,0,N3,0],[0,N1,0,N2,0,N3]])
    D=np.transpose( np.array([element.n1.U1,element.n1.U2,element.n2.U1,element.n2.U2,element.n3.U1,element.n3.U2],dtype=np.float64))
    Us=np.matmul(N,D)
    Us_np=np.array(Us)
    return Us_np
