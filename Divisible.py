import unittest

def checkDivisibleby7(x):
    if x%7 ==0:
        return True
    else:
        return False


class CheckDivisible(unittest.TestCase):

    def test_case_divisble(self):
            x=14
            result = checkDivisibleby7(x)
            self.Assertrue(result)

    def test_case_divisble1(self):
                x=9
                result = checkDivisibleby7(x)
                self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

