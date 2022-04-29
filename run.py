def basic_questions():
    """
    Ask the basic questions to the customer to start the application flow.
    According the customer's answers, we will provide the next steps.
    """
    while True:
        netoperator = input(
            "What would you like to do?\nType number:\n< 1 > Basic Configuration\n< 2 > Basic Troubleshooting\n")
        if validate_answers(netoperator):
            print("Next...")
            pass
        else:
            continue
        while True:
            type_device = input(
                "Which type of device?\nType number:\n< 1 > Switch\n< 2 > Router\n")
            if validate_answers(type_device):
                print("Next...")
                pass
            else:
                continue
            while True:
                if type_device == '1':
                    layer = input(
                        "Which layer?\nType number:\n< 1 > Layer2\n< 2 > Layer3\n")
                    if validate_answers(layer):
                        print("Next...")
                        pass
                    else:
                        continue
                else:
                    route = input(
                        "Which type of route?\nType number:\n< 1 > Static\n< 2 > Dynamic\n")
                    if validate_answers(route):
                        print("Next...")
                        pass
                    else:
                        continue
                while True:
                    vendor = input(
                        "Which vendor?\nType number:\n< 1 > Cisco\n< 2 > Aruba\n< 3 > Datacom\n< 4 > HP Comware\n")
                    if validate_answers_vendors(vendor):
                        print("Next...")
                        break
                    else:
                        continue
                break
            break
        break


def validate_answers(answer):
    try:
        num = int(answer)
        if num != 1 and num != 2:
            raise ValueError(
                f"Make sure you have writing\n< 1 > or < 2 >\n"
            )
    except ValueError as e:
        print(f"{e}is not accepted. Please try again.\n")
        return False

    return True


def validate_answers_vendors(answer):
    try:
        num = int(answer)
        if num != 1 and num != 2 and num != 3 and num != 4:
            raise ValueError(
                f"Make sure you have writing\n< 1 > or < 2 > or < 3 > or < 4 >\n"
            )
    except ValueError as e:
        print(f"{e}is not accepted. Please try again.\n")
        return False

    return True


basic_questions()
