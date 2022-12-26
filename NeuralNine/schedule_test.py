import schedule
from schedule import every, repeat

import time as tm
from datetime import time, timedelta, datetime


# def job():
#     print('Check your laundry!')

# schedule.every(5).seconds.do(job)
# schedule.every(.1).minutes.do(job)
# schedule.every().day.at('18:53').do(job)
# schedule.every().monday.at('18:54').do(job)
# schedule.every().minute.at(':30').do(job)
# schedule.every(10).seconds.until(time(19, 9, 50)).do(job)
# schedule.every(10).seconds.until(timedelta(minutes=2)).do(job)
# schedule.every(1).to(5).seconds.do(job) #random interval


# j = schedule.every(1).to(5).seconds.do(job)


# @repeat(every(5).seconds)
# def job():
#     """
#     way to shedule tasks with a decorator
#     """
#     print('Check your laundry!')@repeat(every(5).seconds)

@repeat(every(5).seconds, message='falochron')
@repeat(every(2).seconds, message='pożarnictwo')
def job(message):
    """
    multipiple triggers with different parametrs injected to the function
    """
    print('Check your laundry! The key word is:', message)

# schedule.every(5).seconds.do(job, message='katastrofa budowlana')

if __name__ == '__main__':

    # counter = 0

    while True:
        schedule.run_pending()
        tm.sleep(1)
        # counter += 1
        #
        # if counter == 10:
        #     schedule.cancel_job(j)
