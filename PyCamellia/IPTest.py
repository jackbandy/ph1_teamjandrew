import IP
import LinearTerm
import VarFactory
import unittest
import Solution
import MeshFactory
import Mesh
import BF
import Function
import PoissonFormulation
import StokesVGPFormulation
from SpatialFilter import *


varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("fieldVar")
testVar = varFac.testVar("testVar",3)
testLT = LinearTerm.LinearTerm()
testFlux = varFac.fluxVar("testFlux")


spaceDim = 2
useConformingTraces  = True
poissonForm = PoissonFormulation.PoissonFormulation(spaceDim, useConformingTraces)
stokesForm = StokesVGPFormulation.StokesVGPFormulation(spaceDim, useConformingTraces)

#testIP.addTerm(testVar)
#stokesForm.u(1) # VarPtr for x component of velocity
#p = stokesForm.p()   # VarPtr for pressure

#phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
#psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued

class IPTest(unittest.TestCase):
  """Basic Test case"""
  def constructorOK(self):
    testIP = IP.IP()

  def addVarTermOK(self):
    testIP.addTerm(testVar)

  def addLinTermOK(self):
    testIP.addTerm(testVar)
  
  def evaluateOK(self):
    testmap1 = IP.map_int_FunctionPtr({fieldVar.ID(): Function.Function_xn(2)})
    testmap2 = LinearTerm.map_int_FunctionPtr({fieldVar.ID(): Function.Function_xn(2)})
    lntrm = testIP.evaluate(testmap1)
    res = lntrm.evaluate(testmap2)
    #also possible to use l2norm?

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


