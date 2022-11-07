import datetime as dt

dates = [
    ('2022-11-01', '2022-11-15'),
    ('2022-12-05',),
    ('2023-12-10',)
]


def check_dates(current_start_date, current_finish_date):
    for date in dates:
        if len(date) == 1:
            start_date = finish_date = dt.date.fromisoformat(date[0])
        else:
            start_date, finish_date = map(dt.date.fromisoformat, date)
        if not (current_finish_date < start_date or current_start_date > finish_date):
            return "Busy"
    else:
        return "Available"
