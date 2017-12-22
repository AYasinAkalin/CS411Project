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

from Crypto.Util import number  # Used to generate prime random numbers
# More info is here: http://pythonhosted.org/pycrypto/


# =====================================
# Functions
# =====================================
# Takes an 'integer' parameter
# Returns 'long'
def randomIntegerNbit(bitLength):
    # Usage
    # randomInteger = randomIntegerNbit(256)

    # Old version
    # return random.getrandbits(bitLength)

    return number.getRandomNBitInteger(bitLength)


# Takes one 'int'
# Returns 'int'
def randomIntegerNDigits(n):
    # Usage
    # threeDigitNumber = randomIntegerNDigits(3)
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    return random.randint(range_start, range_end)


def randomInteger(ceil=None, floor=0):
    if floor is 0:
        try:
            return int(random.uniform(0, ceil))
            # return int(((random.random()) * (ceil + 1)))
        except Exception as e:
            raise e
    else:
        try:
            return random.randint(floor, ceil)
        except Exception as e:
            raise e
    pass


# Takes an 'integer' parameter
# Returns 'long'
def randomPrimeNbit(bitLength):
    # Usage
    # randomPrime = randomPrimeNbit(512)
    return number.getPrime(bitLength)


# Takes one 'int'
# Returns 'string'
def randomName(length):
    # Usage
    # name = randomName(10)
    characters = list(string.ascii_uppercase) + list(string.digits)
    return ''.join(random.sample(characters, length))


# Takes 'integer'
# Returns 'integer'
def checkBitLength(n):
    # Usage
    # >>> checkBitLength(100)
    # 7
    return n.bit_length()


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
