from serial_reader import read
from parser import parse
from odoo_client import send
from logger import logger
from config import CONFIG

print("QC Agent Started...")

while True:

    raw = read()

    logger.info(raw)

    data = parse(raw)

    if not data:
        continue

    value = data["value"]

    status = "PASS"

    if value < CONFIG["qc"]["min"]:

        status = "FAIL"

    if value > CONFIG["qc"]["max"]:

        status = "FAIL"

    payload = {

        "manufacturing_order": data["mo"],

        "test": data["test"],

        "value": value,

        "status": status

    }

    send(payload)

    print(payload)