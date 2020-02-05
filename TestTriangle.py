# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
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
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(9.4567853,9.4567853,9.4567853),'InvalidInput 3','9.4567853,9.4567853,9.4567853 should be InvalidInput 3')

    def testNotATriangleTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 should be scalene')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be isoceles')

    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be isoceles')

    def testInvalidTrianglesA(self): 
        self.assertEqual(classifyTriangle(3,2,0),'InvalidInput 2','3,2,0 should be InvalidInput 2')

    def testInvalidTrianglesB(self): 
        self.assertEqual(classifyTriangle(3,2,300),'InvalidInput 1','3,2,300 should be InvalidInput 1')

    def testInvalidTrianglesC(self): 
        self.assertEqual(classifyTriangle(-2,3,4),'InvalidInput 2','-2,3,4 should be InvalidInput 2')

    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(10,7,15),'Scalene','10,7,15 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

