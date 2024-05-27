# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import pandas as pd
import warnings
import sys
import copy
import os
import multiprocessing
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
from Func_parallel_calPointSRP import gpuParallel_one_point
from Func_parallel_calFemValue import calFemValue
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from Write_posfile import write_pos
from Func_GSH_meshGeneration import meshGeneration
from Write_csvfile import Write_csvfile
from Plot_Error import show_countourError
from Write_logError import ERORR_LOGER_init,ERORR_LOGER_write
from plot_Gradient import plotMESH
import re_iding
import time



if __name__ == "__main__":
    time_start = time.time()
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)
    csvFile=sys.argv[1]
    inpFile=sys.argv[2]
    datFile=sys.argv[3]
    savePath=sys.argv[4]
    thread_x=sys.argv[5]
    thread_y=sys.argv[6]
    core=sys.argv[7]
    error_thereshold=float(sys.argv[8])
    
    
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)

    #read first mesh 
    print(f"info    : reading first mesh")

    first_Nodes = JarOfNodes()
    first_GussianPoints = JarOfGussianPoint()
    first_Elements = JarOfElement()
    firstMesh = Mesh(first_Nodes,first_GussianPoints,first_Elements)

    reader(firstMesh,error_thereshold).read(inpFile)
    reader(firstMesh,error_thereshold).read(csvFile)

    firstMesh=calFemValue(firstMesh)
    
    #read the second mesh
    print(f"info    : reading second mesh")
    second_Elements = JarOfElement()
    second_Nodes = JarOfNodes()
    second_GussianPoints = JarOfGussianPoint()
    secondMesh = Mesh(second_Nodes,second_GussianPoints,second_Elements)
    reader(secondMesh,error_thereshold).read(datFile)
    
    re_iding.rename(firstMesh)
    re_iding.rename(secondMesh)

    
    
    #tranfer data from first mesh to step mesh
    
    print(f"info    : transfering first mesh data to second mesh")
    pool=multiprocessing.Pool(processes= int(core))
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    for element in secondMesh.GiveJarOfElement().GiveElements():
        point=element.GaussianPoint_coordinate
        id_element_main=element.GiveID()
        p = pool.apply_async(gpuParallel_one_point, args=(firstMesh,point,id_element_main,return_list))
        
    p.get()
    pool.close()
    pool.join()
    


    final_mat=np.array(return_list)
    final_mat=pd.DataFrame(final_mat)
    final_mat=final_mat.sort_values(by=0,ascending=True).values


    np.savetxt(os.path.join(savePath, 'final_mat.csv'),final_mat,delimiter=',')
    
    
    print(f"info    : plotting first mesh")
    li_value=[]
    for element in firstMesh.JarOfElement.elements:
        li_value.append(element.fem_value)
    plotMESH(firstMesh,li_value,savePath,"-firstMesh")
    print(f"info    : plotting second mesh")
    li_value=final_mat[:,3]
    li_value=li_value.flatten().tolist()

    plotMESH(secondMesh,li_value,savePath,"-secondMesh")
 

    time_end = time.time()
    print(f"info    : time cost {time_end-time_start}s")
    print("####################done####################")
    
    
    
    
    
