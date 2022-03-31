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

HTML_PATH = 'cal.html'


def get_week(at_date, given_date=GIVEN_DATE, given_week=GIVEN_WEEK, given_day=GIVEN_DAY):
    date_diff = at_date - given_date
    days = date_diff.days
    return [(days + 1) // 7 + given_week, (days + given_day) % 7]


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


HTML_HEADER = '''<style>
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


def build_html():
    t = HTML_HEADER[:]
    current_month = FIRST_DATE
    for i in range(MAX_MONTHS - (GIVEN_WEEK // 4)):
        t += get_html_for_month(current_month)
        current_month = next_month(current_month)
    return t


if __name__ == '__main__':
    code = build_html()
    open(HTML_PATH, 'w').write(code)
    webbrowser.open('file://' + os.path.realpath(HTML_PATH))
