import Adafruit_DHT
import RPi.GPIO as GPIO
import time

chon_cam_bien = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)
pin_sensor = 18

while True:
   do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor);
   if do_am is not None and nhiet_do is not None:
     print(("Nhiet Do = {0:0.1f}  Do Am = {1:0.1f}\n").format(nhiet_do, do_am));
     time.sleep(1)
   else:
     print("Loi khong the doc tu cam bien DHT11 :(\n")
