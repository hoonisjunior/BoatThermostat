import time as time
from datetime import datetime, date
import os


while True:
	current_date_time = datetime.now()
	current_date = (current_date_time.day, current_date_time.month, current_date_time.year)
	current_time = (current_date_time.hour, current_date_time.minute, current_date_time.second)

	print(f'The date today is {current_date[0]}/{current_date[1]}/{current_date[2]} and the current time is {current_time[0]}:{current_time[1]}:{current_time[2]}')
	time.sleep(1)