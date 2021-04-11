import logging
import os
from ftplib import FTP


class ftpConnect:

    def __init__(self):
        pass

    def download_all_file(self, sections_server, host, port, login, password, directory_add):
        backup_folder = "backups/" + sections_server
        if not os.path.isdir(backup_folder):
            os.makedirs(backup_folder, exist_ok=True)
        ftp = FTP()
        connected = False
        try:

            ftp.connect(host, port)
            ftp.login(login, password)
            connected = True
        except:
            logging.error(sections_server + " not responding")
        if connected:
            if directory_add != "":
                ftp.cwd(directory_add)
                directory_add += "/"

            folders = []
            list_folders = []
            ftp.retrlines('MLSD', folders.append)

            for directory in folders:
                splitted = directory.split(';')
                if splitted[-2] == "Type=dir":

                    splitted = splitted[len(splitted) - 1].lstrip()
                    list_folders.append(splitted)
                    folders_pattern = backup_folder + "/" + directory_add + splitted
                    os.mkdir(folders_pattern)
                else:

                    file_path = backup_folder + "/" + directory_add + splitted[len(splitted) - 1].lstrip()
                    file_on_server = splitted[len(splitted) - 1].lstrip()
                    with open(file_path, "wb") as file:

                        # Command for Downloading the file "RETR filename"
                        ftp.retrbinary(f"RETR {file_on_server}", file.write)
            ftp.close()

            # download other folders
            for folders_in_this_location in list_folders:
                new_folder = directory_add + folders_in_this_location
                try:

                    self.download_all_file(sections_server, host, port, login, password, new_folder)

                except:
                    logging.error("error with download" + new_folder)

    def download_one_folder(self, sections_server, host, port, login, password, directory_add):

        backup_folder = "backups/" + sections_server
        if not os.path.isdir(backup_folder):
            os.makedirs(backup_folder, exist_ok=True)

        if os.path.isdir(backup_folder + "/" + directory_add):
            print()
        else:
            os.mkdir(backup_folder + "/" + directory_add)

        ftp = FTP()
        connected = False
        try:

            ftp.connect(host, port)
            ftp.login(login, password)
            connected = True
        except:
            logging.error(sections_server + " not responding")
        if connected:

            # change folder
            if directory_add != "":
                ftp.cwd(directory_add)
                directory_add += "/"

            folders = []
            list_folders = []
            ftp.retrlines('MLSD', folders.append)

            for directory in folders:
                splitted = directory.split(';')
                if splitted[-2] == "Type=dir":

                    splitted = splitted[len(splitted) - 1].lstrip()

                    list_folders.append(splitted)
                    folders_pattern = backup_folder + "/" + directory_add + splitted
                    os.mkdir(folders_pattern)
                else:

                    file_path = backup_folder + "/" + directory_add + splitted[len(splitted) - 1].lstrip()
                    file_on_server = splitted[len(splitted) - 1].lstrip()
                    with open(file_path, "wb") as file:

                        # Command for Downloading the file "RETR filename"
                        ftp.retrbinary(f"RETR {file_on_server}", file.write)
            ftp.close()

            # download other folders
            for folders_in_this_location in list_folders:
                new_folder = directory_add + folders_in_this_location
                try:
                    self.download_one_folder(sections_server, host, port, login, password, new_folder)

                except:
                    logging.error("error with download" + new_folder)
