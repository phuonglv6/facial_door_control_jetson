import RPi.GPIO as GPIO

PIN_DOOR_CTR = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_DOOR_CTR, GPIO.OUT)
def open_door():
    GPIO.output(PIN_DOOR_CTR, GPIO.HIGH)
    print("Open the door")
def close_door():
    GPIO.output(PIN_DOOR_CTR, GPIO.LOW)
    print("Close the door")