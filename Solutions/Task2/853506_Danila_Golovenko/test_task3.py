import unittest
import task3

class TestVector(unittest.TestCase):
    def setUp(self):
        self.a = task3.Vector(2,3,4,5,6)        
        self.c = task3.Vector(3,4)
    
    def test_main_operations(self):
        self.assertListEqual(task3.Vector.sum(self.a, self.a).coordinates, [4,6,8,10,12])
        self.assertListEqual(task3.Vector.sub(self.a, self.a).coordinates, [0,0,0,0,0])
        self.assertAlmostEqual(task3.Vector.length(self.c), 5) 
        self.assertAlmostEqual(self.a.getItemAt(3), 5)
        self.assertListEqual(task3.Vector.mul(self.c, 5).coordinates, [15,20])
        self.assertAlmostEqual(task3.Vector.scalMul(self.a,self.a), 90)
        self.assertTrue(task3.Vector.comp(self.a,self.a))
    
    def test_error(self):
        self.assertRaises(ValueError, task3.Vector.sum, self.a, self.c)
        self.assertRaises(ValueError, task3.Vector.sub, self.a,self.c)