#!/usr/bin/python3

from sense_hat import SenseHat
sense = SenseHat()

scroll_speed = .001
sense.clear((64, 64, 64))

sense.show_message("sweaty clungus")


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        sense.show_message(event.direction)
