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
    File.write("step,stepSize,max_Error,min_Error,mean_Error,std_Error\n")
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
    li_ERORR=[element.Error for element in mesh.GiveJarOfElement().elements]
    File=open(file,"a")
    File.write(f"{step},{stepSize},{np.max(li_ERORR)},{np.min(li_ERORR)},{np.mean(li_ERORR)},{np.std(li_ERORR)}\n")    
    File.close()
    return np.max(li_ERORR)
