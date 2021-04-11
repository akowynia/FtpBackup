import logging
import os.path
from pathlib import Path

from Menu import *


# paths program
config_data = Path("configs/config_data.ini")
backup_folder = Path("backups")

logging.basicConfig(filename="latest.log", filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# check if configs is crated
if config_data.is_file() and os.path.isdir(backup_folder):

    menu = Menu()


else:
    # create config file and folder
    if not os.path.isdir(backup_folder):
        os.makedirs("backups", exist_ok=True)
    x = CreateConfig()
    x.configInit()

    menu = Menu()
