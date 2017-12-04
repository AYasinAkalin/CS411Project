# CS 411 507 2017 Fall Project - Phase 1
# =====================================
# Team Members
# =====================================
# Ali Yasin Akalin
# Burak Aytac
# Eylul Dicle Yurdakul


# =====================================
# Workload
# =====================================
'''
In this phase of the project, you will generate random transactions following
the format described.
You are required to use SHA3 with 256-bit output
as the cryptographic hash function.

Provide a PoW for a single transcation.
Generate at least ten transactions and write them to a file.
'''

# =====================================
# Libraries
# =====================================
import random

import string  # Used for alphabet generation

import uuid  # Used for 128 bit integer generation
import os  # Used to check if a file is empty or not
# =====================================
# Functions
# =====================================


# Takes one 'int'
# Returns 'int'
def random_with_N_digits(n):
    # Usage
    # threeDigitNumber = random_with_N_digits(3)
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    return random.randint(range_start, range_end)


# Takes one 'int'
# Returns 'string'
def randomName(length):
    # Usage
    # name = randomName(10)
    characters = list(string.ascii_uppercase) + list(string.digits)
    return ''.join(random.sample(characters, length))


# Takes no parameter
# Returns 'long'
def randomInteger128bit():
    # Usage
    # randomInteger = randomInteger128bit()
    x = uuid.uuid4().int
    return x


# Takes no parameter
# Returns 'string'
def generateSerialNum():
    return 'Serial number: ' + str(randomInteger128bit())


# Takes one 'int'
# Returns 'string'
def generatePayer(length):
    # Usage
    # print generatePayer(8)
    return 'Payer: ' + randomName(length)


# Takes one 'int'
# Returns 'string'
def generatePayee(length):
    # Usage
    # print generatePayee(5)
    return 'Payee: ' + randomName(length)


# Takes one 'int'
# Returns 'string'
def generateAmount(numOfDigits):
    # Usage
    # print generateAmount(3)
    return 'Amount: ' + str(random_with_N_digits(numOfDigits)) + ' Satoshi'

# Takes ...
# Returns 'string


def findPrevHash():
    pass


# Takes no parameter
# Returns 'string'
def generateNonce():
    return 'Nonce: ' + str(randomInteger128bit())


# Takes ...
# Returns 'string
def generatePoW():
    pass


def generateTransaction(length, lengthAmount):
    header = '*** Bitcoin transaction ***'
    serial = generateSerialNum()
    payer = generatePayer(length)
    payee = generatePayee(length)
    amount = generateAmount(lengthAmount)
    hashPrev = ''
    nonce = generateNonce()

    lines = header + serial + payer + payee + amount + hashPrev + nonce
    print lines
    hashPOW = ''
    # create file
    #

    writeToFile(lines, 'trial.txt')
    pass


def writeToFile(string, fileName):
    # Open a file
    fo = open(fileName, "a")
    fo.write('\n')
    # Fill the text into the file
    fo.write(string)
    # Close opend file
    fo.close()
# =====================================
# Initials
# =====================================


lengthID = 10

# =====================================
# Main
# =====================================
print '*** Bitcoin transaction ***'
print generateSerialNum()
print generatePayer(lengthID)
print generatePayee(lengthID)
print generateAmount(3)
print generateNonce()

writeToFile('Hi77', 'hi.txt')
print '====='
for x in xrange(1,10):
    generateTransaction(lengthID, 3)

