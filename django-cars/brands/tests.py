from django.test import TestCase
from .models import *
# Create your tests here.
class Tests(TestCase):
    def test_01(self):
        b=Brand(name="a totally real company")
        b.full_clean()
        b.save()
        return False