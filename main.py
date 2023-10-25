import time as time #might be needed for timing of certain things
from datetime import datetime, date, time, timedelta #used to assertain current time and date
import os

#import gpiozero #handles all hardware events and pin controls

from pynput import keyboard #used for testing and utlising the keyboard as simulated buttons

current_date = None #initialises current date and time variables
current_time = None

timer_time = datetime.min
current_date_time = datetime.now()

#button = gpiozero.Button(7) #Assigns main button to Pin 7 WILL NEED CHANGING WHEN HARDWARE ASSEMBLED

def on_release(key): #functiuon for use with pynput, when space pressed adds 5 minutes to the provided time
	global timer_time
	global current_date_time
	try:
		if key == key.space:
			#print('wow spacebar got pressed')
			timer_time = current_date_time + timedelta(seconds = 3)
			print(f'The timer is NOW set for {timer_time.time()}')
			#print(timer_time.time())
		else:
			pass
	except AttributeError:
		pass

listener = keyboard.Listener( # starts the keyboard listener to detect keypresses
    on_release=on_release)
listener.start()   

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
		if timer_time == datetime.min:
			print('Currently not a timer set')
		else:
			print(f'The timer is set for {timer_time.time()}\n')
	try:
		if timer_time <= current_date_time and timer_time != datetime.min:
	 		print('YEEEEE FUCKING HAW TIMER TIME BOIS')
	 		timer_time = datetime.min
		else:
			pass
	except TypeError:
		pass