
# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import Func_searse_searchGaussPoint as searchGaussPoint
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
    li_gauss=searchGaussPoint.search_GaussPoint(element,mesh.GiveJarOfGussianPoint().TONumPyArrayWithCoordinates())
    if len(li_gauss) != 0:
        grad=li_gauss[0][2]
    else:
        print(li_gauss)
        raise ValueError("the number of gauss points is not equal to 1")
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