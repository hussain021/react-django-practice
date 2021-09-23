from services.parser import Parser


class Service:
    """Creates an object of parser and calls its functions"""
    def __init__(self):
        self.parser = Parser()

    def get_yearly_data(self, year):
        """ Does not return anything

            Gets data of 12 months from the parser in the form of yearly data and then prints the
            highest and lowest temperature along with highest humidity with
            details about on which day it occured.
        """
        yearly = self.parser.get_year(year)
        print('Highest: ' + str(yearly.highest['value']) + 'C on ' + 
                yearly.highest['month'] + ' ' + str(yearly.highest['date']))
        print('Lowest: ' + str(yearly.lowest['value']) + 'C on ' + 
                yearly.lowest['month'] + ' ' + str(yearly.lowest['date']))
        print('Humidity: ' + str(yearly.highest_humidity['value']) + '% on ' + 
                yearly.highest_humidity['month'] + ' ' + str(yearly.highest_humidity['date']))

    def get_month_average(self, year, month):
        """ Does not return anything

            Gets data of a single month by sending the year and month to the
            parser and then prints highest, lowest and mean humidity average
        """
        month = self.parser.get_month(year, month)
        print('Highest Average: ' + str(month.highest_average) + 'C')
        print('Lowest Average: ' + str(month.lowest_average) + 'C')
        print('Average Mean Humidity: ' + str(month.highest_humidity_average) + '%')

    def get_detailed_month(self, year, month):
        """ Does not return anything

            Gets data of a single month by sending the year and month to the
            parser and then prints highest and lowest temperature for each
            day with highest in red color and lowest in blue color
        """
        month = self.parser.get_month(year, month)
        for index in range(len(month.highest_list)):
            print('\033[1;31;40m' + str(index + 1), end=' ')
            for inner_loop in range(month.highest_list[index]):
                print("+", end='')

            print(' ' + str(month.highest_list[index]))
            print('\033[1;34;40m' + str(index + 1), end=' ')
            for inner_loop in range(month.lowest_list[index]):
                print("+", end='')

            print(' ' + str(month.lowest_list[index]))
            print('\033[1;37;40m' + '', end='')
