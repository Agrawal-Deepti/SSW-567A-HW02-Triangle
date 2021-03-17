# -*- coding: utf-8 -*-
"""
Updated Feb 16, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: dagrawa2
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    '''Test cases to test triangle module'''

    def test_right_triangle_side_a(self):
        '''Test case for right angle triangle side a.'''
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_triangle_side_b(self):
        '''Test case for right angle triangle side b.'''
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_right_triangle_side_c(self):
        '''Test case for right angle triangle side c.'''
        self.assertEqual(classify_triangle(4,3,5),'Right','4,3,5 is a Right triangle')

    def test_equilateral_triangles(self):
        '''Test case for equilateral triangle'''
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 is a equilateral')

    def test_not_equilateral_triangles(self):
        '''Test case for not equilateral triangle'''
        self.assertNotEqual(classify_triangle(3,1,2),'Equilateral','3,1,2 is not a equilateral')

    def test_invalid_input(self):
        '''Test case for invlid input, to test input is instance of integer'''
        self.assertEqual(classify_triangle(1.0,2.0,3.0), 'InvalidInput',
        '1.0,2.0,3.0  is a InvalidInput')

    def test_invalid_input_1(self):
        '''Test case for invlid input 1'''
        self.assertEqual(classify_triangle(0, 1, 0), 'InvalidInput', '0, 1, 0  is a InvalidInput')

    def test_scalene_triangle(self):
        '''Test case for scalene triangle'''
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene', '2, 3, 4 is a Scalene triangle')

    def test_not_a_scalene_triangle(self):
        '''Test case for not a scalene triangle'''
        self.assertNotEqual(classify_triangle(2, 1, 2), 'Scalene',
        '2, 1, 2 is not a Scalene triangle')

    def test_isoceles_triangle_a(self):
        '''Test case for isoceles triangle side a'''
        self.assertEqual(classify_triangle(2, 2, 1), 'Isoceles', '2, 2, 1 is a Isoceles triangle')

    def test_isoceles_triangle_b(self):
        '''Test case for isoceles triangle side b'''
        self.assertEqual(classify_triangle(2, 1, 2), 'Isoceles', '2, 1, 2 is a Isoceles triangle')

    def test_isoceles_triangle_c(self):
        '''Test case for isoceles triangle side c'''
        self.assertEqual(classify_triangle(1, 2, 2), 'Isoceles', '1, 2, 2 is a Isoceles triangle')

    def test_not_a_isoceles_triangle(self):
        '''Test case for not a isoceles triangle'''
        self.assertNotEqual(classify_triangle(1, 2, 3), 'Isoceles',
        '1, 2, 2 is not a Isoceles triangle')

    def test_not_a_triangle(self):
        '''Test case for not a triangle'''
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle',
        '1, 10, 12 is not a triangle')

    def test_invalid_input_2(self):
        '''Test case for isoceles triangle side c'''
        self.assertEqual(classify_triangle(500, 500, 100), 'InvalidInput',
        '500,500,100 is a InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
