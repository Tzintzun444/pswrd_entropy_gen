import secrets
import string


def generate_password(lenght: int, use_uppercase=True,
                      use_numbers=True, use_punctuations=True) -> str:

    characters = string.ascii_lowercase
    situations = {'uppercase': (use_uppercase, string.ascii_uppercase),
                  'numbers': (use_numbers, string.digits),
                  'punctuations': (use_punctuations, string.punctuation)}
    password = []

    for situation, character_type in situations.items():

        if character_type[0]:

            characters += character_type[1]
            password.append(secrets.choice(character_type[1]))

    remaining = lenght - len(password)
    random_password = [secrets.choice(characters) for _ in range(remaining)]
    password.extend(random_password)

    secrets.SystemRandom().shuffle(password)

    final_password = ''.join(password)

    return final_password


print(generate_password(12))
