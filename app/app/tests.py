from django.test import TestCase

from app.calc import add, sub

class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(5,7),12)

    def test_sub_numbers(self):
        self.assertEqual(sub(3,8),5 )
