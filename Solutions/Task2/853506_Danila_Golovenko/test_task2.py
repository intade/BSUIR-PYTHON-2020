import unittest
import task2

class TestJson(unittest.TestCase):

    def test_list(self): 
        a = task2.MyJson()
        l = [5, 6, [45,65], True, False, None, {"sdf": 34}]
        self.assertTrue(a.to_json(l) == "[ 5, 6, [ 45, 65 ], true, false, none, { 'sdf':34 } ]")

    def test_dict(self):
        a = task2.MyJson()
        d = {5 : "afsd", 54 : 'wqe'}
        self.assertTrue(a.to_json(d) == "{ '5':'afsd', '54':'wqe' }")

    def test_list_from_json(self):
        a = task2.MyJson()
        t = [2,3,10, True, "asdf"]
        self.assertListEqual(t, a.from_json(a.to_json(t)))

    def test_dict_from_json(self):
        a = task2.MyJson()
        t = {'32' : "fasd", "fs" : "43"} 
        self.assertDictEqual(t, a.from_json(a.to_json(t)))   