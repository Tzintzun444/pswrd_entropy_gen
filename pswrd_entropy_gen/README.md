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
of the password, then it creates the password and will return 3 values: First, the 'generated_password', which is 
the password that was created. Second, the 'entropy_of_password' as its name says, it is the entropy related to the 
password. And finally, the 'decryption_password_time' that is the time required to crack the password 
by brute force attack \(theoretically).

```python
class Generator:
    
    # The class receives the length of the password as an attribute
    # The other attributes are given by the create_password method
    def __init__(self, length):

        self._length = length
        (self._generated_password, self._entropy_of_password,
         self._decryption_password_time) = self.create_password()
    
    # Call the 3 static methods of the class to create their respective values
    def create_password(self):
        
        try:
            
            generated_password = self.generate_password(self.length)
            entropy_of_password = self.calculate_entropy(generated_password)
            decryption_password_time = self.calculate_decryption_time(entropy_of_password)

            return generated_password, entropy_of_password, decryption_password_time

        except Exception as exception:
            return f'There was an error: {exception}'
```

## Examples

1. 

