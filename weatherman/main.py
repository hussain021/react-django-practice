import argparse

from services.service import Service
from constants.constants import MONTHS


def main():
    """ Main program """
    service = Service()
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str)
    parser.add_argument('-a', type=str)
    parser.add_argument('-c', type=str)
    args = parser.parse_args()

    if not (args.a or args.e or args.c):
        print('No arguments found!')
        return

    if args.c and len(args.c) >= 5:
        month_and_year = get_year_and_month(args.c)
        service.get_detailed_month(month_and_year['year'], month_and_year['month'])

    if args.e and len(args.e) == 4:
        service.get_yearly_data(str(args.e))

    if args.a and len(args.a) >= 5:
        month_and_year = get_year_and_month(args.a)
        service.get_month_average(month_and_year['year'], month_and_year['month'])

    return 0


def get_year_and_month(argument):
    """Returns the year and month in form of a dict

        Splits a single argument containing year and month and returns
        2 arguments with one being the year and other being month in
        3 character form.
    """
    splitter = argument.split('/')
    year_and_month = {}
    year_and_month['year'] = splitter[0]
    month_with_zero_adjusted = int(splitter[1])
    year_and_month['month'] = MONTHS[str(month_with_zero_adjusted)]
    return year_and_month


if __name__ == "__main__":
    main()
