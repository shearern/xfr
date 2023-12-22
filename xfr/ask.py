import getpass

def ask(prompt, default=None, required=False):
    """
    Prompt the user for input.

    :param prompt: The prompt message to display to the user.
    :param default: An optional default value if the user enters nothing.
    :param required: Flag to indicate if the input is required.

    :return: The user's input or the default value.
    """
    prompt = prompt.strip().rstrip(':')
    while True:
        # Display the prompt with the default value if it exists
        if default is not None:
            user_input = input(f"{prompt} [{default}]: ")
            # Use the default value if the user input is empty
            if not user_input:
                return default
        else:
            user_input = input(f"{prompt}: ")

        # Check if the input is required
        if required and not user_input:
            print("This input is required. Please enter a value.")
        else:
            return user_input


def ask_pass(prompt, default=None, required=False):
    """
    Prompt the user for input.

    :param prompt: The prompt message to display to the user.
    :param default: An optional default value if the user enters nothing.
    :param required: Flag to indicate if the input is required.

    :return: The user's input or the default value.
    """
    while True:
        # Display the prompt with the default value if it exists
        if default is not None:
            user_input = getpass.getpass(f"{prompt} [keep existing]: ")
            # Use the default value if the user input is empty
            if not user_input:
                return default
        else:
            user_input = getpass.getpass(f"{prompt}: ")

        # Check if the input is required
        if required and not user_input:
            print("This input is required. Please enter a value.")
        else:
            return user_input


def ask_yes_no(prompt, default=None):
    """
    Prompt the user for a yes/no answer.

    :param prompt: The prompt message to display to the user.
    :param default: An optional default value ('yes' or 'no') if the user enters nothing.

    :return: True for 'yes' and False for 'no'.
    """
    while True:
        # Display the prompt with the default value if it exists
        if default is not None:
            user_input = input(f"{prompt} [y/n] (default: {default}): ").strip().lower()
            # Use the default value if the user input is empty
            if not user_input:
                user_input = default
        else:
            user_input = input(f"{prompt} [y/n]: ").strip().lower()

        # Interpret the user's response
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            return False
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


def ask_choose(question, options, allow_custom=False, default=None, required=True):
    """
    Asks a question and presents a list of options for the user to choose from.
    Optionally allows the user to provide a custom answer.
    Allows specifying a default answer.

    :param question: The question to ask
    :param options: A list of options to present
    :param allow_custom: Whether to allow a custom answer
    :param default: The default answer (optional)
    :return: The user's choice
    """

    # Display the question
    question = question.strip().rstrip(':')
    if default:
        question = f"{question} [{default}]"
    print(question)


    # Print options
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    if allow_custom:
        print(f"  {len(options) + 1}. Provide a different answer")

    # Get user input
    while True:
        user_input = input("> ")
        if user_input == '':
            if default is not None:
                return default
            elif required:
                print("This input is required. Please enter a value.")
                continue
            else:
                return None

        try:
            choice = int(user_input)

            # Check if the choice is within the valid range
            if 1 <= choice <= len(options) + (1 if allow_custom else 0):
                # Return the chosen option
                if allow_custom and choice == len(options) + 1:
                    return input("Enter your custom answer: ")
                else:
                    return options[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

