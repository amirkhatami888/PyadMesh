import Func_searse_isInsideElement as isInsideElement
import Func_searse_transferingdisp as transfering
import func_nearestPoint as func_nearestPoint

def calTransferDisplacement(firstMesh,secondMesh):
    """ this function is used to calculate the transfer displacement from firstMesh to secondMesh
    Args:
        firstMesh(Mesh): the first mesh
        secondMesh(Mesh): the second mesh
    Returns:
        Mesh: the second mesh with transfered displacement
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


def calTransferDisplacement_point(firstMesh,node_X,noxe_y):
    """ this function is used to calculate the transfer displacement from firstMesh to secondMesh
    Args:
        firstMesh(Mesh): the first mesh
        secondMesh(Mesh): the second mesh
    Returns:
        Mesh: the second mesh with transfered displacement
    """
    point=[node_X,noxe_y]
    id_element_center=isInsideElement.kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates())
    if len(id_element_center) >= 1:
        id_element_center=id_element_center[0]
    elif len(id_element_center) == 0:
        nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())
        id_element_center=isInsideElement.kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates())[0]
        
    element_center=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_center)
    u1,u2=transfering.transfering(element_center,point)
    return [u1,u2]

def calTransferDisplacement_point_parallel(firstMesh,point,node_id,return_list):
    """ this function is used to calculate the transfer displacement from firstMesh to secondMesh
    Args:
        firstMesh(Mesh): the first mesh
        secondMesh(Mesh): the second mesh
    Returns:
        Mesh: the second mesh with transfered displacement
    """
    id_element_center=isInsideElement.kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates())
    if len(id_element_center) >= 1:
        id_element_center=id_element_center[0]
    elif len(id_element_center) == 0:
        nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())
        id_element_center=isInsideElement.kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates())[0]
        
    element_center=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_center)
    u1,u2=transfering.transfering(element_center,point)
    return_list.append([node_id,point[0],point[1],u1,u2])