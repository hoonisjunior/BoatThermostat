import time as time #might be needed for timing of certain things
from datetime import datetime, date, time, timedelta #used to assertain current time and date
import os

#import gpiozero #handles all hardware events and pin controls

from pynput import mouse #used for testing and utlising the mouse as simulated buttons

current_date = None #initialises current date and time variables
current_time = None

timer_minutes_value = 0 #These variables control how long to add to the timer per button press
timer_seconds_value = 5 
hold_time = 1 #This is how long constitutes holding the button (to reset the timer) in seconds

press_time = datetime.min
release_time = datetime.min 

timer_time = datetime.min #initialises the timer time to minimum possible time (as this can be treated as null in later logic)
current_date_time = datetime.now() #initialises curent datetime

#button = gpiozero.Button(7) #Assigns main button to Pin 7 WILL NEED CHANGING WHEN HARDWARE ASSEMBLED
def on_click(x,y,button,pressed):
	global current_date_time
	global press_time
	global release_time
	global timer_time

	if pressed: #checks if the mouse button is pressed
		print(f'Mouse button {button} was pressed')
		if button == mouse.Button.left:
			press_time = current_date_time
		else:
			pass

	else: #
		print(f'Mouse button {button} was released')
		if button == mouse.Button.left:
			release_time = current_date_time
			print(f'it was held for {(release_time - press_time).seconds} seconds')
			if (release_time - press_time).seconds >= hold_time:
				timer_time = datetime.min
				print('The timer has been cancelled')
			elif timer_time == datetime.min:
				timer_time = current_date_time + timedelta(minutes = timer_minutes_value, seconds = timer_seconds_value)
			else:
				timer_time = timer_time + timedelta(minutes = timer_minutes_value, seconds = timer_seconds_value)
		else:
			pass

listener = mouse.Listener( #defines the mouse listener to use the on_click function
	on_click=on_click)

listener.start() #starts the mouse listener  

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
		if timer_time > datetime.min:
			print(f'The timer is set for {timer_time.time()} and will be on for {(timer_time - current_date_time).seconds} seconds')
			if timer_time <= current_date_time:
				print('WEEWOOWEEWOOWEEWOO Timer is going off')
				timer_time = datetime.min
		else:
			print('There is no timer set at the moment')



'''
		if timer_time == datetime.min:
			print('Currently not a timer set')
		else:
			print(f'The timer is set for {timer_time.time()}\n')
		if timer_time <= current_date_time and timer_time != datetime.min:#checks if current time has exceeded the timer
	 		print('YEEEEE FUCKING HAW TIMER TIME BOIS')
	 		timer_time = datetime.min
		else:
			pass
'''