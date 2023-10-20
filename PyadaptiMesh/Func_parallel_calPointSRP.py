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
import Func_parallel_isInsideElement as isInsideElement
import Func_parallel_serchElement as serchElement
import Func_parallel_searchGaussPoint as searchGaussPoint
import Func_parallel_Fitting_leastSqure_ord1 as Fitting
import func_nearestPoint 


def one_point(firstMesh,point):
    """function to calculate the gradient of a point from other points

    Args:
        firstMesh (instance of mesh class): the mesh
        point (list): the point

    Returns:
        float: the gradient of the point
    """
    id_element_centerOfPatch=isInsideElement.one_kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates(),thread_x=32,thread_y=32)
    if len(id_element_centerOfPatch) >= 1:
        id_element_centerOfPatch=id_element_centerOfPatch[0]
    elif len(id_element_centerOfPatch) == 0:
        nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())

        id_element_centerOfPatch=isInsideElement.one_kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates(),thread_x=32,thread_y=32)[0]

        
    element_centerOfPatch=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_centerOfPatch)
    ids_patch=serchElement.one_search_element(firstMesh,element_centerOfPatch,thread_x=32,thread_y=32)  
    patch_elements=[]
    for id in ids_patch:
        patch_elements.append(firstMesh.GiveJarOfElement().GiveElementWithID(id))
    patch_GussianPoints=[]
    for element in patch_elements:
        patch_GussianPoints.extend(searchGaussPoint.one_search_GaussPoint(element,firstMesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates(),thread_x=32,thread_y=32))
    patch_GussianPoints=np.array(patch_GussianPoints)
    gradient=Fitting.regressor(patch_GussianPoints,point[0],point[1])
    return gradient
    


def gpuParallel_one_point(firstMesh,point,id__main,return_list,thread_x=32,thread_y=32):
    """function to calculate the gradient of a point from other points

    Args:
        firstMesh (instance of mesh class): the mesh
        point (list): the point

    Returns:
        float: the gradient of the point
    """
    id_element_centerOfPatch=isInsideElement.one_kernel_check_PointIsInsideElements(point,firstMesh.GiveElementsNumpyArrayWithCoordinates(),thread_x=thread_x,thread_y=thread_y)
    if len(id_element_centerOfPatch) >= 1:
        id_element_centerOfPatch=id_element_centerOfPatch[0]
    elif len(id_element_centerOfPatch) == 0:
        nearestPoint=func_nearestPoint.nearest_point(point,firstMesh.GiveNodeNumpyArray())

        id_element_centerOfPatch=isInsideElement.one_kernel_check_PointIsInsideElements(nearestPoint,firstMesh.GiveElementsNumpyArrayWithCoordinates())[0]

        
    element_centerOfPatch=firstMesh.GiveJarOfElement().GiveElementWithID(id_element_centerOfPatch)
    ids_patch=serchElement.one_search_element(firstMesh,element_centerOfPatch,thread_x=thread_x,thread_y=thread_y)
    patch_elements=[]
    for id in ids_patch:
        patch_elements.append(firstMesh.GiveJarOfElement().GiveElementWithID(id))
    patch_GussianPoints=[]
    for element in patch_elements:
        patch_GussianPoints.extend(searchGaussPoint.one_search_GaussPoint(element,firstMesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates(),thread_x=thread_x,thread_y=thread_y))
    patch_GussianPoints=np.array(patch_GussianPoints)
    gradient=Fitting.regressor(patch_GussianPoints,point[0],point[1])
    return_list.append([id__main,point[0],point[1],gradient])
    
