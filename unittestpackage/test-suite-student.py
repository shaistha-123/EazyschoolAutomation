import unittest
import capybara
from unittestpackage.test_add_student import studentcase
from unittestpackage.test_activate_student import activatestudent
from unittestpackage.test_inactive_student import inactivatestudent

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(studentcase)
tc2 = unittest.TestLoader().loadTestsFromTestCase(activatestudent)
tc3 = unittest.TestLoader().loadTestsFromTestCase(inactivatestudent)

# Create a test suite combining TestClass1 and TestClass2
sanity_check = unittest.TestSuite([tc1,tc2,tc3])

#Invoke the run
unittest.TextTestRunner(verbosity=2).run(sanity_check)
