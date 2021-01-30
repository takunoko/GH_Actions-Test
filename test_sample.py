from unittest import TestCase
import sample

class TestSample(TestCase):

    def test_say_hello(self):
        self.assertEqual(sample.say_hello(), "Hello")
        self.assertNotEqual(sample.say_hello(), "hello")


    def test_say_world(self):
        self.assertEqual(sample.say_world(), "World")
        self.assertNotEqual(sample.say_world(), "world")
        self.assertNotEqual(sample.say_world(), "hello")
