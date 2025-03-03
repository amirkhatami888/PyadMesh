# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import Func_parallel_isInsideElement_disp as isInsideElement
import Func_Parallel_N as N_cal
import Func_parallel_U_cal as U_cal
import numpy as np
def calTransferDisplacement(firstMesh,secondMesh):
    """this function is used to transfer displacement from first mesh to second mesh
    Args:
        firstMesh (mesh): first mesh
        secondMesh (mesh): second mesh
    Returns:
        mesh: second mesh with displacement
    """
    points=np.array(secondMesh.JarOfNodes.ToMatrix())
    Elements=firstMesh.JarOfElement.ToNumPyArrayWithCoordinates()
    Elements_sorted_base_newMesh=np.array(isInsideElement.mul_kernel_check_PointIsInsideElements(points,Elements),dtype=np.float64)

    N=N_cal.mul_calculator_N(points,Elements_sorted_base_newMesh)

    U__sorted_base_newMesh=[]
    for i in Elements_sorted_base_newMesh:
        if i is not None:
            id=i[0]
            element=firstMesh.JarOfElement.GiveElementWithID(id)
            n1=element.Give_n1()
            n2=element.Give_n2()
            n3=element.Give_n3()
            U_temp=[n1.U1,n1.U2,n2.U1,n2.U2,n3.U1,n3.U2]
            U__sorted_base_newMesh.append(U_temp)
        else:
            raise ValueError("Error: point is not inside any element")

    U__sorted_base_newMesh=np.array(U__sorted_base_newMesh,dtype=np.float64)
    final_U=U_cal.mul_calculator_U(N,U__sorted_base_newMesh)
    for i in range(len(secondMesh.JarOfNodes.nodes)):
        secondMesh.JarOfNodes.nodes[i].U1=final_U[i,0]
        secondMesh.JarOfNodes.nodes[i].U2=final_U[i,1]
    return secondMesh