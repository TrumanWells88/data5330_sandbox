import csv
import datetime
import urllib.request
import json
import sys
import logging
from pathlib import Path

API_URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

HERE = Path(__file__).resolve.parent()

LOG_DIR = HERE/"logs"
LOG_DIR.mkdir(exists=True)

run_time = datetime.datetime.now()
log_file = LOG_DIR/f"run_{run_time:%Y-%m-%d_%H-%M-%S}.log"

logging.basicconfig(filename=log_file, level=logging.INFO)
logger.logging.getLogger("pipeline")

logger.info("pipeline started")

try:
    request = urllib.request.Request(API_URL, headers={"User-Agent":"cron-demo"})
    with urllib.request.urlopen(request, timeout=20) as response:
        price = print(json.load(response)["data"]["amount"])
        price
    logger.info("price is received")
    
    csv_path = HERE/"prices.csv"
    with open(csv_path, "a", newline="") as f:
        csv.writer(f).writerow([run_time.isoformat(timespec="seconds"), price])
    logger.info("price is written to the csv")
    logger.info("pipeline is finished")

except Exception:
    logger.Exception("pipeline failed")
    sys.exit(1)
