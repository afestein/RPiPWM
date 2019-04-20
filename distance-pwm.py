import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

buzzer = 10
echo = 37
trig = 35

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1)
pwm.start(50)

GPIO.output(trig, False)
print("Calibrating distance sensor...")
time.sleep(2)

try:
    while 1:
        # Trigger a pulse to start measuring
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            pulse_start = time.time()

        while GPIO.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150  # calculate distance in cm
        print("Distance:", round(distance, 2), "cm")

        # map distance to hertz, e.g. 10cm equals 1000hz
        frequency = distance * 100
        pwm.ChangeFrequency(frequency)

        if distance > 2 and distance < 100:
            print("Distance:", distance, "cm")
        else:
            print("Out Of Range")

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
