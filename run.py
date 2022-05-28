"""
This is the main module of run python with basic questions
"""
import os
import pyfiglet
import config
import tshoot


def basic_questions():
    """
    Ask the basic questions to the customer to start the application flow.
    According the customer's answers, we will provide the next steps.
    """
    # Loop to keep code running while validate false
    while True:
        # Variable netoperator take if the user wants to do a Basic
        # Configuration or Troubleshooting
        netoperator = input(
            "What would you like to do?\nType number:\n"
            "< 1 > Basic Configuration\n< 2 > Basic Troubleshooting\n")

        # Validate netoperator if the user provided a right answer if
        # true go to next question
        if validate_answers(netoperator):
            clear_terminal()
            break

    # Loop to keep code running while validate false
    while True:
        type_device = ''
        if netoperator == '1':
            # Variable type_device take which type of device the user will work
            type_device = input(
                "Which type of device?\nType number:\n< 1 > Switch\n"
                "< 2 > Router\n")
            # Validate type_device if the user provided a right answer if
            # true go to next question
            if validate_answers(type_device):
                clear_terminal()
                break
        else:
            break

    # Loop to keep code running while validate false
    while True:
        # If type_device is 1 (Switch) the next question is
        # what's the layer
        if type_device == '1' and netoperator == '1':
            # Variable layer take an answer regarding the layer
            # of switch use
            layer = input(
                "Which layer?\nType number:\n< 1 > Layer2\n"
                "< 2 > Layer3\n")
            # Validate layer if the user provided a right answer
            # if true go to next question
            if validate_answers(layer):
                clear_terminal()
                break
        else:
            break

    if netoperator == '1' and type_device == '1' and layer == '1':
        operator = config.ConfQuestionsSWL2()
    if netoperator == '1' and type_device == '1' and layer == '2':
        operator = config.ConfQuestionsSWL3()
    if netoperator == '1' and type_device == '2':
        operator = config.ConfQuestionsRouter()
    if netoperator == '2':
        operator = tshoot.TroubQuestions()

    # Loop to keep code running while validate false
    while True:
        # Variable vendor take an answer regarding the vendor
        # of the device
        vendor = input(
            "Which vendor?\nType number:\n< 1 > Cisco\n"
            "< 2 > Datacom\n")
        # Validate vendors if the user provided a right answer if
        # true go to next step
        if validate_answers(vendor):
            clear_terminal()
            operator.questions()
            clear_terminal()
            print(operator)
            create_file = input(
                'Do you want print config? YES (Y) or NO (N): ')
            if create_file.upper() == 'Y':
                print("""
                --------------- SEE CONFIG COPY-PASTE ---------------
                """)
                operator.printer_full(vendor)
            break


def validate_answers(answer):
    """
    Validate function to check all answers with 2 options and validate
    the data provided.
    """
    try:
        # Check if received the specific value
        if answer != '1' and answer != '2':
            # If is not number 1 and 2 you receive a message error
            raise ValueError(
                f'''
            --------------- WARNING ---------------
            This answer {answer} is incorrect,
            please, be sure to type it correctly
            < 1 > or < 2 >
            --------------- WARNING ---------------
            '''
            )
    except ValueError as err:
        # Check if it received a integer number if not receive a message
        clear_terminal()
        print(f"{err}")
        return False
    # Return true if didn't have error
    return True


def clear_terminal():
    """
    Clear terminal with os.system
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Main function to call other functions in the application.
    """
    # Call basic questions
    basic_questions()


# Print Welcome message
ascii_banner = pyfiglet.figlet_format("NetOperator")
print(ascii_banner)
print("Welcome to NetOperator\n")
print("This tools have been created to help Network Engineer with "
      "basic day-by-day\n")
print("In this application you can create a basic config for some "
      "network devices.\n")
print("You can create a troubleshooting file with some steps to "
      "fix a issue.\n")


if __name__ == '__main__':
    main()  # Call main function
