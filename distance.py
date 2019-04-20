import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 35
ECHO = 37

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Calibrating...")
time.sleep(2)

try:
    while True:
        # Trigger a pulse to start measuring
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Distance:", distance, "cm")

        if distance > 2 and distance < 400:
            print("Distance:", distance, "cm")
        else:
            print("Out Of Range")

except KeyboardInterrupt:
    GPIO.cleanup()
