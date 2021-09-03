

class MonthlyData:
    """Stores data of a month"""

    def __init__(
        self,
        highest_list,
        lowest_list,
        highest_humidity_list,
        highest_average,
        lowest_average,
        humidity_average,
        month_name,
    ):
        """init function for the MonthlyData class

        Receives data for a month and stores it.
        """
        self.month_name = month_name
        self.highest_list = highest_list
        self.lowest_list = lowest_list
        self.highest_average = int(highest_average)
        self.lowest_average = int(lowest_average)
        self.highest_humidity_average = int(humidity_average)
        self.monthly_highest = max(highest_list)
        self.monthly_highest_date = highest_list.index(self.monthly_highest) + 1
        self.monthly_lowest = min(lowest_list)
        self.monthly_lowest_date = lowest_list.index(self.monthly_lowest) + 1
        self.monthly_highest_humidity = max(highest_humidity_list)
        self.monthly_highest_humidity_date = highest_humidity_list.index(
                                            self.monthly_highest_humidity
                                            ) + 1
