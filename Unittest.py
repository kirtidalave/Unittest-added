import unittest
from distutils.command.check import check
from unittest import result

class EvenorOddApp(unittest.TestCase):
   def test_case_even_check(self):
       x=10
       reult = check(x)
       self.assertEqual("even",result)

       def test_case_odd_check(self):
           x = 15
           result = check(x)
           self.assertEqual("odd",result)

if __name__ == "__main__":
    unittest.main()