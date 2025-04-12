import math
import secrets
import string


def generate_password(length: int, use_uppercase=True,
                      use_numbers=True, use_punctuations=True) -> str:

    characters = string.ascii_lowercase
    situations = {'uppercase': (use_uppercase, string.ascii_uppercase),
                  'numbers': (use_numbers, string.digits),
                  'punctuations': (use_punctuations, string.punctuation),
                  }
    password = []

    for character_type in situations.values():

        if character_type[0]:

            characters += character_type[1]
            password.append(secrets.choice(character_type[1]))

    remaining = length - len(password)
    random_password = [secrets.choice(characters) for _ in range(remaining)]
    password.extend(random_password)

    secrets.SystemRandom().shuffle(password)

    final_password = ''.join(password)

    return final_password


def calculate_entropy(password: str):

    unique_characters = set(password)
    length_password = len(password)
    argument_log = 0

    situations = {'uppercase': (string.ascii_uppercase, 26),
                  'lowercase': (string.ascii_lowercase, 26),
                  'numbers': (string.digits, 10),
                  'punctuations': (string.punctuation, 32),
                  }

    for character_type, posibilities in situations.values():

        if any(character in character_type for character in unique_characters):

            argument_log += posibilities

    entropy = length_password * math.log2(argument_log) if length_password > 0 else 0

    return entropy
