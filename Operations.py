import shutil
from configparser import ConfigParser
from datetime import date
from pathlib import Path

from ftpConnect import *

backups_folder = Path("backups")
config = ConfigParser()

ftp = ftpConnect()


class Operations:

    def zipping_folder(self, folder_name):
        today = date.today()
        current_date = today.strftime("%m-%d-%Y")
        date_text = folder_name + "-" + str(current_date)
        shutil.make_archive("backups/" + date_text, 'zip', "backups/" + folder_name)

        try:
            shutil.rmtree("backups/" + folder_name)
        except OSError as e:
            logging.error("cannot delete folder" + folder_name)

    def create_backup(self):

        config.read('configs/config_data.ini')
        sections = config.sections()

        for sections_server in sections:

            host = config[sections_server]["host"]
            port = config[sections_server]["port"]
            password = config[sections_server]["password"]
            login = config[sections_server]["login"]
            folders_backup = config[sections_server]["folders_backup"]
            status = config[sections_server]["status"]

            if status == "active":
                # for all files
                if folders_backup == "*":

                    ftp.download_all_file(sections_server, host, int(port), login, password, "")
                    logging.info("downloaded all files from " + sections_server)
                    self.zipping_folder(sections_server)
                else:

                    list_folders = folders_backup.split(";")

                    # for specific folders
                    for current_folder in list_folders:
                        ftp.download_one_folder(sections_server, host, int(port), login, password, current_folder)

                    logging.info("downloaded all files from " + sections_server)
                    self.zipping_folder(sections_server)
            else:
                logging.info(sections_server + " are disabled, skipped")
