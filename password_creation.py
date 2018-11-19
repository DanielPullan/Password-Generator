## Password Creation Tool by Dan Pullan (https://danielpullan.co.uk)
## Creates a random password then copies it to your clipboard
## 19/11/2018

import random
import pyperclip

secure_random = random.SystemRandom()

first_word = ['Hello', 'Darkness', 'Friend', 'Silent', 'Sunshine', 'Batman', 'Mario', 'Officer', 'Doggo', 'Pupper', 'Elephants']

second_word = ['Goodbye', 'Lightness', 'Enemy', 'Loud', 'Moonshine', 'Robin', 'Luigi', 'Doctor', 'Paddy', 'Kitten', 'Whales']

number = ['3264', '18', '2018', '8664', '2848', '1366', '1922']

def makePassword():
    first = (secure_random.choice(first_word))
    second = (secure_random.choice(second_word))
    last = (secure_random.choice(number))
    password = (first+second+last)
    return password

completed_password = makePassword()

print(completed_password)
pyperclip.copy(completed_password)
print("Copied to clipboard.")