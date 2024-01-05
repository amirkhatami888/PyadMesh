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
from Func_parallel_calMeshSRP import mul_point_ALL
from Func_parallel_calPointSRP import one_point
from Func_parallel_calFemValue import calFemValue
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from Write_posfile import write_pos
from Func_GSH_meshGeneration import meshGeneration
from Write_csvfile import Write_csvfile
import Reader_disp as Reader_disp
from Write_logError import ERORR_LOGER_init,ERORR_LOGER_write
from Func_parallel_calTransferDisp import calTransferDisplacement
from plot_pureMesh import plotPureMESH



def auto_generateMesh(csvFile,inpFile,igsFile,savePath,max_iteration,scalefactor,dispFile,plotType,meshAlgorithm):    
    """this function is used to generate the mesh automatically and save the mesh in the savePath and transfer gradiant from first mesh to the steper mesh
    Args:
        csvFile (str): the csv file
        inpFile (str): the inp file
        igsFile (str): the igs file
        savePath (str): the save path
        max_iteration (int): the maximum iteration
        scalefactor (float): the scale factor
        dispFile (str): the displacement file
        plotType (str): the plot type
        meshAlgorithm (int): the mesh algorithm
    """
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)
    step=1
    #read step mesh 
    print(f"info    : reading {step} mesh")
    ErorrFile=ERORR_LOGER_init(savePath)
    first_Nodes = JarOfNodes()
    first_GussianPoints = JarOfGussianPoint()
    first_Elements = JarOfElement()
    firstMesh = Mesh(first_Nodes,first_GussianPoints,first_Elements)

    reader(firstMesh).read(inpFile)
    reader(firstMesh).read(csvFile)
    Reader_disp.dispReader(firstMesh,dispFile).read()

    re_iding.rename(firstMesh)

    print(f"info    : calculating {step} mesh fem value")
    firstMesh=calFemValue(firstMesh)

    #calculate the srp for the step mesh
    print(f"info    : calculating {step} mesh srp value")
    firstMesh=mul_point_ALL(firstMesh,firstMesh)
    #ERORR info logger
    maximumError,maximumPureError=ERORR_LOGER_write(ErorrFile,step,firstMesh,step)
    # calculate the step mesh error and save it
    print(f"info    : calculating {step} mesh error and save it")
    if plotType=="matplotlib":
        from Plot_Error import show_countourError
        from plot_Gradient import plotMESH
        from Plot_PureError import show_countourPureError
        import Plot_dispU1
        import Plot_dispU2
        show_countourError(firstMesh,savePath,f"RelativeError-step{step}",0,maximumError)
        show_countourPureError(firstMesh,savePath,f"AbsouloteError-step{step}",0,maximumPureError)
        li_value=[element.fem_value for element in firstMesh.JarOfElement.elements]
        plotMESH(firstMesh,li_value,savePath,f"{step}")
        Plot_dispU1.save_countourDisplacement(firstMesh, savePath,f"U1-step{step}","dispalacement U1")
        Plot_dispU2.save_countourDisplacement(firstMesh, savePath,f"U2-step{step}","dispalacement U2")
    elif plotType=="tecplot":
        from Plot_Error_tecplot import plotError
        from plot_Gradient_tecplot import plotMESH
        from Plot_PureError_tecplot import plotPureError
        import Plot_dispU_tecplot
        plotError(firstMesh,savePath,f"RelativeError-step{step}")
        plotPureError(firstMesh,savePath,f"AbsouloteError-step{step}")
        plotMESH(firstMesh,savePath,f"{step}")
        Plot_dispU_tecplot.save_countourDisplacement(firstMesh, savePath,f"{step}","dispalacement")
    plotPureMESH(firstMesh,savePath,f"{step}")
    #generate the new mesh
    print(f"info    : generating {step+1} mesh")
    new_mesh=meshGeneration(igsFile,write_pos(firstMesh,scalefactor,step),savePath,step,meshAlgorithm)

    #read the new mesh
    print(f"info    : reading {step+1} mesh")
    step_Elements = JarOfElement()
    step_Nodes = JarOfNodes()
    step_GussianPoints = JarOfGussianPoint()
    stepMesh = Mesh(step_Nodes,step_GussianPoints,step_Elements)
    reader(stepMesh).read(new_mesh)
    #tranfer data from first mesh to step mesh
    print(f"info    : transfering {step} mesh data to {step+1} mesh")
    stepMesh=mul_point_ALL(firstMesh,stepMesh)
    stepMesh=calTransferDisplacement(firstMesh,stepMesh)
    #write the step mesh srp value
    print(f"info    : writing {step+1} mesh srp value")
    Write_csvfile(stepMesh,savePath)
    #############################################################################################
    for i in range(2,max_iteration+1):
        step=i
        print(f"nfo    : step    : {step}")
        #read steper mesh
        print(f"info    : reading {step} mesh")
        reader(stepMesh).read(fr"{savePath}/final_mat.csv")
        stepMesh=calFemValue(stepMesh)
        #calculate the srp for the steper mesh
        print(f"info    : calculating {step} mesh srp value")
        stepMesh=mul_point_ALL(stepMesh,stepMesh)
        #calculate the steper mesh error and save it
        print(f"info    : calculating {step} mesh error and save it")
        if plotType=="matplotlib":
            from Plot_Error import show_countourError
            from plot_Gradient import plotMESH
            from Plot_PureError import show_countourPureError
            import Plot_dispU1
            import Plot_dispU2
            show_countourError(stepMesh,savePath,f"RelativeError-step{step}",0,maximumError)
            show_countourPureError(stepMesh,savePath,f"AbsouloteError-step{step}",0,maximumPureError)
            li_value=[element.fem_value for element in stepMesh.JarOfElement.elements]
            plotMESH(stepMesh,li_value,savePath,f"{step}")
            Plot_dispU1.save_countourDisplacement(stepMesh, savePath,f"U1-step{step}","dispalacement U1")
            Plot_dispU2.save_countourDisplacement(stepMesh, savePath,f"U2-step{step}","dispalacement U2")
        elif plotType=="tecplot":
            from Plot_Error_tecplot import plotError
            from plot_Gradient_tecplot import plotMESH
            from Plot_PureError_tecplot import plotPureError
            import Plot_dispU_tecplot
            plotError(stepMesh,savePath,f"RelativeError-step{step}")
            plotMESH(stepMesh,savePath,f"{step}")
            plotPureError(stepMesh,savePath,f"AbsouloteError-step{step}")
            Plot_dispU_tecplot.save_countourDisplacement(stepMesh, savePath,f"{step}","dispalacement U")
        plotPureMESH(stepMesh,savePath,f"{step}")
        #ERORR info logger
        ERORR_LOGER_write(ErorrFile,step,stepMesh,step)
        #generate the new mesh
        print(f"info    : generating {step+1} mesh")
        new_mesh=meshGeneration(igsFile,write_pos(stepMesh,scalefactor,step),savePath,step,meshAlgorithm)
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
        stepMesh=mul_point_ALL(firstMesh,stepMesh)
        stepMesh=calTransferDisplacement(firstMesh,stepMesh)
        #write the step mesh srp value
        print(f"info    : writing {step+1} mesh srp value")
        Write_csvfile(stepMesh,savePath)
    reader(stepMesh).read(fr"{savePath}/final_mat.csv")
    stepMesh=calFemValue(stepMesh)
    #calculate the srp for the steper mesh
    print(f"info    : calculating {step+1} mesh srp value")
    stepMesh=mul_point_ALL(stepMesh,stepMesh)
    #calculate the steper mesh error and save it
    print(f"info    : calculating {step+1} mesh error and save it")
    
    if plotType=="matplotlib":
        from Plot_Error import show_countourError
        from plot_Gradient import plotMESH
        from Plot_PureError import show_countourPureError
        import Plot_dispU1
        import Plot_dispU2
        show_countourError(stepMesh,savePath,f"RelativeError-step{step+1}",0,maximumError)
        show_countourPureError(stepMesh,savePath,f"AbsouloteError-step{step+1}",0,maximumPureError)
        li_value=[element.fem_value for element in stepMesh.JarOfElement.elements]
        plotMESH(stepMesh,li_value,savePath,f"{step+1}")
        Plot_dispU1.save_countourDisplacement(stepMesh, savePath,f"U1-step{step+1}","dispalacement U1")
        Plot_dispU2.save_countourDisplacement(stepMesh, savePath,f"U2-step{step+1}","dispalacement U2")
    elif plotType=="tecplot":
        from Plot_Error_tecplot import plotError
        from plot_Gradient_tecplot import plotMESH
        from Plot_PureError_tecplot import plotPureError
        import Plot_dispU_tecplot
        plotError(stepMesh,savePath,f"RelativeError-step{step+1}")
        plotMESH(stepMesh,savePath,f"{step+1}")
        plotPureError(stepMesh,savePath,f"AbsouloteError-step{step+1}")
        Plot_dispU_tecplot.save_countourDisplacement(stepMesh, savePath,f"{step+1}","dispalacement U1")
    plotPureMESH(stepMesh,savePath,f"{step+1}")
    #ERORR info logger
    ERORR_LOGER_write(ErorrFile,step,stepMesh,step)
        
    



if __name__ == "__main__":
    time_start=time.time()
    CSV_FIILE=sys.argv[1]
    INP_FILE=sys.argv[2]
    IGS_FILE=sys.argv[3]
    SAVE_FILE=sys.argv[4]
    MAX_ITER=int(sys.argv[5])
    scalefactor=float(sys.argv[6])
    dispFile=sys.argv[7]
    plotType=sys.argv[8]
    meshAlgorithm=int(sys.argv[9])
    auto_generateMesh(CSV_FIILE,INP_FILE,IGS_FILE,SAVE_FILE,MAX_ITER,scalefactor,dispFile,plotType,meshAlgorithm)
    time_end = time.time()
    print(f"info    : total time is {time_end-time_start}")
print("####################done####################")
