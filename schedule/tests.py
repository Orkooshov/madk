from django.test import TestCase
from .models import Classroom


class ClassroomTests(TestCase):
    def test_str(self):
        classroom = Classroom(number=1, floor=2, building=3)
        self.assertEqual(str(classroom), '3.2.1')