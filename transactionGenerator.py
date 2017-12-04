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
# =====================================
# Functions
# =====================================


def random_with_N_digits(n):
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    return random.randint(range_start, range_end)


def randomName(length):
    characters = list(string.ascii_uppercase) + list(string.digits)
    return ''.join(random.sample(characters, length))


def randomInteger128bit():
    x = uuid.uuid4().int
    return x


# =====================================
# Initials
# =====================================


# =====================================
# Main
# =====================================

print random_with_N_digits(3)
print randomName(10)

randomInteger = randomInteger128bit()
print randomInteger, len(str(randomInteger))
