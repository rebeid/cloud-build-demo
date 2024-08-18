import unittest

target = __import__("app")

class TestApp(unittest.TestCase):
    def test_say_something(self):
        """
        Test that method returns text enclosed by <h1></h1> tags
        """
        text = "good morning"
        actual = target.say_something(text)
        expected = "<h1>\\(^o^)/ %s!</h1>" % text
        self.assertEqual(actual, expected)    

if __name__ == '__main__':
    unittest.main()