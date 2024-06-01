# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import Func_searse_isInsideElement as isInsideElement
import Func_searse_transferingdisp as transfering
import func_nearestPoint as func_nearestPoint

def calTransferDisplacement(firstMesh,secondMesh):
    """this function is used to transfer displacement from first mesh to second mesh
    Args:
        firstMesh (mesh): first mesh
        secondMesh (mesh): second mesh
    Returns:
        mesh: second mesh with displacement
    """
    for node in secondMesh.GiveJarOfNodes().nodes:
        point=[node.x,node.y]
        node_id=node.id
        id_element_center=isInsideElement.kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates())
        if len(id_element_center) >= 1:
            id_element_center=id_element_center[0]
        elif len(id_element_center) == 0:
            nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())
            id_element_center=isInsideElement.kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates())[0]
        
        element_center=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_center)
        u1,u2=transfering.transfering(element_center,point)
        node.U1=u1
        node.U2=u2
    return secondMesh