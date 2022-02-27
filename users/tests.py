from django.test import TestCase
from .models import Lifter
from django.utils import timezone
from datetime import date


class BirthdayTestCase(TestCase):
    def setUp(self):
        Lifter.objects.create(username="sus", email="sus@gaming.com", date_of_birth='2005-2-27')


    def test_age_from_date_of_birth(self):
        sus = Lifter.objects.get(username='sus')
        today = date.today()
        
        # If the condition is true, subtract one to age.
        print(today.year - sus.date_of_birth.year - ((today.month, today.day) < (sus.date_of_birth.month, sus.date_of_birth.day)))
