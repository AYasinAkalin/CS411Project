# CS 411 507 2017 Fall Project
# =====================================
# Team Members
# =====================================
# Ali Yasin Akalin
# Burak Aytac
# Eylul Dicle Yurdakul


# =====================================
# Libraries
# =====================================
import random  # Used for random generators
import string  # Used for alphabet generation
import RandomGenerator
from Crypto.Util import number  # Used to generate prime random numbers
# More info is here: http://pythonhosted.org/pycrypto/
import os
import sys

# =====================================
# Functions
# =====================================
def findDefDir():
    return sys.path[0]


# Takes no parameter
# Returns 'string'
def generateSerialNum(plainOutput=False):
    if plainOutput:
        return str(RandomGenerator.randomIntegerNbit(128))
    return 'Serial number: ' + str(RandomGenerator.randomIntegerNbit(128))


# Takes one 'int'
# Returns 'string'
def generateAmount(numOfDigits=3, plainOutput=False):
    # Usage
    # print generateAmount(3)
    if plainOutput:
        return str(RandomGenerator.randomIntegerNDigits(numOfDigits))
    return 'Amount: ' \
        + str(RandomGenerator.randomIntegerNDigits(numOfDigits)) \
        + ' Satoshi'


# Takes no parameter
# Returns 'string'
def generateNonce(plainOutput=False):
    if plainOutput:
        return str(RandomGenerator.randomIntegerNbit(128))
    return 'Nonce: ' + str(RandomGenerator.randomIntegerNbit(128))


def writeToFile(inpt, fileName, override=False):
    dirDefault = findDefDir()
    dirFile = dirDefault + IOFolderDir

    # Find if the folder is present, otherwise create the folder
    try:
        os.stat(dirFile)
    except Exception:
        os.mkdir(dirFile)

    # Open a file
    if override:
        fo = open(dirFile + '/' + fileName, "w")  # File opens in write mode
    else:
        fo = open(dirFile + '/' + fileName, "a")  # File opens in append mode
    # Fill the text into the file
    fo.write(inpt)
    fo.write('\n')
    # Close opened file
    fo.close()


def readInputFile(fileName):
    dirDefault = findDefDir()
    try:
        dirFile = dirDefault + IOFolderDir + '/' + fileName
        fo = open(dirFile, "r")
        fileContent = fo.readlines()
        fo.close()
    except Exception as e:
        raise e
        return None
    return fileContent


# =====================================
# Initials
# =====================================
IOFolderDir = '/Outputs'


# =====================================
# Main
# =====================================
def main():
    pass


if __name__ == "__main__":
    main()
