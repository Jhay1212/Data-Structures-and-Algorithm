import unittest
import permutation

class TestPermutation(unittest.TestCase):
    def test_equal(self, msg = None):
     self.assertEqual(permutation([1, 2, 3]), [[1, 2], [1, 3], [2, 1], [2, 3]])
     self.assertEqual(permutation([10, 20, 30, 40, 50]), [[10, 20], [10, 30], [10, 40], [10, 50], [20, 10], 
                                                          [20, 30], [20, 40], [20, 50], [30, 10], [30, 20], [30, 40], [30, 50], [40, 10],
                                                            [40, 20], [40, 30], [40, 50], [50, 10], [50, 20], [50, 30], [50, 40]])
    
    
if __name__ == '__main__':
    unittest.main()
    