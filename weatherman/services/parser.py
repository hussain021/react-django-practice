import os

from model.monthly_data import MonthlyData
from model.yearly_data import YearlyData
from exceptions.input_exception import InputError


class Parser:
    """Reads data from file and and returns them as objects of Monthly and Yearly"""
    def __init__(self):
        os.environ['WEATHERFILES']= os.getcwd()+'/weatherfiles/'

    def get_months_of_year(self, year):
        """Returns the name of files of a specific year in form of a list

            checks for the year in the name files and then adds it to the
            list and returns it.
        """
        list_of_files = os.listdir(os.environ['WEATHERFILES'])
        months = []
        check_if_year_exists = False
        for file in list_of_files:
            if file.__contains__(year):
                months.append(file)
                check_if_year_exists = True

        if check_if_year_exists:
            return months

        raise InputError(year, 'Year not found in the list of files!')

    def get_month(self, year, month):
        """Returns the data of a single month in the form of the MonthlyData class
            by calling the get_monthly_data function

            First it finds the file from the list of 12 files of the passed year by
            calling get_months_of_year function and then calls the get_monthly_data
            to return the data in model form.
        """
        months = self.get_months_of_year(year)
        for single_month in months:
            if single_month.__contains__(month):
                return self.get_monthly_data(single_month)

    def get_year(self, year):
        """Returns the data of the entire year by calling get_yearly_data function"""
        months = self.get_months_of_year(year)
        return self.get_yearly_data(months)

    def get_monthly_data(self, name):
        """ the data of a single month in form of the MonthlyData model

            The function reads the data from the name of the file passed to it
            and then passes it into the function to create an object of model
        """
        name_split = name.split('_')
        month = name_split[3]
        month = month[:3]
        with open(os.environ['WEATHERFILES'] + '/'+ name) as file:
            file.readline() # To discard the metadata
            all_data = file.readlines()

        highest_total = 0
        lowest_total = 0
        humidity_total = 0
        lowest_list = []
        highest_list = []
        highest_humidity_list = []
        days = 0
        for day_data in all_data:
            if day_data == '':
                break

            list_data = day_data.split(",")
            if(list_data[1] == '' and list_data[3] == '' and\
                list_data[7] == '' and list_data[8] == ''):
                # list_data[1] is for max temperature, list_data[3] is for min temperature
                # list_data[8] is for max humidity, as all there are required so,
                # if we do not have this data, exit the loop.
                break

            max_temp = int(list_data[1])
            min_temp = int(list_data[3])
            max_humidity = int(list_data[7])
            highest_list.append(max_temp)
            lowest_list.append(min_temp)
            highest_humidity_list.append(max_humidity)
            highest_total += max_temp
            lowest_total += min_temp
            humidity_total += int(list_data[8])
            days = days + 1

        return MonthlyData(highest_list, lowest_list, highest_humidity_list, highest_total/days,
            lowest_total/days, humidity_total/days, month)

    def get_yearly_data(self, month_names):
        """Returns the data of 12 months in the form of an object of YearlyData

            Calls the get_monthly_data function 12 times and append it into a 
            list of 12 MonthlyData objects.
        """
        months = []
        for month in month_names:
            months.append(self.get_monthly_data(month))

        return YearlyData(months)
