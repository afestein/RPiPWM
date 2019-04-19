import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 35  # blue
ECHO = 37  # yellow

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while 1:
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    # Create a pulse to trigger the sensor to start ranging
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
        print("Echo is LOW")
        pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
        print("Echo is HIGH")
        pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150  # calculate distance in centimetres
    distance = round(distance, 2)
    print(f"Distance: {distance}")

    if distance > 2 and distance < 400:  # Check whether the distance is within range
        # Print distance with 0.5 cm calibration
        print("Distance:"), distance - 0.5, "cm"
    else:
        print("Out Of Range")
