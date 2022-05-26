""" This module to create a config script importing devices module """

import os
import re
import shutil
import datetime
from devices import ConfSwitchL3
from pathlib import Path


class ConfQuestionsSWL3(ConfSwitchL3):
    """ Fuction to provide the question for configuratio L3 devices """

    def __repr__(self):

        return f'''
        ---
        Hostname: {self.hostname}
        Username: {self.username}
        Password: {self.password}
        Manager VLAN ID: {self.manager_vlan}
        Manager IP address: {self.manager_ip}
        Manager Subnet Mask: {self.manager_mask}
        Primary Interface VLAN ID: {self.primary_int_vlan}
        Primary Interface IP address: {self.primary_int_ip}
        Primary Interface Subnet Mask: {self.primary_int_mask}
        Default Gateway: {self.default_gateway}
        ---
        '''

    def return_full_config(self):
        date = datetime.datetime.now()

        base_path_temp = Path('assets/templates/c_sw_l3.txt')
        base_path_conf = Path('assets/configs/' +
                              self.hostname + '_' + date.strftime('%d') + '-' + date.strftime('%b') + '-' + date.strftime('%Y') + '.txt')

        shutil.copyfile(base_path_temp, base_path_conf)

        reading_file = open(base_path_temp, "r")
        writing_file = open(base_path_conf, 'w')

        find_conf = ("${hostname}", "${username}", "${password}",
                     "${manager_vlan}", "${manager_ip}", "${manager_mask}",
                     "${primary_int_vlan}", "${primary_int_ip}",
                     "${primary_int_mask}", "${default_gateway}")
        repl_conf = (self.hostname, self.username, self.password,
                     self.manager_vlan, self.manager_ip,
                     self.manager_mask, self.primary_int_vlan,
                     self.primary_int_ip, self.primary_int_mask,
                     self.default_gateway)

        for line in reading_file:
            for find, repl in zip(find_conf, repl_conf):
                line = line.replace(find, repl)
            writing_file.write(line)
        reading_file.close()
        writing_file.close()

    def questions(self):
        while True:
            self.hostname = input('What is the hostname? (SW-HOST-01): ')
            if validate_text(self.hostname):
                clear_terminal()
                break
        while True:
            self.username = input('What is the username? (local-admin): ')
            if validate_text(self.username):
                clear_terminal()
                break
        while True:
            self.password = input(
                'What is the password? (Minimun 8 characteres): ')
            if validate_pwd(self.password):
                clear_terminal()
                break
        while True:
            self.manager_vlan = input(
                'What is the manager VLAN ID? (1-4094): ')
            if validate_vlan(self.manager_vlan):
                clear_terminal()
                break
        while True:
            self.manager_ip = input(
                'What is the manager IP address? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_ip):
                clear_terminal()
                break
        while True:
            self.manager_mask = input(
                'What is the manager subnet mask? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_mask):
                clear_terminal()
                break
        while True:
            self.primary_int_vlan = input(
                'What is the primary interface VLAN ID? (1-4094): ')
            if validate_vlan(self.primary_int_vlan):
                clear_terminal()
                break
        while True:
            self.primary_int_ip = input(
                'What is the primary interface IP address? ' +
                '(XXX.XXX.XXX.XXX): ')
            if validate_ip(self.primary_int_ip):
                clear_terminal()
                break
        while True:
            self.primary_int_mask = input(
                'What is the primary interface subnet mask? ' +
                '(XXX.XXX.XXX.XXX): ')
            if validate_ip(self.primary_int_mask):
                clear_terminal()
                break
        while True:
            self.default_gateway = input(
                'What is the default gateway? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.default_gateway):
                clear_terminal()
                break


def validate_vlan(answer):
    """
    Validate function to check the answer for VLAN
    """
    try:
        # Convert answer to integer
        num = int(answer)
        # Check if received the specific numbers
        if num < 1 or num > 4094:
            clear_terminal()
            print(
                f'''
            --------------- WARNING ---------------
            This VLAN {answer} is incorrect,
            please, be sure to type it correctly
            VLAN ID should be between 1 - 4094
            --------------- WARNING ---------------
            '''
            )
            return False
    except ValueError:
        # Check if it received a integer number if not receive a message
        clear_terminal()
        print(
            f'''
            --------------- WARNING ---------------
            This VLAN {answer} is incorrect,
            please, be sure to type it correctly
            VLAN ID should be between 1 - 4094
            --------------- WARNING ---------------
            '''
        )
        return False
    # Return true if didn't have error
    return True


def validate_ip(answer):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    try:
        if not re.search(regex, answer):
            clear_terminal()
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This IP {answer} is incorrect,
                please, be sure to type it correctly
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def validate_text(answer):
    try:
        if len(answer) < 5 or len(answer) > 20:
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This text {answer} is incorrect,
                please, be sure to type it correctly
                minimum 5 and maximum 20 characters
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def validate_pwd(answer):
    try:
        if len(answer) < 8:
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This password {answer} is incorrect,
                please, be sure to type it correctly
                minimum 8 characters
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
