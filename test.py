import unittest
import HelloWorld
# import Stophur

class TestStringMethods(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(HelloWorld.hello_world(), "Hello, World!")

    def test_timesthree(self):
        self.assertEqual(HelloWorld.times_three(3), 9)

    def test_cubed(self):
        self.assertEqual(HelloWorld.cube(3), 27)

    def test_square(self):   
        self.assertEqual(HelloWorld.square(3), 9)

    def test_buildtriangle(self):
        self.assertEqual(HelloWorld.half_pyramid(5), 
                         ["#", "##", "###", "####", "#####"])

    def test_findsymbol(self):
        self.assertEqual(HelloWorld.find_symbol("BTC/WS"), 332)
        self.assertFalse(HelloWorld.find_symbol("Tacos"))

    def test_count_char(self):
        self.assertEqual(HelloWorld.count_char(";"), 4)


if __name__ == '__main__':
    unittest.main()