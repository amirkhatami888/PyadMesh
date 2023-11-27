# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import sys
from   DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from   DataStructure_Point_Node              import NodePoint       as Node
from   DataStructure_Point_Gaussian          import GaussianPoint   as GaussianPoint
from   DataStructure_jar_Element             import JarOfElement
from   DataStructure_jar_Node                import JarOfNodes
from   DataStructure_jar_GussianPoint        import JarOfGussianPoint
from   DataStructure_Mesh                    import Mesh
from   Reader_abaqusCSV   import abaqusCSV
from   Reader_abaqusINP   import abaqusINP
from   Reader_GmeshDAT    import GmeshDAT
from   Reader_myselfCSV   import myselfCSV_Gradient 
from   Reader_handler import reader
import Func_searse_isInsideElement as isInsideElement
import Func_searse_serchElement as serchElement
import Func_searse_searchGaussPoint as searchGaussPoint
import Func_searse_Fitting_leastSqure_ord1 as Fitting
import func_nearestPoint 
import multiprocessing 

def one_point(firstMesh,point):
    """function to calculate the gradient of a point from other points

    Args:
        firstMesh (instance of mesh class): the mesh
        point (list): the point

    Returns:
        float: the gradient of the point
    """
    id_element_centerOfPatch=isInsideElement.kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates())
    if len(id_element_centerOfPatch) >= 1:
        id_element_centerOfPatch=id_element_centerOfPatch[0]
    elif len(id_element_centerOfPatch) == 0:
        print('there is no finde center of element')
        nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())

        id_element_centerOfPatch=isInsideElement.kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates())[0]

        
    element_centerOfPatch=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_centerOfPatch)
    ids_patch=serchElement.search_element(firstMesh,element_centerOfPatch)
    patch_elements=[]
    for id in ids_patch:
        patch_elements.append(firstMesh.GiveJarOfElement().GiveElementWithID(id))
    patch_GussianPoints=[]
    for element in patch_elements:
        patch_GussianPoints.extend(searchGaussPoint.search_GaussPoint(element,firstMesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates()))
    patch_GussianPoints=np.array(patch_GussianPoints)
    gradient=Fitting.regressor(patch_GussianPoints,point[0],point[1])
    return gradient
    



def MeshSRP(firstMesh,second_Mesh):
    """function to calculate the gradient of a mesh from other mesh

    Args:
        firstMesh (instance of mesh class): the first mesh  
        second_Mesh (instance of mesh class): the second mesh
    
    Returns:
        second_Mesh (instance of mesh class): the second mesh with gradient
    """
    for element in second_Mesh.GiveJarOfElement().GiveElements():
        point=element.GaussianPoint_coordinate
        element.srp_value =one_point(firstMesh,point)

    return second_Mesh




def cpuParallel_one_point(firstMesh,point,id__main,return_list):
    """function to calculate the gradient of a point from other points

    Args:
        firstMesh (instance of mesh class): the mesh
        point (list): the point

    Returns:
        float: the gradient of the point
    """
    id_element_centerOfPatch=isInsideElement.kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates())
    if len(id_element_centerOfPatch) >= 1:
        id_element_centerOfPatch=id_element_centerOfPatch[0]
    elif len(id_element_centerOfPatch) == 0:
        nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())

        id_element_centerOfPatch=isInsideElement.kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates())[0]

        
    element_centerOfPatch=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_centerOfPatch)
    ids_patch=serchElement.search_element(firstMesh,element_centerOfPatch)
    patch_elements=[]
    for id in ids_patch:
        patch_elements.append(firstMesh.GiveJarOfElement().GiveElementWithID(id))
    patch_GussianPoints=[]
    for element in patch_elements:
        patch_GussianPoints.extend(searchGaussPoint.search_GaussPoint(element,firstMesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates()))
    patch_GussianPoints=np.array(patch_GussianPoints)
    gradient=Fitting.regressor(patch_GussianPoints,point[0],point[1])
    return_list.append([id__main,point[0],point[1],gradient])
    
