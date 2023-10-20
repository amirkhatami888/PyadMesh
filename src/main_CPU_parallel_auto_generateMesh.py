# mail: amirkhatami@gmail.com
# author: amirhossein khatami
#importing libraries
import multiprocessing
import numpy as np
import math
import pandas as pd
import warnings
import sys
import copy
import time
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
from Func_searse_calMeshSRP import cpuParallel_one_point
from Func_searse_calFemValue import calFemValue
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from Write_posfile import write_pos
from Func_GSH_meshGeneration import meshGeneration
from Write_csvfile import Write_csvfile
from Plot_Error import show_countourError
from Write_logError import ERORR_LOGER_init,ERORR_LOGER_write
from plot_Gradient import plotMESH
from plot_pureMesh import plotPureMESH
import re_iding



        


if __name__ == "__main__":
    time_start=time.time()
    csvFile=sys.argv[1]
    inpFile=sys.argv[2]
    igsFile=sys.argv[3]
    savePath=sys.argv[4]
    max_iteration=int(sys.argv[5])
    scalefactor=float(sys.argv[6])
    ratio_selection=float(sys.argv[7])
    core=sys.argv[8]
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
    re_iding.rename(firstMesh)

    firstMesh=calFemValue(firstMesh)
    #calculate the srp for the step mesh
    print(f"info    : calculating {step} mesh srp value")
    
    
    pool=multiprocessing.Pool(processes= int(core))
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    for element in firstMesh.GiveJarOfElement().GiveElements():
        point=element.GaussianPoint_coordinate
        id_element_main=element.GiveID()
        p = pool.apply_async(cpuParallel_one_point, args=(firstMesh,point,id_element_main,return_list))

    p.get()
    pool.close()
    pool.join()
    


    final_mat=np.array(return_list)
    
    for i in firstMesh.GiveJarOfElement().GiveElements():
        id=i.GiveID()
        indx=np.where(final_mat[:,0]==id)
        i.srp_value=final_mat[indx[0][0]][3]
    

    
    #ERORR info logger
    maximumError=ERORR_LOGER_write(ErorrFile,step,firstMesh,step)
    #calculate the step mesh error and save it
    print(f"info    : calculating {step} mesh error and save it")
    show_countourError(firstMesh,savePath,f"Error1",f"Error{step}",0,maximumError)
    li_value=[element.fem_value for element in firstMesh.JarOfElement.elements]
    plotMESH(firstMesh,li_value,savePath,f"mesh{step}")
    plotPureMESH(firstMesh,savePath,f"mesh{step}")
    #generate the new mesh
    print(f"info    : generating {step+1} mesh")
    new_mesh=meshGeneration(igsFile,write_pos(firstMesh,scalefactor,ratio_selection,step        ),savePath,step)

    #read the new mesh
    print(f"info    : reading {step+1} mesh")
    step_Elements = JarOfElement()
    step_Nodes = JarOfNodes()
    step_GussianPoints = JarOfGussianPoint()
    stepMesh = Mesh(step_Nodes,step_GussianPoints,step_Elements)
    reader(stepMesh).read(new_mesh)
    #tranfer data from first mesh to step mesh
    print(f"info    : transfering {step} mesh data to {step+1} mesh")
    
    
    # stepMesh=MeshSRP(firstMesh,stepMesh)
    pool=multiprocessing.Pool(processes= int(core))
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    for element in stepMesh.GiveJarOfElement().GiveElements():
        point=element.GaussianPoint_coordinate
        id_element_main=element.GiveID()
        p = pool.apply_async(cpuParallel_one_point, args=(firstMesh,point,id_element_main,return_list))

    p.get()
    pool.close()
    pool.join()

    final_mat=np.array(return_list)
    
    for i in stepMesh.GiveJarOfElement().GiveElements():
        id=i.GiveID()
        indx=np.where(final_mat[:,0]==id)
        i.srp_value=final_mat[indx[0][0]][3]

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
        
        # stepMesh=MeshSRP(stepMesh,stepMesh)
        
        
        pool=multiprocessing.Pool(processes= int(core))
        manager = multiprocessing.Manager()
        return_list = manager.list()
        jobs = []
        for element in stepMesh.GiveJarOfElement().GiveElements():
            point=element.GaussianPoint_coordinate
            id_element_main=element.GiveID()
            p = pool.apply_async(cpuParallel_one_point, args=(stepMesh,point,id_element_main,return_list))

        p.get()
        pool.close()
        pool.join()
        


        final_mat=np.array(return_list)
        
  
        for i in stepMesh.GiveJarOfElement().GiveElements():
            id=i.GiveID()
            indx=np.where(final_mat[:,0]==id)
            i.srp_value=final_mat[indx[0][0]][3]

            
        #calculate the steper mesh error and save it
        print(f"info    : calculating {step} mesh error and save it")
        show_countourError(stepMesh,savePath,f"Error{step}",f"Error{step}",0,maximumError)
        li_value=[element.fem_value for element in stepMesh.JarOfElement.elements]
        plotMESH(stepMesh,li_value,savePath,f"mesh{step}")
        plotPureMESH(stepMesh,savePath,f"mesh{step}")
        #ERORR info logger
        maximumError=ERORR_LOGER_write(ErorrFile,step,stepMesh,step)
        #generate the new mesh
        print(f"info    : generating {step+1} mesh")
        old_mesh=copy.deepcopy(stepMesh)
        new_mesh=meshGeneration(igsFile,write_pos(firstMesh,scalefactor,ratio_selection,step        ),savePath,step)

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

        # stepMesh=MeshSRP(firstMesh,stepMesh)
        
        
        
        
                
        pool=multiprocessing.Pool(processes= int(core))
        manager = multiprocessing.Manager()
        return_list = manager.list()
        jobs = []
        for element in stepMesh.GiveJarOfElement().GiveElements():
            point=element.GaussianPoint_coordinate
            id_element_main=element.GiveID()
            p = pool.apply_async(cpuParallel_one_point, args=(firstMesh,point,id_element_main,return_list))

        p.get()
        pool.close()
        pool.join()
        


        final_mat=np.array(return_list)
        

        for i in stepMesh.GiveJarOfElement().GiveElements():
            id=i.GiveID()
            indx=np.where(final_mat[:,0]==id)
            i.srp_value=final_mat[indx[0][0]][3]

    
        
        #write the step mesh srp value
        print(f"info    : writing {step+1} mesh srp value")
        Write_csvfile(stepMesh,savePath)
    plotPureMESH(stepMesh,savePath,f"mesh{step+1}")
    reader(stepMesh).read(fr"{savePath}/final_mat.csv")
    stepMesh=calFemValue(stepMesh)
    #calculate the srp for the steper mesh
    print(f"info    : calculating {step+1} mesh srp value")
    
    # stepMesh=MeshSRP(stepMesh,stepMesh)
    

    pool=multiprocessing.Pool(processes= int(core))
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    for element in stepMesh.GiveJarOfElement().GiveElements():
        point=element.GaussianPoint_coordinate
        id_element_main=element.GiveID()
        p = pool.apply_async(cpuParallel_one_point, args=(stepMesh,point,id_element_main,return_list))

    p.get()
    pool.close()
    pool.join()



    final_mat=np.array(return_list)

    for i in stepMesh.GiveJarOfElement().GiveElements():
        id=i.GiveID()
        indx=np.where(final_mat[:,0]==id)
        i.srp_value=final_mat[indx[0][0]][3]

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #calculate the steper mesh error and save it
    print(f"info    : calculating {step+1} mesh error and save it")
    show_countourError(stepMesh,savePath,f"Error{step+1}.png",f"Error{step+1}",0,maximumError)
    li_value=[element.fem_value for element in stepMesh.JarOfElement.elements]
    plotMESH(stepMesh,li_value,savePath,f"mesh{step+1}")
    #ERORR info logger
    maximumError=ERORR_LOGER_write(ErorrFile,step,stepMesh,step)
    
    
    #_______________________________________________________________________________________________________________________________________________________________________#
    
    
    time_end = time.time()
    print(f"info    : total time is {time_end-time_start}")
