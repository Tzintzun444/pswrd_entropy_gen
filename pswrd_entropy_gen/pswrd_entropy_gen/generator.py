import secrets
import string


def possible_characters(use_uppercase=True, use_numbers=True, use_punctuations=True):

    characters = string.ascii_lowercase
    situations = {use_uppercase: string.ascii_uppercase,
                  use_numbers: string.digits,
                  use_punctuations: string.punctuation}

    for situation, character_type in situations.items():

        if type:

            characters += character_type

    return characters


