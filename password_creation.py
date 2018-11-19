## Password Creation Tool by Dan Pullan (https://danielpullan.co.uk)
## Creates a random password then copies it to your clipboard
## 19/11/2018

import random
import pyperclip
import csv

secure_random = random.SystemRandom()

def getFirstWord():
    lines = [line.rstrip('\n') for line in open('first.txt')]
    return(lines)

def getSecondWord():
    lines = [line.rstrip('\n') for line in open('second.txt')]
    return(lines)

def getNumber():
    lines = [line.rstrip('\n') for line in open('numbers.txt')]
    return(lines)

firstWord = getFirstWord()
secondWord = getSecondWord()
number = getNumber()

def makePassword():
    firstBit = (secure_random.choice(firstWord))
    secondBit = (secure_random.choice(secondWord))
    numberBit = (secure_random.choice(number))
    password = (firstBit+secondBit+numberBit)
    return password

completed_password = makePassword()

print(completed_password)
pyperclip.copy(completed_password)
print("Copied to clipboard.")