SIMULATION = True

import serial
import random
import time

from config import CONFIG

if not SIMULATION:

    ser = serial.Serial(
        CONFIG["serial"]["port"],
        CONFIG["serial"]["baudrate"],
        timeout=CONFIG["serial"]["timeout"]
    )


def read():

    if SIMULATION:

        time.sleep(2)

        moisture = round(random.uniform(7, 14), 2)

        return f"MO00001,MOISTURE,{moisture}"

    else:

        return ser.readline().decode().strip()