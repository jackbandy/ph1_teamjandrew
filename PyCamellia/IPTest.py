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
    print "created instance testIP"
  def addVarTermOK(self):
    testIP.addTerm(testVar)
    print "added varPtr term to testIP"
  def addLinTermOK(self):
    #testIP.addTerm(testVar)
    print "added"
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()


