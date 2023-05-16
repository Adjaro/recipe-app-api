from django.test import SimpleTestCase

from app import calc


class CalcsTest(SimpleTestCase):
    def test_add_number(self):
        res = calc.add(3, 2)
        self.assertEqual(res, 5)
