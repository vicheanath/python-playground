
import unittest

from selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([5,3,6,2,10]), [2,3,5,6,10])
        self.assertEqual(selection_sort([5,3,6,2,10,1]), [1,2,3,5,6,10])
        
    def test_selection_sort_with_negative_numbers(self):
        self.assertEqual(selection_sort([5,3,6,2,10,-1]), [-1,2,3,5,6,10])
        self.assertEqual(selection_sort([5,3,6,2,10,-1,-3]), [-3,-1,2,3,5,6,10])
        
    def test_selection_sort_with_repeated_numbers(self):
        self.assertEqual(selection_sort([5,3,6,2,10,1,5]), [1,2,3,5,5,6,10])
        self.assertEqual(selection_sort([5,3,6,2,10,1,5,3]), [1,2,3,3,5,5,6,10])
        
    def test_selection_sort_with_empty_array(self):
        self.assertEqual(selection_sort([]), [])
        
    def test_selection_sort_with_one_element(self):
        self.assertEqual(selection_sort([5]), [5])
        self.assertEqual(selection_sort([-5]), [-5])
        
    def test_selection_sort_with_two_elements(self):
        self.assertEqual(selection_sort([5,3]), [3,5])
        self.assertEqual(selection_sort([5,-3]), [-3,5])
        self.assertEqual(selection_sort([-5,-3]), [-5,-3])
        
        
if __name__ == '__main__':
    
    unittest.main()