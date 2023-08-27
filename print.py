import time
import cups
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
from random import randint
import os

conn = cups.Connection()
printers = conn.getPrinters()
printer = printers['Xprinter-XP-420B']

BTN_pin = 10
GREEN_pin = 40
YELLOW_pin = 38
RED_pin = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BTN_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(GREEN_pin, GPIO.OUT)
GPIO.setup(YELLOW_pin, GPIO.OUT)
GPIO.setup(RED_pin, GPIO.OUT)

GPIO.output(GREEN_pin, GPIO.HIGH)
GPIO.output(YELLOW_pin, GPIO.LOW)
GPIO.output(RED_pin, GPIO.LOW)

# list all the png files in the images folder
images = os.listdir('images/')
images = [i for i in images if i.endswith('.png')]

def print_image():
    #print('printing')
    GPIO.output(GREEN_pin, GPIO.LOW)
    GPIO.output(YELLOW_pin, GPIO.HIGH)
    idx = randint(0, len(images) - 1)
    
    base_img = Image.open('images/' + images[idx])
    base_img.save('temp.png')
    
    conn.printFile('Xprinter-XP-420B', 'temp.png', 'image', {})
    
    """ time.sleep(1)
    GPIO.output(RED_pin, GPIO.LOW)
    GPIO.output(YELLOW_pin, GPIO.HIGH) """
    time.sleep(1)
    GPIO.output(YELLOW_pin, GPIO.LOW)
    GPIO.output(GREEN_pin, GPIO.HIGH)
    
while True:
    if GPIO.input(10) == GPIO.HIGH:
        #print("hello")
        print_image()   
        
    #GPIO.add_event_detect(10, GPIO.RISING, callback=print_image, bouncetime=12000) 
#message = input("Press enter to quit\n\n") # Run until someone presses enter
#GPIO.cleanup() # Clean up
