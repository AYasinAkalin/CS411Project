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

# Used to generate hash value
import sys
import hashlib
if sys.version_info < (3, 6):
    import sha3
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


# Takes an 'integer'
# Returns 'string'
def findPrevHash(numOfRun):
    # Usage
    # print findPrevHash(4)
    if numOfRun is 0:
        return 'Previous hash in the chain: First transaction'
    else:
        return 'Previous hash in the chain: ' + listHash[numOfRun - 1]


# Takes no parameter
# Returns 'string'
def generateNonce():
    return 'Nonce: ' + str(randomInteger128bit())


# Takes 'string'
# Returns 'string
def generatePoW(string):
    # Usage
    # print generatePoW('s;jdfh;lsdh'fjd;sljfh)
    return hashlib.sha3_256(string).hexdigest()


# Takes three 'integers'. These are:
# -- lenID is number of characters in the name of payer and payee
# -- lenAmount is the number of digit of the amount of transaction
# -- numOfRun is the number of this function running in a loop
# Returns nothing
def generateTransaction(lenID, lenAmount, numOfRun):
    # Usage
    # print generatePoW(12, 5, i)
    fileName = 'output.txt'

    header = '*** Bitcoin transaction ***'
    serial = generateSerialNum()
    payer = generatePayer(lenID)
    payee = generatePayee(lenID)
    amount = generateAmount(lenAmount)
    hashPrev = findPrevHash(numOfRun)
    nonce = generateNonce()

    lines = header + serial + payer + payee + amount + hashPrev + nonce
    hashPOW = generatePoW(lines)
    while not hashPOW.startswith('000000'):
        nonce = generateNonce()  # New nonce value
        lines = header + serial + payer + payee + amount + hashPrev + nonce
        hashPOW = generatePoW(lines)
    listHash.append(hashPOW)  # Add current PoW to a list to found later

    # Create file and write transaction details on it
    hashPOW = 'Proof of Work: ' + hashPOW
    linesToFile = '\n'.join(
        [header, serial, payer, payee, amount, hashPrev, nonce, hashPOW])
    writeToFile(linesToFile, fileName)


def writeToFile(string, fileName):
    # Open a file
    fo = open(fileName, "a")
    # Fill the text into the file
    fo.write(string)
    fo.write('\n')
    # Close opend file
    fo.close()


# =====================================
# Initials
# =====================================
listHash = []
lengthID = 10

# =====================================
# Main
# =====================================
print 'Looking for proof of work hash value.'
for x in xrange(0, 10):
    generateTransaction(lengthID, 3, x)
    print 'A PoW value found.', listHash[x]
    print '=============================================='
print '10 transactions are proven and connected.'
