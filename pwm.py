import RPi.GPIO as GPIO
import time

buzzer = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer, GPIO.OUT)

try:
    # pwm = GPIO.PWM(buzzer, 0.5)
    # pwm.start(1)
    # while 1:
    #     for dc in range(0, 101, 5):
    #     pwm.ChangeDutyCycle(dc)
    #     time.sleep(0.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(3)
except KeyboardInterrupt:
    pass
# pwm.stop()
GPIO.cleanup()
