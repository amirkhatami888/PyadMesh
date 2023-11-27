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

def Plot_Error(csvFile,inpFile,savePath,inpFile_fineMesh,csvFile_fineMesh):
    """ this function plot error of mesh
    Args:
        csvFile (str): csv file path
        inpFile (str): inp file path
        savePath (str): save path
        inpFile_fineMesh (str): inp file path
        csvFile_fineMesh (str): csv file path
    """
    #read fine mesh 
    print(f"info    : reading  mesh")

    fine_Nodes = JarOfNodes()
    fine_GussianPoints = JarOfGussianPoint()
    fine_Elements = JarOfElement()
    fineMesh = Mesh(fine_Nodes,fine_GussianPoints,fine_Elements)

    reader(fineMesh).read(inpFile_fineMesh)
    reader(fineMesh).read(csvFile_fineMesh)
    re_iding.rename(fineMesh)
    firstMesh=calFemValue(fineMesh)
    #read coarse mesh
    print(f"info    : reading  mesh")
    coarse_Nodes = JarOfNodes()
    coarse_GussianPoints = JarOfGussianPoint()
    coarse_Elements = JarOfElement()
    coarseMesh = Mesh(coarse_Nodes,coarse_GussianPoints,coarse_Elements)
    
    reader(coarseMesh).read(inpFile)
    reader(coarseMesh).read(csvFile)
    re_iding.rename(coarseMesh)
    
    #tranfer data from first mesh to step mesh
    fineMesh=calFemValue(fineMesh)
    coarseMesh=calFemValue(coarseMesh)
    coarseMesh=mul_point_ALL(fineMesh,coarseMesh)
    #calculate the step mesh error and save it
    print(f"info    : calculating  mesh error and save it")
    maximumError=[i.Error for i in coarseMesh.JarOfElement.elements]
    show_countourError(coarseMesh,savePath,f"Error",f"Error",0,max(maximumError))
    Write_csvfileError(coarseMesh,savePath)
    



  
if __name__ == "__main__":
    time_start = time.time()
    csvFile=sys.argv[1]
    inpFile=sys.argv[2]
    savePath=sys.argv[3]
    inpFile_fineMesh=sys.argv[4]
    csvFile_fineMesh=sys.argv[5]
    Plot_Error(csvFile,inpFile,savePath,inpFile_fineMesh,csvFile_fineMesh)
    time_end = time.time()
    print(f"info    : total time {time_end-time_start}")
    print("####################done####################")
