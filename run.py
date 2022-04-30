"""
This is the main module of run python with basic questions
"""
import pyfiglet


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
            print("Next...")
        # If false should back to the previous question
        else:
            continue
        # Loop to keep code running while validate false
        while True:
            # Variable type_device take which type of device the user will work
            type_device = input(
                "Which type of device?\nType number:\n< 1 > Switch\n"
                "< 2 > Router\n")
            # Validate type_device if the user provided a right answer if
            # true go to next question
            if validate_answers(type_device):
                print("Next...")
            # If false should back to the previous question
            else:
                continue
            while True:
                # If type_device is 1 (Switch) the next question is
                # what's the layer
                if type_device == '1':
                    # Variable layer take an answer regarding the layer
                    # of switch use
                    layer = input(
                        "Which layer?\nType number:\n< 1 > Layer2\n"
                        "< 2 > Layer3\n")
                    # Validate layer if the user provided a right answer
                    # if true go to next question
                    if validate_answers(layer):
                        print("Next...")
                    # If false should back to the previous question
                    else:
                        continue
                else:
                    # Variable route take an answer regarding the routing
                    # of router use
                    route = input(
                        "Which type of route?\nType number:\n< 1 > Static\n"
                        "< 2 > Dynamic\n")
                    # Validate route if the user provided a right answer if
                    #  true go to next question
                    if validate_answers(route):
                        print("Next...")
                    # If false should back to the previous question
                    else:
                        continue
                while True:
                    # Variable vendor take an answer regarding the vendor
                    # of the device
                    vendor = input(
                        "Which vendor?\nType number:\n< 1 > Cisco\n"
                        "< 2 > Aruba\n< 3 > Datacom\n< 4 > HP Comware\n")
                    # Validate vendors if the user provided a right answer if
                    # true go to next step
                    if validate_answers_vendors(vendor):
                        print("Next...")
                        break
                    # If false should back to the previous question
                    else:
                        continue
                break
            break
        break


def validate_answers(answer):
    """
    Validate function to check all answers with 2 options and validate
    the data provided.
    """
    try:
        # Convert answer to integer
        num = int(answer)
        # Check if received the specific numbers
        if num != 1 and num != 2:
            # If is not number 1 and 2 you receive a message error
            raise ValueError(
                f'Make sure you have writing\n< 1 > or < 2 > not {answer}\n'
            )
    except ValueError as error:
        # Check if it received a integer number if not receive a message
        print(f"{error}is not accepted. Please try again.\n")
        return False
    # Return true if didn't have error
    return True


def validate_answers_vendors(answer):
    """
    Validate function to check the answers about vendor question and
    validate the data provided.
    """
    try:
        # Convert answer to integer
        num = int(answer)
        # Check if received the specific numbers
        if num != 1 and num != 2 and num != 3 and num != 4:
            # If is not number 1 and 2 you receive a message error
            raise ValueError(
                f'This answer {answer} is not right\nMake sure you have '
                'writing\n< 1 > or < 2 > or < 3 > or < 4 >\n'
            )
    except ValueError as error:
        # Check if it received a integer number if not receive a message
        print(f"{error}is not accepted. Please try again.\n")
        return False
    # Return true if didn't have error
    return True


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

main()  # Call main function
