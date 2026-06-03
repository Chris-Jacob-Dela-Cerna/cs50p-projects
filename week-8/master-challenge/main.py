

import datetime as dt


birth_date = dt.date(2008, 5, 2)
today = dt.date.today()
age = today - birth_date
days = dt.timedelta(days=6606)
minutes = days.total_seconds() / 60

print(minutes)