"""Password Generator"""

import string
import random

ALPHABET_LIST = list(string.ascii_letters)
NUMERICAL_LIST = list(string.digits)
PUNCTUATION_LIST = list(string.punctuation)

DEFAULT_LENGTHS = (5, 3, 2)


def password_length():
    pw_length = int(input("Enter password length, or leave blank for default length."))
    if isinstance(pw_length, int):
        x = pw_length/2
        y = pw_length*(3/10)
        z = pw_length-round(x)-round(y)
        pw_length = (int(x), int(y), int(z))
        return pw_length
    return DEFAULT_LENGTHS


def generate_password(pw_size):
    """
    | Generates 10 digit password.
    """
    password = []
    for i in range(0, pw_size[0]):
        password.append(random.choice(ALPHABET_LIST))
    for i in range(0, pw_size[1]):
        password.append(random.choice(NUMERICAL_LIST))
    for i in range(0, pw_size[2]):
        password.append(random.choice(PUNCTUATION_LIST))
    password = random.sample(password, len(password))
    pw_str = ''
    for i in password:
        pw_str += i
    return pw_str


def user_information(completed_password):
    """
    | Prompts, compiles, organizes user information. Ready to be saved to a file to printed.
    """
    name = input("Your name: \n").capitalize()
    sm_account = input("Name of social media site: \n").capitalize()
    username = input("Username or Email associated with account: \n").capitalize()
    return f"{name}-{sm_account}", f"""Your {sm_account} details are:
Username: {username}
Password: {completed_password}"""


def save_password(file_name, details):
    """
    :param file_name: Creates name for txt file to which details will be saved.
    :param details: Name, Username & Password to be saved.
    :return: Txt file with details added to it.
    """
    with open(file=f"./generated-passwords/save-{file_name}.txt", mode="w") as file:
        file.write(details)


def main():
    compiled_details = user_information(generate_password(password_length()))
    save_password(compiled_details[0], compiled_details[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
