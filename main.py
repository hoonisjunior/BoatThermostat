import time as time #might be needed for timing of certain things
from datetime import datetime, date #used to assertain current time and date
import os

import gpiozero #handles all hardware events and pin controls

from pynput import keyboard #used for testing and utlising the keyboard as simulated buttons

current_date = None #initialises current date and time variables
current_time = None

#button = gpiozero.Button(7) #Assigns main button to Pin 7 WILL NEED CHANGING WHEN HARDWARE ASSEMBLED
while True:
	last_date = current_date
	last_time = current_time

	current_date_time = datetime.now()
	current_date = (current_date_time.day, current_date_time.month, current_date_time.year)
	current_time = (current_date_time.hour, current_date_time.minute, current_date_time.second)

	if current_date != last_date or current_time != last_time:
#		print(f'The date today is {current_date[0]}/{current_date[1]}/{current_date[2]} and the current time is {current_time[0]}:{current_time[1]}:{current_time[2]}') Simple formatting of date and current_time
		print_date = current_date_time.strftime('%A the %d of %B, %Y')
		print_time = current_date_time.strftime('%I:%M:%S %p') # formats the date and times into a nice format (Day the DD of Month, YYYY) (HH:MM:SS AM/PM)
#		print(f'The date today is {current_date_time.strftime('%A the %d of %M, %Y')} and it is currently {current_date_time.strftime('%I:%M:%S%p')}')
		print(f'The date today is {print_date} and the current time is {print_time}')