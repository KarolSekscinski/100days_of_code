
# fun to calculate stock market yesterday
def yesterday(weekday, date_list):
    if weekday == 0:
        date_list[2] = str(int(date_list[2]) - 3)
    elif weekday == 6:
        date_list[2] = str(int(date_list[2]) - 2)
    else:
        date_list[2] = str(int(date_list[2]) - 1)
    return "".join(item for item in date_list)


def day_before_yesterday(weekday, date_list):
    if weekday == 1:
        date_list[2] = str(int(date_list[2]) - 5)
    elif weekday == 0:
        date_list[2] = str(int(date_list[2]) - 4)
    elif weekday == 6:
        date_list[2] = str(int(date_list[2]) - 3)
    else:
        date_list[2] = str(int(date_list[2]) - 2)
    return "".join(item for item in date_list)
