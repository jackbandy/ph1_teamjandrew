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
  #def testHDF5(self):
  def testCellPolyOrder(self):
    print("Order of first cell: %i" % mesh.cellPolyOrder(1))
    self.assertEqual(2, mesh.cellPolyOrder(0))

  def testActiveCellID(self):
    self.assertNotEqual(0, len(mesh.getActiveCellIDs()))

  def testgetDimension(self):
    self.assertEqual(numelements, mesh.getDimension())
    print("Active elements: %i" % mesh.getDimension())

  def testhRefine(self):
    activebefore = mesh.getActiveCellIDs()
    print ("number of elements before refine: %i" % len(activebefore))
    mesh.hRefine([0])
    activeafter = mesh.getActiveCellIDs()
    print ("number of elements after refine: %i" % len(activeafter))
    self.assertGreater(len(activeafter),len(activebefore))

  def testDofCount(self):
    fl = mesh.numFluxDofs()
    fi = mesh.numFieldDofs()
    gl = mesh.numGlobalDofs()
    self.assertEqual(gl, (fl+fi))
    print ("Total dofs: %i" % gl)

  def testpRefine(self):
    before = mesh.cellPolyOrder(0)
    print ("before refine: %i" % before)
    mesh.pRefine([0])
    after = mesh.cellPolyOrder(0)
    print ("after refine: %i" % after)
    self.assertGreater(after,(before+1))

  #def testRegister(self):

  #def testVertices(self):


# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


