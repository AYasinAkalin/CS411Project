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
It is required to use SHA3 with 256-bit output
as the cryptographic hash function.

Provide a PoW for a single transcation.
Generate at least ten transactions and write them to a file.
'''

# =====================================
# Libraries
# =====================================
import hashlib, sha3 # Used to generate hash value

# Helper functions for Tx generation
from library import transactionHelpers as TxLib


# =====================================
# Functions
# =====================================
# Takes an 'integer'
# Returns 'string'
def findPrevHash(numOfRun):
    # Usage
    # print findPrevHash(4)
    if numOfRun is 0:
        return 'Previous hash in the chain: First transaction'
    else:
        return 'Previous hash in the chain: ' + listHash[numOfRun - 1]


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
    serial = TxLib.generateSerialNum()
    payer = TxLib.generatePayer(lenID)
    payee = TxLib.generatePayee(lenID)
    amount = TxLib.generateAmount(lenAmount)
    hashPrev = findPrevHash(numOfRun)
    nonce = TxLib.generateNonce()

    lines = '\n'.join(
        [header, serial, payer, payee, amount, hashPrev, nonce]) + '\n'
    hashPOW = generatePoW(lines)
    while not hashPOW.startswith('000'):
        nonce = TxLib.generateNonce()  # New nonce value
        lines = '\n'.join(
            [header, serial, payer, payee, amount, hashPrev, nonce]) + '\n'
        hashPOW = generatePoW(lines)
    # Add current PoW to a list so it can be found later
    listHash.append(hashPOW)

    # Create file and write transaction details on it
    hashPOW = 'Proof of Work: ' + hashPOW
    linesToFile = '\n'.join(
        [header, serial, payer, payee, amount, hashPrev, nonce, hashPOW])
    TxLib.writeToFile(linesToFile, fileName)


# =====================================
# Initials
# =====================================
listHash = []
lengthID = 10  # Length of the names of payee and payer
lenPaymentAmount = 3  # Number of digits of transaction amount
numTransactions = 10  # Total number of transactions


# =====================================
# Main
# =====================================
def main():
    print 'Looking for \'proof of work\' hash value.'
    for x in xrange(0, numTransactions):
        generateTransaction(lengthID, lenPaymentAmount, x)
        print 'A PoW value has been found.', listHash[x]
        print '========================================'
        if x is not 9:
            print 'Looking for another one.'
    print numTransactions, 'transactions has been proven and connected.'


if __name__ == "__main__":
    main()
