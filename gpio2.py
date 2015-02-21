#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

def update(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)

if __name__ == '__main__':
    angle = input("Bitte Winkel eingeben")
    update(angle)

    i = 0
    while(angle != 0):
        if i != 1000000:
            i += 1
        else:
            i = 0
            angle = input("Bitte Winkel eingeben (0 zum abbrechen)")
            update(angle)
    GPIO.cleanup()