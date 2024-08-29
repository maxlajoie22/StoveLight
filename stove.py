from sense_hat import SenseHat
import time
sense = SenseHat()

red = (255,0,0) 
nothing = (0,0,0)

def too_hot(light): # capital H

  R = red
  O = nothing
  logo = [
    O, O, R, O, O, R, O, O,
    O, O, R, O, O, R, O, O,
    O, O, R, O, O, R, O, O,
    O, O, R, R, R, R, O, O,
    O, O, R, O, O, R, O, O,
    O, O, R, O, O, R, O, O,
    O, O, R, O, O, R, O, O,
    light, O, R, O, O, R, O, O,
    ]
  return logo
  
def medium_hot(light): # lowercase h
  R = red
  O = nothing
  logo = [
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, R, R, R, O, O,
    O, O, R, O, O, R, O, O,
    O, O, R, O, O, R, O, O,
    light, O, R, O, O, R, O, O,
    ]
  return logo

def humidity_detected(light): # E
  R = red
  O = nothing
  logo = [
    O, O, R, R, R, R, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, R, R, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, O, R, O, O, O, O, O,
    light, O, R, R, R, R, O, O,
    ]
  return logo
  

def start(light): # blank board
  R = red
  O = nothing
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    light, O, O, O, O, O, O, O,
    ]
  return logo

light = (0,0,0) # status of the stove light (whether if it is on/off)
image = start(light)
sense.set_pixels(image)
status = "off"

while True:
  temp = round(sense.get_temperature(),0)
  humidity = round(sense.get_humidity(),0)
  
  if status== "on": #checks to see if stove is on or ot
    light = (255,0,0)
  elif status == "off":
    light = (0,0,0)
  
  if temp >= 50 and temp <= 75:
    image = medium_hot(light)
    sense.set_pixels(image)
  elif temp > 75:
    image = too_hot(light)
    sense.set_pixels(image)
  
 
  time.sleep(.5)
  
  if humidity > 60:
    image = humidity_detected(light)
    sense.set_pixels(image)
    
    

  
  time.sleep(.5)
  
  if humidity <= 60 and temp < 50: # clears board if needed
    image = start(light)
    sense.set_pixels(image)
  
  
  events = sense.stick.get_events()
  for event in events: # turns stove on and off
    if event.action == "pressed" and event.direction == "middle":
      if status == "off":
        status = "on"
      elif status == "on":
        status ="off"
      
  
