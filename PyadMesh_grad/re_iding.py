# author: amirhossein khatami
# mail: amirkhatami@gmail.com

def rename(mesh):
    """this function rename id of nodes and elements"""
    couter=1
    for element in mesh.GiveJarOfElement().GiveElements():
        element.id=couter
        couter+=1
    couter=1
    for node in mesh.GiveJarOfNodes().GiveNodes():
        node.id=couter
        couter+=1
        
