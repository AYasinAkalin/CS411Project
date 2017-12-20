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
def generateSerialNum():
    return 'Serial number: ' + str(RandomGenerator.randomIntegerNbit(128))


# Takes one 'int'
# Returns 'string'
def generateAmount(numOfDigits):
    # Usage
    # print generateAmount(3)
    return 'Amount: ' \
    + str(RandomGenerator.randomIntegerNDigits(numOfDigits)) \
    + ' Satoshi'


def writeToFile(string, fileName):
    dirMain = findDefDir()
    dirFile = dirMain + '/Outputs/'

    # Find if folder is present, otherwise create the folder
    try:
        os.stat(dirFile)
    except:
        os.mkdir(dirFile)   
    
    # Open a file
    fo = open(dirFile + fileName, "a")  # File opens in append mode
    # Fill the text into the file
    fo.write(string)
    fo.write('\n')
    # Close opened file
    fo.close()

# =====================================
# Initials
# =====================================

# =====================================
# Main
# =====================================
def main():
    pass


if __name__ == "__main__":
    main()
