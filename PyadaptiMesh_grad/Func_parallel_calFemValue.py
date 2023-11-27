
# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import Func_parallel_searchGaussPoint as searchGaussPoint
import numpy as np

def calculateGradient(mesh,element):
    """this function is used to calculate the gradient of the gauss point iside the element

    Args:
        mesh (instance of mesh class): the mesh
        element (instance of element class): the element

    Raises:
        ValueError: the number of gauss points is not equal to 1

    Returns:
        float: the gradient of the gauss point
    """
    li_gauss=searchGaussPoint.one_search_GaussPoint(element,mesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates())
    if len(li_gauss) == 1:
        grad=li_gauss[0][2]
    elif len(li_gauss) != 0 and len(li_gauss) !=1:
        sum_grad=0
        for i in li_gauss:
            sum_grad+=i[2]
        grad=sum_grad/len(li_gauss)
        # print('more than one Gnode in element')
        # raise ValueError("the number of gauss points is not equal to 1")
        
    else:
        print(li_gauss)
        print('there are no gauss point in element')
        # raise ValueError("the number of gauss points is not equal to 1")
    return float(grad)

def calFemValue(mesh):
    """this function is used to calculate the fem value of the gauss point iside the element

    Args:
        mesh (instance of mesh class): the mesh

    Returns:
        instance of mesh class  : the mesh with fem value
    """
    for element in mesh.JarOfElement.elements:
        element.fem_value=calculateGradient(mesh,element)
    return mesh