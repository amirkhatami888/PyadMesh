import numpy as np 

def write_plt_tecplot(path,fileName,X_li,Y_li,Value_li,index_li):
    """this function is used to write plt tecplot file
    Args:
        path (str): the path
        fileName (str): the name of the file
        X_li (list): list of x
        Y_li (list): list of y
        Value_li (list): list of values
        index_li (list): list of index
    """
    ntri=len(index_li)
    npoint=len(X_li)
    li_file=[]
    li_file.append(f"TITLE = \"{fileName}\"\n")
    li_file.append("VARIABLES = \"X\", \"Y\", \"Value\"\n")
    li_file.append(f"ZONE N={npoint}, E={ntri}, F=FEPOINT, ET=TRIANGLE\n")
    for i in range(npoint):
        li_file.append(f"{X_li[i]} {Y_li[i]} {Value_li[i]}\n")
    for i in range(ntri):
        li_file.append(f"{index_li[i][0]} {index_li[i][1]} {index_li[i][2]}\n")
    file=open(path,'w')
    file.writelines(li_file)
    file.close()