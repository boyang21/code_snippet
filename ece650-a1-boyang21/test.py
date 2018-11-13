## A simple unit test example. Replace by your own tests

import unittest

from a1ece650 import *

class MyTest(unittest.TestCase):

    def test_upper(self):
        """Test the upper() function of class string"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Test isupper() function of class string"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_cmd_paser(self):
        line1 = 'a "weber" 1, 2 ,3, 4 ,5 ,6'
        line2 = 'a "weber" (1, 2 (3, 4) (5 ,6)'
        line3 = 'a "weber Street" (1,2)(3,4) (5,6)\n'
        with self.assertRaises(Exception):
            cmd_paser(line1)
        with self.assertRaises(Exception):
            cmd_paser(line2)
        self.assertEqual(cmd_parser(line3), ('a', 'weber Street', 
                                            '(1,2)(3,4) (5,6)'))

    def test_street_db(self):
        coords = ( (1, 2), (3, 4), (5, 6) )
        seg1 = line( point(1, 2), point(3, 4) )
        seg2 = line( point(3, 4), point(5, 6) )
        st_name = 'weber'
        # test add
        db = street_db()
        db.add(st_name, coords)
        self.assertTrue(len(db.get_segs(st_name)) == 2) 
        self.assertTrue( db.get_segs(st_name)[0] == (seg1))
        self.assertTrue( db.get_segs(st_name)[1] == (seg2))

        # test chg
        coords_new = ( (1, 2), (2, 2), (5, 6) )
        seg1_new = line( point(1, 2), point(2, 2) )
        seg2_new = line( point(2, 2), point(5, 6) )
        db.chg(st_name, coords_new)
        self.assertTrue(len(db.get_segs(st_name)) == 2) 
        self.assertTrue( db.get_segs(st_name)[0] == (seg1_new))
        self.assertTrue( db.get_segs(st_name)[1] == (seg2_new))

        # test rm
        db.rm(st_name)
        with self.assertRaises(Exception):
            db.rm(st_name)
        with self.assertRaises(Exception):
            db.chg(st_name, coords)

    
    def test_coords_str2tuple(self):
        coords_str1 = '(1,2)(3,4) (5,6)'
        self.assertEqual(coords_str2tuple(coords_str1), 
                         ((1, 2), (3, 4), (5, 6)))

    def test_intersect(self):
        # case1 
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(0, 3)
        pt4 = point(3, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l1, l2)[0]  ==  point(0, 3) and \
                          intersect(l1, l2)[1]  ==  point(1, 3))  or  \
                         (intersect(l1, l2)[0]  ==  point(1, 3) and \
                          intersect(l1, l2)[1]  ==  point(0, 3)) )

        # case2 
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(0, 3)
        pt4 = point(1, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l1, l2)[0]  ==  point(0, 3) and \
                          intersect(l1, l2)[1]  ==  point(1, 3))  or  \
                         (intersect(l1, l2)[0]  ==  point(1, 3) and \
                          intersect(l1, l2)[1]  ==  point(0, 3)) )
        

        # case3
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(0, 3)
        pt4 = point(3, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l2, l1)[0]  ==  point(0, 3) and \
                          intersect(l2, l1)[1]  ==  point(1, 3))  or  \
                         (intersect(l2, l1)[0]  ==  point(1, 3) and \
                          intersect(l2, l1)[1]  ==  point(0, 3)) )

        # case4
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(-1, 3)
        pt4 = point(3, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l2, l1)[0]  ==  point(-1, 3) and \
                          intersect(l2, l1)[1]  ==  point(1, 3))  or  \
                         (intersect(l2, l1)[0]  ==  point(1, 3) and \
                          intersect(l2, l1)[1]  ==  point(-1, 3)) )

        # case5
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(-2, 3)
        pt4 = point(3, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l1, l2)[0]  ==  point(-1, 3) and \
                          intersect(l1, l2)[1]  ==  point(1, 3))  or  \
                         (intersect(l1, l2)[0]  ==  point(1, 3) and \
                          intersect(l1, l2)[1]  ==  point(-1, 3)) )

        # case6
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(3, 3)
        pt4 = point(4, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [] )

        # case7
        pt1 = point(1, 3)
        pt2 = point(-1, 3)
        l1  = line(pt1, pt2)
        pt3 = point(3, 3)
        pt4 = point(4, 3)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l2, l1) == [] )

                         
        # case8
        pt1 = point(3, -1)
        pt2 = point(3, 1)
        l1  = line(pt1, pt2)
        pt3 = point(3, -1)
        pt4 = point(3, 4)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l1, l2)[0]  ==  point(3, -1) and \
                          intersect(l1, l2)[1]  ==  point(3, 1))  or  \
                         (intersect(l1, l2)[0]  ==  point(3, 1) and \
                          intersect(l1, l2)[1]  ==  point(3, -1)) )


        # case9
        pt1 = point(3, -1)
        pt2 = point(3, 1)
        l1  = line(pt1, pt2)
        pt3 = point(3, -1)
        pt4 = point(3, 4)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l2, l1)[0]  ==  point(3, -1) and \
                          intersect(l2, l1)[1]  ==  point(3, 1))  or  \
                         (intersect(l2, l1)[0]  ==  point(3, 1) and \
                          intersect(l2, l1)[1]  ==  point(3, -1)) )

        # case10
        pt1 = point(3, -1)
        pt2 = point(3, 1)
        l1  = line(pt1, pt2)
        pt3 = point(3, -4)
        pt4 = point(3, 4)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l2, l1)[0]  ==  point(3, -1) and \
                          intersect(l2, l1)[1]  ==  point(3, 1))  or  \
                         (intersect(l2, l1)[0]  ==  point(3, 1) and \
                          intersect(l2, l1)[1]  ==  point(3, -1)) )

        # case11
        pt1 = point(3, -1)
        pt2 = point(3, 1)
        l1  = line(pt1, pt2)
        pt3 = point(3, -4)
        pt4 = point(3, 4)
        l2  = line(pt3, pt4)
        self.assertTrue( (intersect(l1, l2)[0]  ==  point(3, -1) and \
                          intersect(l1, l2)[1]  ==  point(3, 1))  or  \
                         (intersect(l1, l2)[0]  ==  point(3, 1) and \
                          intersect(l1, l2)[1]  ==  point(3, -1)) )

        # case12
        pt1 = point(3, -1)
        pt2 = point(3, 1)
        l1  = line(pt1, pt2)
        pt3 = point(3, 4)
        pt4 = point(3, 5)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [] )

        # case13
        pt1 = point(3, -1)
        pt2 = point(3, 1)
        l1  = line(pt1, pt2)
        pt3 = point(3, 4)
        pt4 = point(3, 5)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l2, l1) == [] )

        # case14
        pt1 = point(-3, 0)
        pt2 = point(3, 0)
        l1  = line(pt1, pt2)
        pt3 = point(0, -1)
        pt4 = point(0, 5)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l2, l1) == [ point(0, 0) ] )

        # case15
        pt1 = point(-3, 0)
        pt2 = point(3, 0)
        l1  = line(pt1, pt2)
        pt3 = point(-1, -1)
        pt4 = point(1, 1)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [ point(0, 0) ] )

        # case16
        pt1 = point(-3, 0)
        pt2 = point(3, 0)
        l1  = line(pt1, pt2)
        pt3 = point(1, 1)
        pt4 = point(-1, -1)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [ point(0, 0) ] )

        # case17
        pt1 = point(3, -6)
        pt2 = point(3, 6)
        l1  = line(pt1, pt2)
        pt3 = point(-1, 1)
        pt4 = point(3, 1)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [ point(3, 1) ] )

        # case18
        pt1 = point(3, -6)
        pt2 = point(3, 6)
        l1  = line(pt1, pt2)
        pt3 = point(4, 4)
        pt4 = point(6, -1)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [] )

        # case19
        pt1 = point(-3, -3)
        pt2 = point(3, 3)
        l1  = line(pt1, pt2)
        pt3 = point(-3, 3)
        pt4 = point(3, -3)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [ point(0, 0) ] )

        # case20
        pt1 = point(-3, -3)
        pt2 = point(3, 3)
        l1  = line(pt1, pt2)
        pt3 = point(-3, 3)
        pt4 = point(-2, 2)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l1, l2) == [] )

        # case21
        pt1 = point(-3, -3)
        pt2 = point(3, 3)
        l1  = line(pt1, pt2)
        pt3 = point(-3, 3)
        pt4 = point(-2, 2)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l2, l1) == [] )

        # case22
        pt1 = point(-1, -1)
        pt2 = point(1, 1)
        l1  = line(pt1, pt2)
        pt3 = point(-3, 4)
        pt4 = point(4, -4)
        l2  = line(pt3, pt4)
        self.assertTrue( intersect(l2, l1) == [point(4.0/15, 4.0/15)] )

                         

        
if __name__ == '__main__':
    unittest.main()
