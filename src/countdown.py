import datetime

now = "EEEEEUUUUU, I think this is a bug, you shoudn't see this, well please consider reporting is, or no, i don't really care"

def delta_time():
    now = datetime.datetime.now()
    format = "%d : %m : %H : %M : %S"
    ny = "31 : 12 : 23 : 59 : 59"
    datetime.datetime.now().strftime(format)
    return now