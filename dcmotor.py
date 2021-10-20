import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 25
GPIO.setup(pwmPin, GPIO.OUT)

pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(1)

try:
  while True:
    for dc in reversed(range(100)):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(0.5)
except KeyboardInterrupt:
  print("bye")
GPIO.cleanup() 