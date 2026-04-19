import random
import time
def random_date(start_date,end_date):
    print("printing random date between", start_date, "and", end_date)
    random_generator=random.random()
    date_format="%M/%d/%Y"
    start_time=time.mktime(time.strptime(start_date,date_format))
    end_time=time.mktime(time.strptime(end_date,date_format))
    random_time=start_time+random_generator*(end_time-start_time)
    random_date=time.strftime(date_format,time.localtime(random_time))
    return random_date
print("Random date =", random_date("11/2/2016" , "11/2/2017"))