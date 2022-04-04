import RPi.GPIO as GPIO
import time
led = 18 #Connect the Kathode with ground and the Anode with an GPIO of your choice(in this case pin 18)
frequenz = 1000
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
ledFade = GPIO.PWM(led, frequenz)
GPIO.output(led, GPIO.HIGH)
ledFade.start(0)

while True:
    for i in range (0, 101, 5):
        ledFade,ChangeDutyCycle(25)
        sleep(0.05)
        for i in range(100, 0, -5)
        ledFade.ChangeDutyCycle(i)
        sleep(0.05)
