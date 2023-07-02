import locale
from datetime import datetime


locale.setlocale(locale.LC_ALL, 'zh_CN.utf8')
current_time = datetime.now()
hour = str(current_time.hour)
minute = str(current_time.minute)
weekday = current_time.strftime("%A")
print(weekday)