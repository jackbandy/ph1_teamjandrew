import IP
import LinearTerm
import VarFactory
import unittest
import Solution
import MeshFactory
import Mesh
import BF
import Function
from SpatialFilter import *


varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("fieldVar")
testVar = varFac.testVar("testVar",3)
testLT = LinearTerm.LinearTerm()
testFlux = varFac.fluxVar("testFlux")

allSpace = SpatialFilter.allSpace()
allSpace.matchesPoint([1.0,1.0])

spaceDim = 2
useConformingTraces  = True
poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
stokesForm = StokesVGPFormulation.StokesVGPFormulation(spaceDim, useConformingTraces)

testIP = IP.IP()
testIP.addTerm(testVar)
stokesForm.u(1) # VarPtr for x component of velocity
p = stokesForm.p()   # VarPtr for pressure

phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued

class IPTest(unittest.TestCase):
  """Test something"""
  #def testadd(self):
    #self.assertAlmostEqual(8,Adder.addNumbers(5,3),delta=1e-12)
    #self.assertEqual(8,Adder.addNumbers(5,3))
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


