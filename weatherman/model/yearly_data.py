from constants.constants import MONTH_FULL_NAMES


class YearlyData:
    """Stores Yearly data"""
    def __init__(self, months):
        """init function for the YearlyData class

            Receives a list of months and then finds the highest and lowest
            temperature and highest humidity and stores their data for later use
        """
        self.lowest = {'value':float('inf'), 'date':0, 'month':'Aug'}
        self.highest = {'value':float('-inf'), 'date':0, 'month':'Aug'}
        self.highest_humidity = {'value':0,'date':0, 'month':'Aug'}
        for month in months:
            if month.monthly_lowest < self.lowest['value']:
                self.lowest['value'] = month.monthly_lowest
                self.lowest['date'] = month.monthly_lowest_date
                self.lowest['month'] = MONTH_FULL_NAMES[month.month_name]

            if month.monthly_highest > self.highest['value']:
                self.highest['value'] = month.monthly_highest
                self.highest['date'] = month.monthly_highest_date
                self.highest['month'] = MONTH_FULL_NAMES[month.month_name]

            if month.monthly_highest_humidity > self.highest_humidity['value']:
                self.highest_humidity['value'] = month.monthly_highest_humidity
                self.highest_humidity['date'] = month.monthly_highest_humidity_date
                self.highest_humidity['month'] = MONTH_FULL_NAMES[month.month_name]
