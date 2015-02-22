#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)      # (Broadcom SOC Channel Number) Achtung, bei jedem Board aendern die Ports
GPIO.setup(18, GPIO.OUT)    # (Channel 18, Output-Modus)
pwm = GPIO.PWM(18, 100)     # (Channel 18, Frequenz 100Hz)
pwm.start(5)                # (Duty Cycle 5)

def update(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)

if __name__ == '__main__':
    angle = input("Bitte Winkel eingeben")
    update(angle)

    while angle != 0:
        angle = input("Bitte Winkel eingeben (0 zum abbrechen)")
        update(angle)
    pwm.stop()
    GPIO.cleanup()