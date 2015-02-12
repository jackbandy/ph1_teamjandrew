import PoissonFormulation
import StokesVGPFormulation
import Var
import Solution
import BF
import Function
from SpatialFilter import *
import Mesh
import MeshFactory
import VarFactory
import unittest

class MeshTest(unittest.TestCase):
  """Test something"""
  def testCellPolyOrder(self):
    varFac = VarFactory.VarFactory()
    fieldVar = varFac.fieldVar("f")
    testVar = varFac.testVar("t", Var.HGRAD)
    bf = BF.BF_bf(varFac)
    vecd = MeshFactory.vectord(2,1.5)
    veci = MeshFactory.vectori(2,1)
    mesh = MeshFactory.MeshFactory_rectilinearMesh(bf,vecd,veci,2)
    print("Mesh has %i active elements" % mesh.getDimension())

  #def testActiveCellID(self):
  #def testgetDimension(self):
  #def testhRefine(self):

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


