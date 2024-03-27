from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))
