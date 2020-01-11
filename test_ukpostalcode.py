import unittest
import ukpostalcode as ukpc

class ukpc_test(unittest.TestCase):
  def __init__(self):
    self.pc = ukpc.ukpc("EC 2M 5TU")

  def isValidTest(self):
    self.assertTrue(self.pc.isValid())
  
  def formatTest(self):
    self.assertEqual(self.pc.format, "EC2M 5TU")
  
  def detailsTest(self):
    self.assertIn('data', self.pc.details)

if __name__ == "__main__":
    unittest.main()