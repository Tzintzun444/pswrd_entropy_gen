# PSWRD_ENTROPY_GEN PROJECT
This project is a simple but powerful tool to create secure passwords based on **entropy** \(information theory).

## Description
This is a password generator based on entropy in bits, this means that the passwords created can be measured on
how much is possible to guess the password based on its randomness and can calculate how much time it would need to be decrypted.
The generator is a class called Generator \(of course) and has 4 methods involved, which we will see later.

## Installation

To install the package, you only need to use the following command:
```bash
pip install pswrd_entropy_gen
```

Once the package has been installed, import its class "Generator":

```python
from pswrd_entropy_gen import Generator
```

## Characteristics

Class 'Generator' creates a password based on the length provided, it receives as a parameter the required length 
\(integer)of the password, then it creates the password and will return 3 variables: First, the 'generated_password', 
which is the password that was created. Second, the 'entropy_of_password' as its name says, it is the entropy 
related to the password. And finally, the 'decryption_password_time' that is the time required to crack the 
password by brute force attack \(theoretically).

```python
class Generator:
    
    # The class receives the length of the password as an attribute
    # The other attributes are given by the create_password method
    def __init__(self, length):

        self._length = length
        (self._generated_password, self._entropy_of_password,
         self._decryption_password_time) = self.create_password()
    
    # Call the 3 static methods of the class to create their respective attributes
    def create_password(self):
        
        try:
            
            generated_password = self.generate_password(self.length)
            entropy_of_password = self.calculate_entropy(generated_password)
            decryption_password_time = self.calculate_decryption_time(entropy_of_password)

            return generated_password, entropy_of_password, decryption_password_time

        except Exception as exception:
            return f'There was an error: {exception}'
```

### generate_password() function:
The function has 4 parameters:
+ length:
It must be a positive integer \(do not exist decimal or negative passwords), it is recommended to be 8 or 
greater numbers. It is not defined by default.
+ use_uppercase:
It is a boolean value, it is true by default. This means that is allowed to have at least 1 uppercase letter in
the password, it may be more than 1.
+ use_numbers:
Also is a boolean value, true by default. Also means that is allowed to have at least 1 number \(0-9) in the 
password, it may be more than 1.
+ use_punctuations:
And finally, it is a boolean value, true by default. Includes at least 1 punctuation character \(.#$%/! for example)
in the password, also it may be more than 1.

The function uses the 'string' and 'secrets' modules for its functionality. The use of lowercase letters is 
mandatory, and all parameters by default are in the 'situations' dictionary with their respective characters as a
value.

 
```python
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
```

Next, creates the 'password' list, where will be stored all characters of the password. Then, a for loop adds 1 
character of each of the character types if those are 'True' in the parameters above, this ensures that at least
1 of each type was added.

```
password = []

        for character_type in situations.values():

            if character_type[0]:

                characters += character_type[1]
                password.append(secrets.choice(character_type[1]))
```

After that, the length remaining is calculated and with a list comprehension, the necessary characters are chosen 
and added in a list, which is joined with our 'password' list.

```python
remaining = length - len(password)
        random_password = [secrets.choice(characters) for _ in range(remaining)]
        password.extend(random_password)
```

Finally, the characters in the list are randomly shuffled and joined as a string.

```python
secrets.SystemRandom().shuffle(password)

        final_password = ''.join(password)

        return final_password
```

And the password is returned. ¡woohoo!

### calculate_entropy() function:


### calculate_decryption_time function:


## Examples

1. 

