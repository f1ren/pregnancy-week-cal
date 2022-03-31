import os
from datetime import date

from dateutil import relativedelta
from dateutil.parser import parse
import calendar
import webbrowser

GIVEN_WEEK, GIVEN_DAY = (13, 1)
GIVEN_DATE = parse('2022-03-31').date()

# TODO: Substruct GIVEN_WEEK
FIRST_DATE = GIVEN_DATE


def get_week(at_date):
    date_diff = at_date - GIVEN_DATE
    days = date_diff.days
    return [(days + 1) // 7 + GIVEN_WEEK, (days + GIVEN_DAY) % 7]


class MyCalendar(calendar.HTMLCalendar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.year = None
        self.month = None

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        else:
            w, d = get_week(date(self.year, self.month, day))
            details = f'{w},{d}'
            if w >= 0:
                return '<td class="%s"><font size=3><b>%d</b></font><br/><font size=2>%s</font></td>' % (
                    self.cssclasses[weekday], day, details)
            else:
                return '<td class="%s"><font size=3><b>%d</b></font><br/><font size=2>&nbsp;</font></td></td>' % (
                    self.cssclasses[weekday], day)


t = '''<style>
body {
    font-family: 'arial';
}
table {
    display: inline-block;
    float: left;
    height: 15rem;
    padding-right: 1rem;
}
th {
    width: 10%;
}
td {
    text-align: center;
}
</style>'''

current_month = FIRST_DATE
MAX_MONTHS = 11


def next_month(x):
    return x + relativedelta.relativedelta(months=1)


def get_html_for_month(current_month):
    c = MyCalendar(calendar.SUNDAY)
    y = current_month.year
    m = current_month.month
    c.year = y
    c.month = m
    return f'{c.formatmonth(y, m)}'


for i in range(MAX_MONTHS - (GIVEN_WEEK // 4)):
    t += get_html_for_month(current_month)
    current_month = next_month(current_month)

html_path = 'cal.html'
open(html_path, 'w').write(t)
webbrowser.open('file://' + os.path.realpath(html_path))
