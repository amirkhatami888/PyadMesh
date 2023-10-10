# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from math import sqrt


        
def write_pos(Mesh,scalefactor,ratio_selection,step ):
    li_value=[]
    for element in Mesh.JarOfElement.elements:
        temp=element.srp_value
        if temp==0:
            temp=1e-7
        else:
            temp=abs(temp)
        li_value.append(temp)
    
    
    li_value=np.array(li_value)
    li_value=li_value**2
    li_value=1/(li_value)

    ratio_value=np.quantile(li_value,ratio_selection)

    
    for i in range(len(li_value)):
        if li_value[i]<ratio_value:
            li_value[i]=li_value[i]*scalefactor/step
        else:
            li_value[i]=li_value[i]*scalefactor




    
    
    

    
   

    
    li_points=Mesh.JarOfElement.ToMatrixWithCoordinates()
    li_points=np.array(li_points)
    li_value=np.round(li_value,4)
    lowest_value_not_zero=min(li_value[np.nonzero(li_value)])
    li_value=[lowest_value_not_zero if i==0 else i for i in li_value]
    li_value=np.array(li_value).reshape(-1,1).repeat(3,axis=1).reshape(-1,3)
    
    file=open("posfile.pos","w")
    li=[]
    li.append('View "background mesh" {\n')
    for i in range(len(li_value)):
        temp="ST("+str(li_points[i][1])+","+str(li_points[i][2])+","+"0"+","+\
                   str(li_points[i][3])+","+str(li_points[i][4])+","+"0"+","+\
                   str(li_points[i][5])+","+str(li_points[i][6])+","+"0"+"){"+\
                   str(li_value [i][0])+","+str(li_value [i][1])+","+str(li_value [i][2])+"};\n"
        li.append(temp)
    li.append('};\n')
    file.writelines(li)
    file.close()
    return "posfile.pos"