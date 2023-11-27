# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import gmsh
import os
def meshGeneration(igsFile,posfile,savePath,step,meshAlgorithm=5):
    """this function generate mesh for igs file and pos file

    Args:
        igsFile (str): path to igs file
        posfile (str): path to pos file
        MIN (float ):minimum mesh size

    Returns:
        str : name of mesh file
    """
    gmsh.initialize()
    gmsh.merge(posfile)
    gmsh.merge(igsFile)
    # Add the post-processing view as a new size field:
    bg_field = gmsh.model.mesh.field.add("PostView")
    gmsh.model.mesh.field.setNumber(bg_field, "ViewIndex", 0)
    gmsh.model.mesh.field.setAsBackgroundMesh(bg_field)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary",60)
    gmsh.option.setNumber("Mesh.MeshSizeFromPoints",        60)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature",     0)




    print()
    gmsh.option.setNumber("Mesh.Algorithm",meshAlgorithm)
 



    # gmsh.model.mesh.optimize("Relocate2D")
    # gmsh.model.mesh.optimize("Netgen")
    gmsh.model.mesh.generate(2)
    name=f"refinement_{step}.dat"
    name2=f"refinement_{step}.inp"
    gmsh.write(os.path.join(savePath,name))
    gmsh.write(os.path.join(savePath,name2))
    # gmsh.fltk.run()
    gmsh.finalize()
    return os.path.join(savePath,name)