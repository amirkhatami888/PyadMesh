# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import pandas as pd
import warnings
import sys
import copy
import multiprocessing 
import os
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
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from Write_csvfile import Write_csvfile
from Func_searse_calTransferDisp import calTransferDisplacement_point_parallel
import pandas as pd
import time
import re_iding
import Func_parallel_U_cal as U_cal
import Plot_dispU1
import Plot_dispU2

if __name__ == "__main__":
    time_start = time.time()
    csvFile=sys.argv[1]
    inpFile=sys.argv[2]
    datFile=sys.argv[3]
    savePath=sys.argv[4]
    core=sys.argv[5]

    
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)

    #read first mesh 
    print(f"info    : reading first mesh")

    first_Nodes = JarOfNodes()
    first_GussianPoints = JarOfGussianPoint()
    first_Elements = JarOfElement()
    firstMesh = Mesh(first_Nodes,first_GussianPoints,first_Elements)

    reader(firstMesh).read(inpFile)
    reader(firstMesh).read(csvFile)
    re_iding.rename(firstMesh)
    
    #read the second mesh
    print(f"info    : reading second mesh")
    second_Elements = JarOfElement()
    second_Nodes = JarOfNodes()
    second_GussianPoints = JarOfGussianPoint()
    secondMesh = Mesh(second_Nodes,second_GussianPoints,second_Elements)
    reader(secondMesh).read(datFile)
    re_iding.rename(secondMesh)
    
    
    #tranfer data from first mesh to step mesh
    print(f"info    : transfering first mesh data to second mesh")
    pool=multiprocessing.Pool(processes= int(core))
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    for node in secondMesh.GiveJarOfNodes().nodes:
        point=[node.x,node.y]
        node_id=node.id
        p = pool.apply_async(calTransferDisplacement_point_parallel, args=(firstMesh,point,node_id,return_list))

    p.get()
    pool.close()
    pool.join()
    


    final_mat=np.array(return_list)
    final_mat=pd.DataFrame(final_mat)
    final_mat=final_mat.sort_values(by=0,ascending=True).values
    for i in range(len(final_mat)):
        id=final_mat[i,0]
        node=secondMesh.GiveJarOfNodes().GiveNodeWithID(id)
        node.U1=final_mat[i,3]
        node.U2=final_mat[i,4]
    Write_csvfile(secondMesh,savePath)
    Plot_dispU1.save_countourDisplacement(firstMesh, savePath,"firstDispU1","first mesh dispalacement U1")
    Plot_dispU1.save_countourDisplacement(secondMesh, savePath,"secondDispU1","second mesh dispalacement U1")
    Plot_dispU2.save_countourDisplacement(firstMesh, savePath,"firstDispU2","first mesh dispalacement U2")
    Plot_dispU2.save_countourDisplacement(secondMesh, savePath,"secondDispU2","second mesh dispalacement U2")
        
 
    time_end = time.time()
    print(f"info    : total time is {time_end-time_start}")
    print("####################done####################")
