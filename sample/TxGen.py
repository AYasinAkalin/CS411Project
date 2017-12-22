# CS 411 507 2017 Fall Project - Phase 2
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
'''

# =====================================
# Libraries
# =====================================
import DSA
from Crypto.Util import number  # Used to generate prime random numbers
# More info is here: http://pythonhosted.org/pycrypto/

import random  # Used for random generators
import string  # Used for alphabet generation


# =====================================
# Functions
# =====================================


# Takes an 'integer' parameter
# Returns 'long'
def randomIntegerNbit(bitLength):
    # Usage
    # randomInteger = randomIntegerNbit(256)
    return number.getRandomNBitInteger(bitLength)


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
# Returns 'string'
def generateSerialNum():
    return 'Serial number: ' + str(randomIntegerNbit(128))


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


def GenSingleTx(p, q, g, alpha, beta):
    DSA_params = [p, q, g, alpha, beta]
    m = genMessageToHash(DSA_params)
    (r, s) = DSA.SignGen(m, p, q, g, alpha, beta)
    r = 'Signature (r): ' + str(r)
    s = 'Signature (s): ' + str(s)
    linesToBeWritten = '\n'.join(
        [m.rstrip(), r, s]) + '\n'
    return linesToBeWritten


def genMessageToHash(DSA_params, lenID=10, lenAmount=3):
    # DSA_params is a list containing p, q, g, alpha, beta
    header = '*** Bitcoin transaction ***'
    serial = generateSerialNum()
    payer = generatePayer(lenID)
    payee = generatePayee(lenID)
    amount = generateAmount(lenAmount)
    p = 'p: ' + str(DSA_params[0])
    q = 'q: ' + str(DSA_params[1])
    g = 'g: ' + str(DSA_params[2])
    beta = 'Public Key (beta): ' + str(DSA_params[4])
    linesToBeHashed = '\n'.join(
        [header, serial, payer, payee, amount, p, q, g, beta]) + '\n'
    return linesToBeHashed


def writeToFile(string, fileName):
    # Open a file
    fo = open(fileName, "a")  # File opens in append mode
    # Fill the text into the file
    fo.write(string)
    fo.write('\n')
    # Close opened file
    fo.close()


# =====================================
# Initials
# =====================================
lengthID = 10  # Length of the names of payee and payer
outputFiles = ['DSA_params.txt', 'DSA_pkey.txt',
               'DSA_skey.txt', 'SingleTransaction.txt']
# =====================================
# Main
# =====================================


def main():
    # DEPRECATED
    # returns a list containing p, q, g, r, s, beta
    # publicParams = DSA.main()

    # returns a list containing p, q, g, alpha, beta
    initParams = DSA.main()

    # Print SingleTransaction.txt file
    lines = GenSingleTx(initParams[0], initParams[1],
                        initParams[2], initParams[3], initParams[4])
    writeToFile(lines.rstrip(), outputFiles[3])
    print 'All text files are created.'


if __name__ == "__main__":
    main()
