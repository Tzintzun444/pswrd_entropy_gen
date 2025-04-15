import math
import secrets
import string
from typing import Union


class Generator:

    def __init__(self, length):

        self._length = length
        (self._generated_password, self._entropy_of_password,
         self._decryption_password_time) = self.create_password()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def generated_password(self):
        return self._generated_password

    @generated_password.setter
    def generated_password(self, generated_password):
        self._generated_password = generated_password

    @property
    def entropy_of_password(self):
        return self._entropy_of_password

    @entropy_of_password.setter
    def entropy_of_password(self, entropy_of_password):
        self._entropy_of_password = entropy_of_password

    @property
    def decryption_password_time(self):
        return self._decryption_password_time

    @decryption_password_time.setter
    def decryption_password_time(self, decryption_password_time):
        self._decryption_password_time = decryption_password_time

    @staticmethod
    def generate_password(length: int, use_uppercase=True,
                          use_numbers=True, use_punctuations=True) -> str:

        if length <= 0:
            raise ValueError('The number must be a positive integer')

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

    @staticmethod
    def calculate_entropy(password: str, decimals: int = 1) -> Union[int, float]:

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

        return round(entropy, decimals)

    @staticmethod
    def calculate_decryption_time(entropy: Union[int, float],
                                  decimals: int = 2, attempts_per_second=1e12) -> Union[int, float]:

        seconds_per_year = 60 * 60 * 24 * 365

        combinations = 2 ** entropy
        decryption_time_in_seconds = combinations / attempts_per_second
        decryption_time_in_years = decryption_time_in_seconds / seconds_per_year

        return round(decryption_time_in_years, decimals)

    def create_password(self):
        try:
            generated_password = self.generate_password(self.length)
            entropy_of_password = self.calculate_entropy(generated_password)
            decryption_password_time = self.calculate_decryption_time(entropy_of_password)

            return str(generated_password), entropy_of_password, decryption_password_time

        except Exception as exception:
            return f'There was an error: {exception}'

    def __str__(self):
        return (f'The password generated is: {self.generated_password}\n'
                f'Entropy={self.entropy_of_password}\n'
                f'The time necessary to decrypte it is {self.decryption_password_time} years')


generator = Generator(12)
print(generator)
print(type(generator.generate_password(12)))
