import Func_parallel_isInsideElement as isInsideElement
import Func_parallel_transferingdisp as transfering
import func_nearestPoint as func_nearestPoint

def calTransferDisplacement(firstMesh,secondMesh):
    for node in secondMesh.GiveJarOfNodes().nodes:
        point=[node.x,node.y]
        node_id=node.id
        id_element_center=isInsideElement.one_kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates())
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