# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import pandas as pd
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
import warnings
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

warnings.simplefilter('ignore', category=NumbaPerformanceWarning)

def mul_point(firstMesh,points,thread_x=32,thread_y=32):
    """function for calculate the fem value of the points from other mesh

    Args:
        firstMesh (instance of mesh class): the mesh
        points (numpy array): the points

    Returns:
        numpy array: the fem value of the points
    
    """
   
    mat_id_ElementCenterOfPatch=isInsideElement.mul_kernel_check_PointIsInsideElements(points,firstMesh.GiveElementsNumpyArrayWithCoordinates(),thread_x,thread_y)
    li_id_ElementCenterOfPatch=[]
    for i in range(len(mat_id_ElementCenterOfPatch)):
        if mat_id_ElementCenterOfPatch[i]!=None:
            li_id_ElementCenterOfPatch.append(mat_id_ElementCenterOfPatch[i])    
        else: 
            nearestPoint=func_nearestPoint.nearest_point(points[i],firstMesh.GiveNodeNumpyArray())
            id_element_centerOfPatch=isInsideElement.one_kernel_check_PointIsInsideElements([nearestPoint[0],nearestPoint[1]],firstMesh.GiveElementsNumpyArrayWithCoordinates())
            li_id_ElementCenterOfPatch.append(id_element_centerOfPatch)
            
    element_centerOfPatch=np.array([firstMesh.GiveJarOfElement().GiveElementWithID(i).ToMatrix_IDs() for i in li_id_ElementCenterOfPatch])
    mat_ids_patchs=serchElement.mul_kernel_check_PointIsInsideElementssearch_element(firstMesh.GiveJarOfElement().ToNumPyArrayWithIDs(),element_centerOfPatch,thread_x,thread_y)
    mat_patch_elements=[]
    for patch in  mat_ids_patchs:
        li_path=[]
        for id in patch:
            li_path.append(firstMesh.GiveJarOfElement().GiveElementWithID(id))
        mat_patch_elements.append(li_path) 
    mat_patch_GussianPoints=[]
    for patchs in mat_patch_elements:
        patch_GussianPoints=searchGaussPoint.mul_search_GaussPoint(np.array([i.ToMatrix_Coordinates() for i in patchs]),firstMesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates(),thread_x,thread_y)
        mat_patch_GussianPoints.append(patch_GussianPoints)
    mat_gradient=[]
    for i in range(len(points)):
        patch=mat_patch_GussianPoints[i]
        point=points[i]
        gradient=Fitting.regressor(patch,point[0],point[1])
        grad_li=[point[0],point[1],gradient]
        mat_gradient.append(grad_li)
    return mat_gradient
    
    


def mul_point_ALL(firstMesh,second_Mesh,thread_x=32,thread_y=32):
    """function for calculate the fem value of the Gaussian points from other mesh

    Args:
        firstMesh (instance of mesh class): the mesh
        second_Mesh (instance of mesh class): the mesh
    
    Returns:
        instance of mesh class: the mesh with fem value of the Gaussian points
    """
    NU_simultaneous_points=1024
    final_mat=[]
    Gpoints_secondMesh=np.array([i.GaussianPoint_coordinate for i in second_Mesh.GiveJarOfElement().GiveElements()])
    inds_secondMesh=np.array([i.GiveID() for i in second_Mesh.GiveJarOfElement().GiveElements()])
    for  i in range(0,len(Gpoints_secondMesh),NU_simultaneous_points):
        points=Gpoints_secondMesh[i:i+NU_simultaneous_points].reshape(-1,2)
        ids=inds_secondMesh[i:i+NU_simultaneous_points].reshape(-1,1)
        mat_grad=mul_point(firstMesh,points,thread_x,thread_y)
        mat_grad=np.array(mat_grad).reshape(-1,3)
        mat_grad=np.concatenate((ids,mat_grad),axis=1)
        final_mat.extend(mat_grad)
    final_mat=np.array(final_mat).reshape(-1,4)

    pd_final_mat=pd.DataFrame(final_mat)
    pd_final_mat.sort_values(by=[0],inplace=True)
    final_mat=pd_final_mat.values

    for i in range(len(final_mat)):
        second_Mesh.GiveJarOfElement().GiveElements()[i].srp_value=final_mat[i][3]
    return second_Mesh


        
        

