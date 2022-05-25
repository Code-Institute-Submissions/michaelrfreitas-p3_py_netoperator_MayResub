""" This module to create a config script importing devices module """
from devices import ConfSwitchL3
import os
import re


class ConfQuestionsSWL3(ConfSwitchL3):
    """ Fuction to provide the question for configuratio L3 devices """

    def __repr__(self):

        return f'''
        ---
        {self.hostname}
        {self.username}
        ---
        '''

    def return_full_config(self):
        pass

    def questions(self):
        self.hostname = input('Whats the hostname? ')
        self.username = input('Whats the username? ')
        self.password = input('Whats the password? ')
        while True:
            self.manager_vlan = input('Whats the manager VLAN ID? (1-4094): ')
            if validate_vlan(self.manager_vlan):
                clear_terminal()
                break
        while True:
            self.manager_ip = input(
                'Whats the manager IP? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_ip):
                clear_terminal()
                break
        self.manager_mask = input(
            'Whats the manager mask? (XXX.XXX.XXX.XXX): ')
        self.primary_int_vlan = input(
            'Whats the primary interface VLAN? (1-4094): ')
        self.primary_int_ip = input(
            'Whats the primary interface IP? (XXX.XXX.XXX.XXX): ')
        self.primary_int_mask = input(
            'Whats the primary interface mask? (XXX.XXX.XXX.XXX): ')
        self.default_gateway = input(
            'Whats the default gateway? (XXX.XXX.XXX.XXX): ')


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
        if not (re.search(regex, answer)):
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


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
