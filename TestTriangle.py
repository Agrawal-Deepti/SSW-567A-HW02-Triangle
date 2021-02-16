# -*- coding: utf-8 -*-
"""
Updated Feb 16, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: dagrawa2
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a equilateral')

    def testNotEquilateralTriangles(self): 
        self.assertNotEqual(classifyTriangle(3,1,2),'Equilateral','3,1,2 is not a equilateral')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(1.0,2.0,3.0), 'InvalidInput', '1.0,2.0,3.0  is a InvalidInput') #to test input is instance of integer

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(0, 1, 0), 'InvalidInput', '0, 1, 0  is a InvalidInput')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2, 3, 4 is a Scalene triangle') 

    def testNotAScaleneTriangle(self):
        self.assertNotEqual(classifyTriangle(2, 1, 2), 'Scalene', '2, 1, 2 is not a Scalene triangle') 

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isoceles', '2, 2, 1 is a Isoceles triangle') 

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(2, 1, 2), 'Isoceles', '2, 1, 2 is a Isoceles triangle') 

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isoceles', '1, 2, 2 is a Isoceles triangle') 

    def testNotAIsocelesTriangle(self):
        self.assertNotEqual(classifyTriangle(1, 2, 3), 'Isoceles', '1, 2, 2 is not a Isoceles triangle') 

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1, 10, 12 is not a triangle') 
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

