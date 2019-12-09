import time
from  urllib.request import urlopen
import Adafruit_DHT
import RPi.GPIO as GPIO

chon_cam_bien = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)
pin_sensor = 18

# Enter Your API key here
myAPI = '5W3OPR2IB7M5487L'
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key={}'.format(myAPI)



while True:
    time.sleep(1)
    h, t = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor);
    if h is not None and t is not None:
      conn = urlopen(baseURL + '&field1={}&field2={}'.format(t, h))
      print(conn.read())
      conn.close()
      print(t, h)

