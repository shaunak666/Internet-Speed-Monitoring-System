
import subprocess
from time import sleep
from pynput.keyboard import Key, Controller
import csv
import time
import datetime
import speedtest


keyboard = Controller()
s = speedtest.Speedtest()

alert = "The internet speed is pretty low :/"
fieldnames = ["time", "downspeed", "upspeed"]

with open('speed_data.csv', 'w' , newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
while True:

    with open('speed_data.csv', 'a', newline = '') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        while True:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(" Entering the process...")
            downspeed = round((round(s.download()) / 1048576), 2)
            print("DownSpeed Calculated...")
            upspeed = round((round(s.upload()) / 1048576), 2)
            print("Upspeed Calculated...")
            csv_writer.writerow({
                'time': time_now,
                'downspeed': downspeed,
                "upspeed": upspeed
            })
            print(f"CSV written ||{time_now }|| {downspeed} || {upspeed}")
            if downspeed < 90:
                subprocess.Popen(["cmd", "/C", f"start whatsapp://send?phone=+919356691596"], shell=True) # phone number shall contain country code too
                time.sleep(1)
                keyboard.type(alert)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

    time.sleep(1)


