import secrets
import string
from random import randint, choice
import csv
import names
import faker
from data.data import Person

faiker_en = faker.Faker('en')

# valid password
def generated_password() -> str:
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    numbers = string.digits
    space = ' '
    char = '@'

    sell = lower_alphabet + upper_alphabet + numbers + space + char
    # len_password = 7
    len_password = randint(8, 16)

    while True:
        password = ''.join(secrets.choice(sell) for i in range(len_password)).strip()
        if sum(c.isdigit() for c in password) >= 1 \
                and any(c.isupper() for c in password) \
                and any(c.islower() for c in password) \
                and any(c == char for c in password):
            for i in range(len(password) - 1):
                if (max(c == space for c in password) == 1) \
                        or ((password[i] == c for c in char) and (password[i+1] not in char)):
                    break
            break
    return password

def generated_person():
    return Person(
        name=faiker_en.first_name(),
        surname=faiker_en.last_name(),
        email=faiker_en.email(),
        password=generated_password()
    )


# def name_email() -> str:
#     lower_alphabet = string.ascii_lowercase
#     upper_alphabet = string.ascii_uppercase
#     numbers = string.digits
#     punctuation = ['.', '-', '_']
#
#     sell = lower_alphabet + upper_alphabet + numbers + ''.join(punctuation)
#     # len_name = 6
#     len_name = randint(4, 32)
#
#     while True:
#         name = ''.join(choice(sell) for i in range(len_name))
#
#         if name[0] not in punctuation and name[-1] not in punctuation:
#             for i in range(len(name)):
#                 if (name[i] == c for c in punctuation) and (name[i+1] not in punctuation):
#                     return name

# # valid name
# def generated_name() -> str:
#     return names.get_first_name()
#
# # valid surname
# def generated_surname() -> str:
#     return names.get_last_name()

# # valid mail
# def generated_email() -> str:
#     list_domain = ['com', 'org', 'net', 'biz', 'mobi', 'pro', 'info']
#
#     with open('generator/src/service_mail.csv', 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         second_domains = [row for row in reader]
#     f.close()
#
#     with open('generator/src/country_domains.csv', 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         first_domains = [row[1] for row in reader if row[1] not in list_domain]
#     f.close()
#
#     second_domain = choice(second_domains)[0]
#
#     if second_domain in ['gmail', 'yahoo', 'hotmail', 'outlook', 'ya']:
#         return name_email() + '@' + second_domain + '.' + 'com'
#     else:
#         return name_email() + '@' + second_domain + '.' + choice(first_domains + list_domain)[0]

