

import datetime as dt
import inflect


birth_date = dt.date(2008, 5, 2)
today = dt.date.today()
age = today - birth_date
days = dt.timedelta(days=6606)
minutes = round(days.total_seconds() / 60)

print(minutes)

p = inflect.engine()

print(p.number_to_words(minutes, andword="").capitalize())