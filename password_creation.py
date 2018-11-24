## Password Creation Tool by Dan Pullan (https://danielpullan.co.uk)
## Creates a random password then copies it to your clipboard
## 19/11/2018

import random
import pyperclip
import csv
import sys

secure_random = random.SystemRandom()

input = sys.argv[1]
yarp = ["y", "Y", "yes", "YES", "Yes","yarp", "YARP", "Yarp"]
narp =["n", "N", "no", "NO", "narp", "NARP", "Narp"]

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

if input in yarp:
    pyperclip.copy(completed_password)
    print("Copied to clipboard.")
elif input in narp:
    print("The password is " + completed_password)
else:
    print("Sorry, I didn't understand that")