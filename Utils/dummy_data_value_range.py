import itertools
import random
import time


def str_time_prop(start, end, time_format, prop):
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))
    random_date = start_time + prop * (end_time - start_time)
    return time.strftime(time_format, time.localtime(random_date))


class ValueRange:
    def __init__(self, desired_col_size):
        self.desired_col_size = desired_col_size

    def get_name_value_list(self, list_of_first_name, list_of_middle_name, list_of_last_name):
        names = [list_of_first_name, list_of_middle_name, list_of_last_name]
        val = []
        for name in list(itertools.product(*names))[:self.desired_col_size]:
            val.append(name[0] + " " + name[1] + " " + name[2])
        return val

    def get_string_value_list(self, list_of_strings):
        val = []
        for i in range(self.desired_col_size):
            val.append(list_of_strings[random.randint(0, len(list_of_strings)-1)])
        return val

    def get_date_value_range(self, from_date, to_date):
        val = []
        for i in range(self.desired_col_size):
            val.append(str_time_prop(from_date, to_date, "%d-%m-%Y %H:%M:%S", random.random()))
        return val

    def get_int_value_range(self, lowest, highest):
        return random.sample(range(lowest, highest), self.desired_col_size)

    def get_int_seq_range(self, start):
        return list(range(start, start + self.desired_col_size + 1))

    def get_enum_range(self, value_list):
        val = []
        for i in range(self.desired_col_size):
            val.append(value_list[random.randint(0, len(value_list) - 1)])
        return val
