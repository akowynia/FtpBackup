import subprocess as sp

from CreateConfig import CreateConfig
from Operations import Operations


class Menu:
    def author(self):
        version = "1.0"
        author = "Vrozax"
        git_link = "https://github.com/Vrozax"
        print("FTP download and archive from multiple servers")
        print("version:" + version)
        print("author:"+author)
        print("repo:"+git_link)

    def __init__(self):
        Menu.print_information(self)

    def print_information(self):
        config = CreateConfig()

        while True:

            sp.call('cls', shell=True)
            self.author()
            print("What can i do?")
            print("     1.Add server")
            print("     2.remove server")
            print("     3.change/edit server folders")
            print("     4.backup server")
            print("     0.exit")
            decision = input("choice: ")
            try:
                decision = int(decision)
                if decision == 0:
                    break
                if decision == 1:
                    config.add_server()
                if decision == 2:
                    config.remove_server()
                if decision == 3:
                    config.add_folders()
                if decision == 4:
                    
                    op = Operations()
                    op.create_backup()
            except ValueError:
                print("Write number!")
