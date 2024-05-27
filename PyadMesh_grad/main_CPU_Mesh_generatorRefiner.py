# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import warnings
import sys
import time

import re_iding
from DataStructure_Element_Triangle_order1 import Triangle_order1 as Element
from DataStructure_Point_Node              import NodePoint       as Node
from DataStructure_Point_Gaussian          import GaussianPoint   as GaussianPoint
from DataStructure_jar_Element             import JarOfElement
from DataStructure_jar_Node                import JarOfNodes
from DataStructure_jar_GussianPoint        import JarOfGussianPoint
from DataStructure_Mesh                    import Mesh
from Reader_abaqusCSV   import abaqusCSV
from Reader_abaqusINP   import abaqusINP
from Reader_GmeshDAT    import GmeshDAT
from Reader_myselfCSV   import myselfCSV_Gradient 
from Reader_handler import reader
from Func_searse_calMeshSRP import MeshSRP
from Func_searse_calPointSRP import one_point
from Func_searse_calFemValue import calFemValue
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from Write_posfile import write_pos
from Func_GSH_meshGeneration import meshGeneration
from Write_csvfile import Write_csvfile
import Reader_disp as Reader_disp
from Write_logError import ERORR_LOGER_init,ERORR_LOGER_write
from Func_searse_calTransferDisp import calTransferDisplacement
from plot_pureMesh import plotPureMESH



def auto_generateMesh(inpFile,igsFile,savePath,max_iteration,scalefactor,dispFile):
    """
    this function is used to generate the mesh automatically and save the mesh in the savePath
    Args:
        inpFile (str): the inp file
        igsFile (str): the igs file
        savePath (str): the save path
        max_iteration (int): the maximum iteration
        scalefactor (float): the scale factor
        dispFile (str): the displacement file
    """
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)
    step=1
    #read step mesh 
    print(f"info    : reading {step} mesh")
    first_Nodes = JarOfNodes()
    first_GussianPoints = JarOfGussianPoint()
    first_Elements = JarOfElement()
    firstMesh = Mesh(first_Nodes,first_GussianPoints,first_Elements)

    reader(firstMesh).read(inpFile)
    Reader_disp.dispReader(firstMesh,dispFile).read()    
    
    re_iding.rename(firstMesh)

    plotPureMESH(firstMesh,savePath,f"{step}")

    #generate the new mesh
    print(f"info    : generating {step+1} mesh")
    new_mesh=meshGeneration(igsFile,write_pos(firstMesh,scalefactor,step),savePath,step)

    #read the new mesh
    print(f"info    : reading {step+1} mesh")
    step_Elements = JarOfElement()
    step_Nodes = JarOfNodes()
    step_GussianPoints = JarOfGussianPoint()
    stepMesh = Mesh(step_Nodes,step_GussianPoints,step_Elements)
    reader(stepMesh).read(new_mesh)
    #tranfer data from first mesh to step mesh
    print(f"info    : transfering {step} mesh data to {step+1} mesh")
    stepMesh=calTransferDisplacement(firstMesh,stepMesh)
    #############################################################################################
    for i in range(2,max_iteration+1):
        step=i
        print(f"nfo    : step    : {step}")
    
        plotPureMESH(stepMesh,savePath,f"{step}")
        #generate the new mesh
        print(f"info    : generating {step+1} mesh")
        new_mesh=meshGeneration(igsFile,write_pos(firstMesh,scalefactor,step),savePath,step)

        #read the new mesh
        print(f"info    : reading {step+1} mesh")
        del stepMesh
        stepElements = JarOfElement()
        stepNodes = JarOfNodes()
        stepGussianPoints = JarOfGussianPoint()
        stepMesh = Mesh(stepNodes,stepGussianPoints,stepElements)
        reader(stepMesh).read(new_mesh)
        #tranfer data from step mesh to new mesh
        print(f"info    : transfering {step} mesh data to {step+1} mesh")
        stepMesh=calTransferDisplacement(firstMesh,stepMesh)
    plotPureMESH(stepMesh,savePath,f"{step+1}")


if __name__ == "__main__":
    time_start=time.time()
    INP_FILE=sys.argv[1]
    IGS_FILE=sys.argv[2]
    SAVE_FILE=sys.argv[3]
    MAX_ITER=int(sys.argv[4])
    scalefactor=float(sys.argv[5])
    dispFile=sys.argv[6]
    auto_generateMesh(INP_FILE,IGS_FILE,SAVE_FILE,MAX_ITER,scalefactor,dispFile)
    time_end = time.time()
    print(f"info    : total time is {time_end-time_start}")
print("####################done####################")
