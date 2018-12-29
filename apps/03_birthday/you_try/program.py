import datetime


def header():
    print('*' * 20)
    print('   B-Day Checker')
    print('*' * 20)


def user_bday():
    year = int(input('What year [YYYY]?'))
    month = int(input('What month [MM]?'))
    day = int(input('What day [DD]?'))
    bday = datetime.date(year, month, day)
    return bday


def bday_delta(bday, target_date):
    this_year = datetime.date(target_date.year, bday.month, bday.day)
    days = this_year - target_date
    return days.days


def check_logic(delt):
    if delt < 0:
        print('Your birthday was {} days ago.'.format(-delt))
    elif delt > 0:
        print('Your birthday is in {} days.'.format(delt))
    else:
        print('Go, its your birthday!')


def main():
    header()
    bday = user_bday()
    today = datetime.date.today()
    days = bday_delta(bday, today)
    check_logic(days)


main()
