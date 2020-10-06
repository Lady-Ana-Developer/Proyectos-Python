import RPi.GPIO as GPIO
import time

# define motion pin
motion_pin = 23

TRIG = 16
ECHO = 12
# set GPIO as GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set pin mode as INPUT
GPIO.setup(motion_pin, GPIO.IN)

try:
    while True:
        if(GPIO.input(motion_pin) == 0):
            print("Nothing moves ...")
                
        elif(GPIO.input(motion_pin) == 1):
                print("Motion detected!")
                GPIO.setup(TRIG,GPIO.OUT)
                GPIO.setup(ECHO,GPIO.IN)

                GPIO.output(TRIG, False)
                print("Waiting For Sensor To Settle")
                time.sleep(2)

                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                while GPIO.input(ECHO)==0:
                pulse_start = time.time()

                while GPIO.input(ECHO)==1:
                pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start

                distance = pulse_duration * 17150

                distance = round(distance, 2)
                
                print("Distance: %scm" % distance)

except KeyboardInterrupt:
    GPIO.cleanup()     
            
            