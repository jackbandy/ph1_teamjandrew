import MeshFactory
import unittest
import Mesh
import VarFactory
import Var
import BF

varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("f")
testVar = varFac.testVar("t", Var.HGRAD)
bf = BF.BF_bf(varFac)
vecd = MeshFactory.vectord(2,1.5)
veci = MeshFactory.vectori(2,1)
mesh = MeshFactory.MeshFactory_rectilinearMesh(bf,vecd,veci,2) 

print("Before refinement, mesh has %i active elements" % mesh.numActiveElements())

mesh.hRefine([0])

print("After refinement, mesh has %i active elements" % mesh.numActiveElements())
numGlobalDofsBefore = mesh.numGlobalDofs();
numElementsBefore = mesh.numElements();

mesh.saveToHDF5("Mesh.HDF5")
meshLoad = MeshFactory.MeshFactory_loadFromHDF5(bf,"Mesh.HDF5")


numGlobalDofsAfter = meshLoad.numGlobalDofs();
numElementsAfter = meshLoad.numElements();

class MeshFactoryTest(unittest.TestCase):
  """Test something"""
  def testadd(self):
    #Tests to see if loadFromHDF5 works (assuming the saveToHDF5 works)
    self.assertEqual(numGlobalDofsBefore,numGlobalDofsAfter)
    self.assertEqual(numElementsBefore,numElementsAfter)
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


