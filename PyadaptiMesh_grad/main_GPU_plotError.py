# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries


import sys
from DataStructure_jar_Element             import JarOfElement
from DataStructure_jar_Node                import JarOfNodes
from DataStructure_jar_GussianPoint        import JarOfGussianPoint
from DataStructure_Mesh                    import Mesh


from Reader_handler import reader
from Func_parallel_calMeshSRP import mul_point_ALL

from Func_parallel_calFemValue import calFemValue

from Plot_Error import show_countourError
from Write_csvfileError import Write_csvfileError
import re_iding
import time


def Plot_Error(csvFile,inpFile,savePath):
    """ this function plot error of mesh
    Args:
        csvFile (str): csv file path
        inpFile (str): inp file path
        savePath (str): save path
    """
    print(f"info    : reading  mesh")

    first_Nodes = JarOfNodes()
    first_GussianPoints = JarOfGussianPoint()
    first_Elements = JarOfElement()
    firstMesh = Mesh(first_Nodes,first_GussianPoints,first_Elements)
    
    reader(firstMesh).read(inpFile)
    reader(firstMesh).read(csvFile)
    re_iding.rename(firstMesh)
    firstMesh=calFemValue(firstMesh)
    #calculate the srp for the step mesh
    print(f"info    : calculating  mesh srp value")
    firstMesh=mul_point_ALL(firstMesh,firstMesh)   
    #calculate the step mesh error and save it
    print(f"info    : calculating  mesh error and save it")
    maximumError=[i.Error for i in firstMesh.JarOfElement.elements]
    show_countourError(firstMesh,savePath,f"Error",f"Error",0,max(maximumError))
    Write_csvfileError(firstMesh,savePath)
  
  
if __name__ == "__main__":
    time_start = time.time()
    csvFile=sys.argv[1]
    inpFile=sys.argv[2]
    savePath=sys.argv[3]
    Plot_Error(csvFile,inpFile,savePath)
    time_end = time.time()
    print(f"info    : total time {time_end-time_start}")
    print("####################done####################")
