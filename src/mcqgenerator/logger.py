import logging
import os
from datetime import datetime

LOG = "LOG"
LOG_FILE_NAME = f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log"

LOG_DIR = os.path.join(os.getcwd(), LOG)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]: %(lineno)d - %(name)s - %(levelname)s - %(message)s"
)