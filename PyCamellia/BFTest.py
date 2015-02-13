from Function import *
import BF
import unittest
import Var
import VarFactory
import LinearTerm
import PoissonFormulation
import StokesVGPFormulation
import Function
import Solution
import Mesh
import MeshFactory

varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("fieldVar")
testVar1 = varFac.testVar("testVar",3)
testVar2 = varFac.testVar("testVar2",3)
lttestVars = testVar1 + testVar2
testFlux = varFac.fluxVar("testFlux")
testFluxID = testFlux.ID()
bf = BF.BF_bf(varFac)
spaceDim = 2
function1 = Function.Function_xn()
ltTrial =  function1 * fieldVar
useConformingTraces  = True
poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
stokesForm = StokesVGPFormulation.StokesVGPFormulation(spaceDim, useConformingTraces)
stokesBF = stokesForm.bf()
poissonBF = poissonForm.bf()

u1 = stokesForm.u(1) # VarPtr for x component of velocity
p = stokesForm.p()   # VarPtr for pressure

phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued



class BFTest(unittest.TestCase):
  """Test something"""
  def testBFCtor(self):
    testBF = BF.BF_bf(varFac)
    
  def testIsFluxOrTrace(self):
    self.assertTrue(bf.isFluxOrTrace(testFluxID))

  def testAddTerm(self):
    bf.addTerm(LT,LT)
    bf.addTerm(u1,LT)
    bf.addTerm(phi,psi)
    bf.addTerm(LT,p)
 # def testGraphNorm(self):
   # IPPtr = bf.graphNorm()
    
# Run the tests:
if (__name__ == '__main__'):
  unittest.main()

