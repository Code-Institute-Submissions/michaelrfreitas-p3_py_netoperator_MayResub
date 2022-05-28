""" This module to create a troubleshooting script importing devices module """

import os
from pathlib import Path
from devices import TshootDevices


class TroubQuestions(TshootDevices):
    """ Class to provide the question for Troubleshooting devices """

    def __repr__(self):
        return f'''
        ---
        Ping Destination: {self.ping_dest.upper()}
        Status VLAN: {self.status_vlan.upper()}
        Validate Routing Table: {self.routing_tab.upper()}
        Validate Routing Protocol: {self.proto_stat.upper()}
        Mirror Configuration: {self.mirror_config.upper()}
        ---
        '''

    def printer_full(self, vendor):
        """
        Function to printer in screen troubleshooting commands
        """
        if vendor == '1' and self.mirror_config.upper() == 'Y':
            path_temp_1 = Path('assets/templates/mirror_cisco.txt')
        if vendor == '2' and self.mirror_config.upper() == 'Y':
            path_temp_1 = Path('assets/templates/mirror_datacom.txt')
        if self.ping_dest.upper() == 'N' or self.status_vlan.upper() == 'N':
            path_temp_2 = Path('assets/templates/icmp.txt')
            path_temp_3 = Path('assets/templates/network_layer.txt')
            path_temp_4 = Path('assets/templates/data_layer.txt')
        if self.routing_tab.upper() == 'N' or self.proto_stat.upper() == 'N':
            path_temp_2 = Path('assets/templates/icmp.txt')
            path_temp_3 = Path('assets/templates/network_layer.txt')
            path_temp_4 = Path('assets/templates/routing.txt')

        try:
            reading_file1 = open(path_temp_1, "r", encoding='UTF-8')
        except UnboundLocalError:
            pass
        reading_file2 = open(path_temp_2, "r", encoding='UTF-8')
        reading_file3 = open(path_temp_3, "r", encoding='UTF-8')
        reading_file4 = open(path_temp_4, "r", encoding='UTF-8')

        try:
            for line in reading_file1:
                print(line)
            reading_file1.close()
        except UnboundLocalError:
            pass

        for line in reading_file2:
            print(line)
        reading_file2.close()

        for line in reading_file3:
            print(line)
        reading_file3.close()

        for line in reading_file4:
            print(line)
        reading_file4.close()

    def questions(self):
        """
        Function to provide questions regarding Troubleshooting
        """
        # Loop to keep code running while validate false
        while True:
            self.ping_dest = input(
                'Can you PING the destination? YES (Y) or NO (N): ')
            if validate_answer(self.ping_dest.upper()):
                break
        while True:
            self.status_vlan = input(
                'Can you validate the VLAN status? YES (Y) or NO (N): ')
            if validate_answer(self.status_vlan.upper()):
                break
        while True:
            self.routing_tab = input(
                'Can you validate the routing table? YES (Y) or NO (N): ')
            if validate_answer(self.routing_tab.upper()):
                break
        while True:
            self.proto_stat = input(
                'Can you validate the routing protocol? YES (Y) or NO (N): ')
            if validate_answer(self.proto_stat.upper()):
                break
        while True:
            self.mirror_config = input(
                'Do you want to setup a monitor port? YES (Y) or NO (N): ')
            if validate_answer(self.mirror_config.upper()):
                break


def validate_answer(answer):
    """
    Validate function to check the answer for troubleshooting
    """
    try:
        if answer != 'Y' and answer != 'N':
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This answer {answer} is incorrect,
                please, be sure to type it correctly
                YES (Y) or NO (N)
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def clear_terminal():
    """
    Clear terminal with os.system
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')
