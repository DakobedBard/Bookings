from datetime import date, timedelta

def date_range_list(startdate, enddate):
    '''
    Returns a list of days between startdate and endate
    :param startdate:
    :param enddate:
    :return:
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    delta = enddate - startdate  # as timedelta
    days = []
    for i in range(delta.days + 1):
        days.append(startdate + timedelta(days=i))
    return days

startdate = date(2020, 4, 1)  # start date
enddate = date(2020, 4, 5)  # end date

