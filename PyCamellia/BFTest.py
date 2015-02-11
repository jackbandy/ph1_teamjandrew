import BF
import unittest
import Var
import VarFactory
import LinearTerm


#varFac = VarFactory.VarFactory()
#fieldVar = varFac.fieldVar("fieldVar")
#testVar1 = varFac.testVar("testVar",3)
#testVar2 = varFac.testVar("testVar2",3)
#LT = testVar1 + testVar2
#testFlux = varFac.fluxVar("testFlux")
#testBF = BF.BF(varFac)
#testFluxID = testFlux.ID()

import PoissonFormulation
import StokesVGPFormulation
spaceDim = 2
useConformingTraces  = True
poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
stokesForm = StokesVGPFormulation.StokesVGPFormulation(spaceDim, useConformingTraces)
stokesBF = stokesForm.bf()
poissonBF = poissonForm.bf()

u1 = stokesForm.u(1) # VarPtr for x component of velocity
p = stokesForm.p()   # VarPtr for pressure

phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued

LT = phi + psi

class BFTest(unittest.TestCase):
  """Test something"""
  def testadd(self):
    #self.assertAlmostEqual(8,Adder.addNumbers(5,3),delta=1e-12)
    #self.assertEqual(8,Adder.addNumbers(5,3))
    self.assertTrue(testBF.isFluxOrTrace(testfluxID))

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()

