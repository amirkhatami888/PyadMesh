# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import numpy as np
import math
import pandas as pd
import warnings
import sys
import copy
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
from Plot_Error import show_countourError
from Write_logError import ERORR_LOGER_init,ERORR_LOGER_write
from plot_Gradient import plotMESH

import time

def tranferPoint(csvFile,inpFile,X,Y):
    
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)

    #read first mesh 
    print(f"info    : reading first mesh")

    first_Nodes = JarOfNodes()
    first_GussianPoints = JarOfGussianPoint()
    first_Elements = JarOfElement()
    firstMesh = Mesh(first_Nodes,first_GussianPoints,first_Elements)

    reader(firstMesh).read(inpFile)
    reader(firstMesh).read(csvFile)

    firstMesh=calFemValue(firstMesh)
    re_iding.rename(firstMesh)

    

    #tranfer data from first mesh to step mesh
    print(f"info    : transfering ")
    result=one_point(firstMesh,[float(X),float(Y)])
    print("result:",result)


if __name__ == "__main__":
    time_start = time.time()
    csvFile=sys.argv[1]
    inpFile=sys.argv[2]
    x=sys.argv[3]
    y=sys.argv[4]

    
    tranferPoint(csvFile,inpFile,x,y)
    time_end = time.time()
    print(f"time    : {time_end-time_start} s")
print("####################done####################")
