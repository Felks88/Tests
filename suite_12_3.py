import unittest
import tests_12_3

runnerTS = unittest.TestSuite()
runnerTS.addTests(unittest.TestLoader().loadTestsFromModule(tests_12_3))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTS)
