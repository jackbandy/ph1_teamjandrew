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

class MeshFactoryTest(unittest.TestCase):
  """Test something"""
  #def testadd(self):
    #self.assertAlmostEqual(8,Adder.addNumbers(5,3),delta=1e-12)
    #self.assertEqual(8,Adder.addNumbers(5,3))
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


