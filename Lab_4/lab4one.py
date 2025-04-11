from datetime import datetime, timedelta
date=datetime.now()
new_date=date-timedelta(months=5)
print("5 дней назад:", new_date)