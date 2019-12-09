import Adafruit_DHT
import RPi.GPIO as GPIO
import time

chon_cam_bien = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)
pin_sensor = 18
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

while True:
   do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor);
   if do_am is not None and nhiet_do is not None:
     print(("Nhiet Do = {0:0.1f}  Do Am = {1:0.1f}\n").format(nhiet_do, do_am));
     time.sleep(1)
     if nhiet_do >= 33:
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
     else:
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
   else:
     print("Loi khong the doc tu cam bien DHT11 :(\n")
