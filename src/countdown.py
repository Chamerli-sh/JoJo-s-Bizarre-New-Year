import datetime


format = "%d : %m : %H : %M : %S"

now = datetime.datetime.now()




NY = datetime.datetime(2022, month=1, day=1)
BTD_OP = datetime.datetime(2021, month=9, day=12, hour=16, minute=12, second=16)



def delta_time():
    now = datetime.datetime.now().strftime(format)
    return str(now).split(".")[0]

def remain_time():
    now = datetime.datetime.now()

    time_until_ny = NY - now
    

    return str(time_until_ny).split(".")[0]