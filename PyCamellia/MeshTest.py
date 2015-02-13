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

numelements = 2
varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("f")
testVar = varFac.testVar("t", Var.HGRAD)
bf = BF.BF_bf(varFac)
vecd = MeshFactory.vectord(numelements,1.5)
veci = MeshFactory.vectori(numelements,1)
mesh = MeshFactory.MeshFactory_rectilinearMesh(bf,vecd,veci,2)

class MeshTest(unittest.TestCase):
  """Test something"""
  def testCellPolyOrder(self):
    print("Order of first cell: %i" % mesh.cellPolyOrder(1))
    self.assertEqual(2, mesh.cellPolyOrder(0))

  def testActiveCellID(self):
    activebefore = mesh.getActiveCellIDs()
    print ("number of elements before refine: %i" % len(activebefore))
    mesh.hRefine([0])
    activeafter = mesh.getActiveCellIDs()
    print ("number of elements after refine: %i" % len(activeafter))
    self.assertGreater(len(activeafter),len(activebefore))

  def testgetDimension(self):
    self.assertEqual(numelements, mesh.getDimension())
    print("Active elements: %i" % mesh.getDimension())

  #def testhRefine(self):

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


