from unittest import TestCase
import sample

class TestSample(TestCase):

    def test_say_hello(self):
        self.assertEqual(sample.say_hello(), "Hello")
        self.assertNotEqual(sample.say_hello(), "hello")