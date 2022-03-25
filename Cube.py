import unittest

def volumeofcube(x):
    return (x*x*x)

class CheckDivisible(unittest.TestCase):

    def test_case_divisble(self):
            x=5.555
            result = volumeofcube(x)
            self.assertAlmostEqual(result, x*x*x)

if __name__ == "__main__":
    unittest.main()

