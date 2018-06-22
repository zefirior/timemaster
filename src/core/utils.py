from config import MINUTE


def int_2_time_attr(timeint):
    minute = timeint // MINUTE
    second = timeint - minute * MINUTE
    return minute, second


def time_attr_2_int(minute, second):
    return minute * MINUTE + second


