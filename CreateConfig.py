import os
import re
from configparser import ConfigParser
from pathlib import Path


class CreateConfig:

    # function created first configs
    def configInit(self):
        os.makedirs("configs", exist_ok=True)
        config_data = Path("configs/config_data.ini")
        if not config_data.is_file():
            while True:

                self.add_server()

                decision = input("add more?y/n")
                if decision == "n":
                    break




    def add_server(self):

        # regex patterns

        # ipv4 pattern
        host_pattern = '((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        # port pattern
        port_pattern = '[0-9]{1,5}'

        # variables
        config = ConfigParser()
        while True:
            host = str(input(f"host:\n"))
            port = str(input(f"port:\n"))
            if re.match(host_pattern, host) and re.match(port_pattern, port):
                break
            else:
                print("Please type host and port correctly")

        login = str(input(f"login:\n"))
        password = str(input(f"password:\n"))
        name_server = str(input(f"name server:\n"))
        print("Type which backup you need")
        print("* - all")
        print("or type folder-name separated by a semicolon:")
        folders_backup = str(input())

        # template server config
        config[name_server] = {'host': host,
                               'port': port,
                               'login': login,
                               'password': password,
                               'folders_backup': folders_backup,
                               'status': "active"
                               # 99 not set
                               }
        with open("configs/config_data.ini", 'w') as configfile:
            config.write(configfile)

    def remove_server(self):
        config = ConfigParser()
        config.read('configs/config_data.ini')
        list_server = config.sections()
        print("List servers:")
        counter = 0

        # print list server
        for print_list in list_server:
            print(counter + 1, " ", print_list)
            counter += 1
        delete_server = input("Which server to delete?\n type c to cancel :")
        if delete_server != "c":
            # open and save server config after delete
            if delete_server.isdigit():
                with open("configs/config_data.ini", 'w') as configfile:
                    delete_server = int(delete_server)
                    name = str(list_server[delete_server - 1])

                    config.remove_section(name)
                    config.write(configfile)
            else:
                print("canceled")


    def add_folders(self):
        config = ConfigParser()
        config.read('configs/config_data.ini')

        counter = 0
        list_server = config.sections()
        if len(list_server) == 0:
            print("Don't have any server, please add")
        else:
            print("List servers:")
            # print list server
            for print_list in list_server:
                print(counter + 1, " ", print_list)
                counter += 1
            change_server = input("Which server to change folders?\n type c to cancel")
            if change_server != "c":
                try:
                    if change_server.isdigit():
                        change_server = int(change_server)
                        with open("configs/config_data.ini", 'w') as configfile:

                            name = str(list_server[change_server - 1])
                            print("Actual folders:")

                            print(config[name]['folders_backup'])
                            while True:
                                print("Type folder name to add", end="\n")
                                print("Type '*' to select all folders", end="\n")
                                print("Type c to cancel", end="\n")

                                choice = input()

                                if choice != "c":
                                    if choice == "*":
                                        config[name]['folders_backup'] = '*'
                                        break
                                    else:
                                        config[name]['folders_backup'] +=  ";"+ choice
                                        break
                                else:
                                    break

                            config.write(configfile)
                except:
                    print("type number or c")
            else:
                print("canceled")
