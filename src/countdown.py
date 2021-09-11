import datetime

now = datetime.datetime.now()

NY = datetime.datetime(2022, month=1, day=1)

format = "%d : %m : %H : %M : %S"


def delta_time():
    now = datetime.datetime.now()
    datetime.datetime.now().strftime(format)
    return str(now)

def remain_time():
    now = datetime.datetime.now()

    time_until_ny = NY - now

    return str(time_until_ny).split(".")[0]