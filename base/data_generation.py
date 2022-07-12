import secrets
import string
from random import randint


def name_email():
    pass


def domain_section():
    pass


def domain_zone():
    pass


def gen_email():
    pass

# valid password
def gen_password():
    alphabet = string.ascii_letters
    numbers = string.digits
    punctuation = ' '
    chars = '@'

    sell = alphabet + numbers + punctuation + chars
    len_password = randint(8, 16)

    while True:
        password = ''.join(secrets.choice(sell) for i in range(len_password)).strip()
        if sum(c.isdigit() for c in password) >= 1 \
                and any(c.isupper() for c in password) \
                and any(c.islower() for c in password) \
                and any(c == '@' for c in password):
            for i in range(len(password) - 1):
                if (max(c == ' ' for c in password) == 1) \
                        or (password[i] == punctuation and password[i + 1] != punctuation):
                    break
            break
    return password
