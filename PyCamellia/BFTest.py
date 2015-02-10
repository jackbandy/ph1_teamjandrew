import BF
import unittest
import Var
import VarFactory
import LinearTerm


varFac = VarFactory.VarFactory()
fieldVar = varFac.fieldVar("fieldVar")
testVar = varFac.testVar("testVar",3)
testLT = LinearTerm.LinearTerm()
testFlux = varFac.fluxVar("testFlux")
testBF = BF.BF(varFac)
testFluxID = testFlux.ID()


class BFTest(unittest.TestCase):
  """Test something"""
  def testadd(self):
    #self.assertAlmostEqual(8,Adder.addNumbers(5,3),delta=1e-12)
    #self.assertEqual(8,Adder.addNumbers(5,3))
    self.assertTrue(testBF.isFluxOrTrace(testfluxID))

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()

