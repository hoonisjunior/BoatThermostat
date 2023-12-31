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
current_date_time = datetime.now() #initialises curent datetime, and previous datetime
last_date_time = datetime.now()
#button = gpiozero.Button(7) #Assigns main button to Pin 7 WILL NEED CHANGING WHEN HARDWARE ASSEMBLED
def on_click(x,y,button,pressed):
	global current_date_time #global variables used to track the timing of mouse events etc
	global press_time
	global release_time
	global timer_time

	if pressed: #checks if the mouse button is pressed
		print(f'Mouse button {button} was pressed') #TESTING output which mouse button released
		if button == mouse.Button.left:
			press_time = current_date_time
		else:
			pass

	else: #handles all events on mouse button release
		print(f'Mouse button {button} was released') #TESTING output which mouse button released
		if button == mouse.Button.left: 
			release_time = current_date_time
			print(f'It was held for {(release_time - press_time).seconds} seconds') #TESTING output to show how long mouse was held
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

def get_formatted_date_time(datetime_obj): #takes a datetime object and returns 2 nicely formatted strings
	print_date = datetime_obj.strftime('%A the %d of %B, %Y')
	print_time = datetime_obj.strftime('%I:%M:%S %p')
	return print_date, print_time

def console_info_print(): #checks if the time has changed by at least 1 second, prints all relevant info to console.
	global current_date_time
	global last_date_time
	global timer_time 
	print_date, print_time = get_formatted_date_time(current_date_time) 
	if current_date_time.replace(microsecond = 0) != last_date_time.replace(microsecond = 0): #only prints info if the datetime has changed by at least a second
		print(f'The date today is {print_date} and the time is currently {print_time}')
		if timer_time > datetime.min: #checks if timer set
			print(f'The timer is set for {timer_time.time()} and will go off in {(timer_time - current_date_time).seconds} seconds')
		else: #if no timer set
			print('There isn\'t a timer set right now.')

listener = mouse.Listener( #defines the mouse listener to use the on_click function
	on_click=on_click)

listener.start() #starts the mouse listener  

while True:
	last_date_time = current_date_time #updates previous datetime
	current_date_time = datetime.now()#updates current datetime
	console_info_print()#Tries to print all info to console
	if timer_time > datetime.min: #checks if timer is set
		if timer_time <= current_date_time: #checks if time has surpassed when timer should go off
				print('WEEWOOWEEWOOWEEWOO Timer is going off') #timer goes off
				timer_time = datetime.min #resets the timer once it goes off
		else:
			pass
	else:
		pass

