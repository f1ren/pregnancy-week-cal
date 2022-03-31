from unittest import TestCase

from datetime import date
from cal import get_week
from dateutil.parser import parse


class Test(TestCase):
    def test_get_week_sample_1(self):
        # Setup
        GIVEN_WEEK, GIVEN_DAY = (13, 1)
        GIVEN_DATE = parse('2022-03-31').date()

        # Case
        at_date = date(2022, 3, 31)
        expected_week = [13, 1]

        self.assertEqual(get_week(at_date, GIVEN_DATE, GIVEN_WEEK, GIVEN_DAY), expected_week)
