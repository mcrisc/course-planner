# coding: utf-8

import calendar
from datetime import date, timedelta


DAYS_OF_CLASS = {
    calendar.TUESDAY: 4,
    calendar.FRIDAY: 2,
}
TOTAL_CLASSES = 120

START_DATE = date(2015, 7, 30)
END_DATE = date(2015, 12, 21)
HOLIDAYS = {
    '2015-08-22',
    '2015-09-05',
    '2015-09-07',
    '2015-10-12',
    '2015-10-15',
    '2015-10-16',
    '2015-10-17',
    '2015-11-02',
    '2015-11-15',
    '2015-11-20',
    '2015-11-21'
    }


ONE_DAY = timedelta(days=1)
WEEK_DAYS = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']


def main():
    d = START_DATE
    # week gets 1 if any class occurs in the first week, or 0 otherwise
    week = 1 if max(DAYS_OF_CLASS.keys()) >= START_DATE.weekday() else 0
    possible_classes = 0
    week_turn = min(DAYS_OF_CLASS.keys())
    while d <= END_DATE and possible_classes < TOTAL_CLASSES:
        if d.weekday() == week_turn:
            week += 1
        if d.weekday() in DAYS_OF_CLASS:
            holiday = d.isoformat() in HOLIDAYS
            classes = 0 if holiday else DAYS_OF_CLASS[d.weekday()]
            possible_classes += classes
            print('%3d\t%s\t%s\t%2s\t%s' % (
                week, d, WEEK_DAYS[d.weekday()],
                '' if holiday else classes,
                '*' if holiday else ''))
        d = d + ONE_DAY
    print()
    print('Total de aulas:', possible_classes)
    print('Reposições:', TOTAL_CLASSES, '-', possible_classes, '=',
          TOTAL_CLASSES - possible_classes)


if __name__ == '__main__':
    main()
