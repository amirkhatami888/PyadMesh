# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np
import os
def ERORR_LOGER_init(path):
    """init the ERORR_LOGER

    Returns:
        str: name of the ERORR_LOGER file
            """
    File=open(os.path.join(path, 'ERORR_LOGER.csv'),"w")
    File.write("step,number of nodes ,number of elements,\
               max Error Relative,min Error Relative,mean Error Relative,std Error Relative,max Error Absolute,min Error Absolute,mean Error Absolute,std Error Absolute\n")
    File.close()
    return os.path.join(path, 'ERORR_LOGER.csv')

def ERORR_LOGER_write(file,step,mesh,stepSize):
    """"
    write the ERORR_LOGER file

    Args:
        file (str): name of the ERORR_LOGER file
        step (int): step number
        mesh (instance of mesh class): the mesh
    """ 
    nu_element=len(mesh.GiveJarOfElement().elements)
    nu_nodes=len(mesh.JarOfNodes.nodes)
    li_ERORR=[element.Error for element in mesh.GiveJarOfElement().elements]
    li_pure_ERORR=[element.Error for element in mesh.GiveJarOfElement().elements]
    li_pureERORR=[element.Error_pure for element in mesh.GiveJarOfElement().elements]
    File=open(file,"a")
    File.write(f"{step},{nu_nodes},{nu_element},\
               {np.max(li_ERORR)},{np.min(li_ERORR)},{np.mean(li_ERORR)},{np.std(li_ERORR)},{np.max(li_pureERORR)},{np.min(li_pureERORR)},{np.mean(li_pureERORR)},{np.std(li_pureERORR)}\n")
    File.close()
    return np.max(li_ERORR),np.max(li_pureERORR)
