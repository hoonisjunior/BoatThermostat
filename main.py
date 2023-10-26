import time as time #might be needed for timing of certain things
from datetime import datetime, date, time, timedelta #used to assertain current time and date
import os

#import gpiozero #handles all hardware events and pin controls

from pynput import keyboard #used for testing and utlising the keyboard as simulated buttons

current_date = None #initialises current date and time variables
current_time = None

timer_value = 5 #THIS VARIABLE CONTROLS HOW LONG A TIMER TO BE SET (PER PRESS) IN SECONDS

press_times = {} #initialises dicts to track when keys pressed or released (to check how long they have been held)
release_times = {}

timer_time = datetime.min #initialises the timer time to minimum possible time (as this can be treated as null in later logic)
current_date_time = datetime.now() #initialises curent datetime

#button = gpiozero.Button(7) #Assigns main button to Pin 7 WILL NEED CHANGING WHEN HARDWARE ASSEMBLED
def on_press(key):
	global current_date_time
	global press_times
	try:
		print(f' key {key.char} pressed') #testing lines to print when keys pressed and released
		#press_times[key.char].append(current_date_time)
	except AttributeError:
		print(f' s key {key} pressed')
		#if key == key.space:
		#	press_times['space'].append(current_date_time)
		#else:
		#  	pass

def on_release(key): #function for use with pynput, when space pressed adds 5 minutes to the provided time
	global timer_time #uses lots of naughty global variables
	global current_date_time
	global release_times
	global timer_value
	try:
		#release_times[key.char].append(current_date_time) #adds the time that current key was released to the correct dictionary
		if key == key.space: 
			#print('wow spacebar got pressed')
			timer_time = current_date_time + timedelta(seconds = timer_value) #uses a timedelta object to calculate when the timer will go off
			print(f'The timer is NOW set for {timer_time.time()}')
			#print(timer_time.time())
		else:
			pass
	except AttributeError:
		pass

listener = keyboard.Listener( #defines the keyboard listener to use the previous on_press and
	on_press=on_press,
    on_release=on_release)

listener.start() #starts the keyboard listener  

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
		if timer_time <= current_date_time and timer_time != datetime.min:#checks if current time has exceeded the timer
	 		print('YEEEEE FUCKING HAW TIMER TIME BOIS')
	 		timer_time = datetime.min
		else:
			pass
	except TypeError:
		pass