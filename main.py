from datetime import datetime, date, time, timedelta #used to assertain current time and date

#import gpiozero #handles all hardware events and pin controls

from pynput import mouse #used for testing and utlising the mouse as simulated buttons

current_date = None #initialises current date and time variables
current_time = None

timer_minutes_value = 5 #These variables control how long to add to the timer per button press
timer_seconds_value = 0 
hold_time = 1 #This is how long constitutes holding the button (to reset the timer) in seconds

press_time = datetime.min
release_time = datetime.min 

timer_time = datetime.min #initialises the timer time to minimum possible time (as this can be treated as null in later logic)
current_date_time = datetime.now() #initialises curent datetime

#button = gpiozero.Button(7) #Assigns main button to Pin 7 WILL NEED CHANGING WHEN HARDWARE ASSEMBLED
def on_click(x,y,button,pressed):
	global current_date_time #global variables used to track the timing of mouse events etc
	global press_time
	global release_time
	global timer_time

	if pressed: #checks if the mouse button is pressed
		print(f'Mouse button {button} was pressed')
		if button == mouse.Button.left:
			press_time = current_date_time
		else:
			pass

	else: #handles all events on mouse button release
		print(f'Mouse button {button} was released')
		if button == mouse.Button.left: 
			release_time = current_date_time
			print(f'it was held for {(release_time - press_time).seconds} seconds')
			if (release_time - press_time).seconds >= 5: #if held for > 5 seconds, stop mouse listener
				print('stopping mouse listener')
				pynput.mouse.Listener.stop
			elif (release_time - press_time).seconds >= hold_time: #if held for longer than specified hold_time, cancel timer
				timer_time = datetime.min
				print('The timer has been cancelled')
			elif timer_time == datetime.min: #if no timer set, set new timer
				timer_time = current_date_time + timedelta(minutes = timer_minutes_value, seconds = timer_seconds_value)
			else: #if timer exists, add time to timer
				timer_time = timer_time + timedelta(minutes = timer_minutes_value, seconds = timer_seconds_value)
		else:
			pass

listener = mouse.Listener( #defines the mouse listener to use the on_click function
	on_click=on_click)

listener.start() #starts the mouse listener  

while True:
	last_date = current_date #keeps track of the date of last loop, so it can be updated only when it changes
	last_time = current_time

	current_date_time = datetime.now() #updates current date_time - very important as this is used in almost all other functions (so as to reduce calls of .now())

	current_date = (current_date_time.day, current_date_time.month, current_date_time.year) # could probably be made more streamlined?
	current_time = (current_date_time.hour, current_date_time.minute, current_date_time.second)

	if current_date != last_date or current_time != last_time:
		print_date = current_date_time.strftime('%A the %d of %B, %Y')
		print_time = current_date_time.strftime('%I:%M:%S %p') # formats the date and times into a nice format (Day the DD of Month, YYYY) (HH:MM:SS AM/PM)
		print(f'The date today is {print_date} and the current time is {print_time}')

		if timer_time > datetime.min: #checks if timer set
			print(f'The timer is set for {timer_time.time()} and will be on for {(timer_time - current_date_time).seconds} seconds')
			if timer_time <= current_date_time: #checks if time has surpasses when timer should go off
				print('WEEWOOWEEWOOWEEWOO Timer is going off')
				timer_time = datetime.min #resets the timer once it goes off
		else:
			print('There is no timer set at the moment')
