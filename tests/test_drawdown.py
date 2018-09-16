from com.a_labs.drawdown import DrawDownCalculator
import unittest

"""
    __author__ = "Nidhi Kushwah"
    __date   : 16-09-2018
    __copyright__ = "Copyright 2007, The AL Assignment"
    __license__ = "Free Usage"
    __version__ = "1.0.0"
    __maintainer__ = "Nidhi Kushwah"
    __email__ = "nidhikushwah_it@rediffmail.com"
    __status__ = "Production"
"""

class TestDrawDown(unittest.TestCase):

    def setUp(self):
        self.calc = DrawDownCalculator()

    def test_drawdown(self):
        arr1 = [3, 2, 1, 5, 2, 7, 3, 10]
        val = self.calc.find_drawdown(arr1, 2)
        self.assertEqual([4,3], val)

        arr2 = [1, 2, 3, 4, 5, 4, 3, 4, 3, 4, 5, 6, 7, 4, 3, 6, 2, 10]
        val = self.calc.find_drawdown(arr2, 2)
        self.assertEqual([5, 2], val)

        arr3 = [1, 2, 3, 4, 5, 7]
        val = self.calc.find_drawdown(arr3, 3)
        self.assertEqual(val, [0])

if __name__ == '__main__':
    unittest.main()