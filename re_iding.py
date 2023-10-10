
def rename(mesh):
    couter=1
    for element in mesh.GiveJarOfElement().GiveElements():
        element.id=couter
        couter+=1
    couter=1
    for node in mesh.GiveJarOfNodes().GiveNodes():
        node.id=couter
        couter+=1
        
