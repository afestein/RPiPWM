import RPi.GPIO as GPIO
from time import sleep

buzzer = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1)

try:
    while 1:
        for frequency in range(1, 5001, 1000):
            pwm.start(50)
            pwm.ChangeFrequency(frequency)
            sleep(1)
            pwm.stop()
            sleep(1)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
