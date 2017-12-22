# CS 411 507 2017 Fall Project - Phase 3
# =====================================
# Team Members
# =====================================
# Ali Yasin Akalin
# Burak Aytac
# Eylul Dicle Yurdakul


# =====================================
# Info
# =====================================
'''
Generates Proof of Work (PoW) values for previously signed Bitcoin transaction
blocks, writes generated parameters (Previous Pow, Merkle Hash, Nonce, PoW) to
both terminal and a file.

Requires custom python module(s):
    */library/transactionHelpers.py

Functions
    generateMerkleHash(fileName, lenTx): Returns a hash value from a Tx Block
    findPrevPoW(fName): Returns PoW hash value of previous Tx Block
    PoW(TxBlockFile, ChainFile, PoWLen, TxLen): Generates PoW for a Tx Block
        with TxLen number of '0's in the beginning of it
'''


# =====================================
# Libraries
# =====================================
from library import transactionHelpers as TxLib
import hashlib
import sha3


# =====================================
# Functions
# =====================================
def generateMerkleHash(fileName, lenTx):
    '''
    Takes two parameters, returns a single hexadecimal hash value as 'string'
    Opens file containing 2^n number of bitcoin transaction informations.
    Each transaction hashes into a single value. Then each pair of hash value
    hashes into a new single value. This operation keeps going until number of
    hash value is decreased to 1.

    Input(s)
    fileName: (string) Name of the file containing a block of transaction info
    lenTx: (int) Number of lines holding info for a single transaction

    Output
    A 'string' value. It is a hash (SHA3_256) value
        of a transaction block in hex format.
    '''
    content = TxLib.readInputFile(fileName)  # Content of transaction info file
    hashList = []
    numOfTxs = len(content) / lenTx

    # Hash every transaction one by one
    for x in xrange(0, numOfTxs):
        a = "".join(content[x * lenTx:(x + 1) * lenTx])
        h = hashlib.sha3_256(a).hexdigest()
        hashList.append(h)

    # Pick hashes in pairs, combine them as a new hash
    # Continue until there is only one hash
    while len(hashList) != 1:
        tempList = []
        for x in xrange(0, len(hashList), 2):
            oldHash = hashList[x] + hashList[x + 1]
            h = hashlib.sha3_256(oldHash).hexdigest()
            tempList.append(h)
        hashList = tempList
    return hashList[0]


def findPrevPoW(fName=''):
    '''
    Takes a parameter, a file name as string. Returns a string, previous PoW
    hash value of previous transaction block, by either reading the value from
    a file of which name is given or finding it from a global variable, a list.

    Input
    fName: (string) Name of the file containing PoW hash values

    Output
    A 'string' value. It is a PoW of a transaction block in hexadecimal format.
    '''
    if len(listPoWs) is 0:
        try:
            lines = TxLib.readInputFile(fName)
            for x in xrange(3, len(lines), 4):
                # If reading last line, remove new line char
                if x is len(lines) - 1:
                    listPoWs.append(lines[x].rstrip())
                else:
                    listPoWs.append(lines[x])
        except Exception:
            return 'Day Zero Link in the Chain'
    return listPoWs[len(listPoWs) - 1]


def PoW(TxBlockFile, ChainFile, PoWLen, TxLen):
    '''
    Takes 4 parameters. Returns nothing. Calculates a proof of work value per
    transaction block which is related to block comes before it.
    Prints 4 values and some informative messages to screen
    and writes those values to a file.

    Inputs
    TxBlockFile: (string) Name of the file containing a block of transaction info
    ChainFile: (string) Name of the file outputs of this function will be written on
    PoWLen: (int) Number of consequtive zeros required at the beginning of PoW hash
    TxLen: (int) Number of lines in a single transaction

    Output on the screen:
    Looking for a proof of work value.
    Found one.
    Previous PoW Day Zero Link in the Chain
    hashMerkle:  0a5ef716fa67793eb4e9c749f12b7d2ef6e029260d0412fb2fbb7b20d9140c63
    nonce:  336787476443477213007589513908532830366
    Current PoW:  0007eabc927c21078c05f62db9be9c82f25951e92a2ff20f5c55c160a29ea95c
    ========================================

    Output on the file:
    Day Zero Link in the Chain
    992f1da6338e1813f41e3fe46d69b2617cf73af640871c06167646a86b3bb765
    314659532392970585142622764647369548167
    0000e5961e1a639707aa7ebce5e2227a23acc33f44e1a1b3ac6a74d224af413f
    '''
    powPrev = findPrevPoW(ChainFile)
    hashMerkle = generateMerkleHash(TxBlockFile, TxLen)
    powCurrent = ''
    print 'Looking for a proof of work value.'
    while not powCurrent.startswith(PoWLen * '0'):
        nonce = TxLib.generateNonce(True)  # New nonce value
        a = '\n'.join([powPrev, hashMerkle, nonce]) + '\n'
        # print repr(a)  # Debug
        powCurrent = hashlib.sha3_256(a).hexdigest()
    print 'Found one.'
    listPoWs.append(powCurrent)
    print 'Previous PoW', powPrev
    print 'hashMerkle: ', hashMerkle
    print 'nonce: ', nonce
    print 'Current PoW: ', powCurrent
    print '========================================'
    linesToBeWritten = '\n'.join(
        [powPrev, hashMerkle, nonce, powCurrent])
    TxLib.writeToFile(linesToBeWritten, ChainFile)


# =====================================
# Initials
# =====================================
IOFolderDir = '/Outputs'              # Directory of I/O files
nameTxBlockFile = 'TransactionBlock'  # ie. TransactionBlock2.txt
nameChainFile = 'LongestChain.txt'    # Name of output file
PoWLen = 6  # Number of consequtive zeros at the beginning of PoW hash value
TxLen = 10  # Number of lines in a single transaction in a block file
listPoWs = []


# =====================================
# Main
# =====================================
def main():
    for x in xrange(0, 3):
        TxBlockFile = nameTxBlockFile + str(x) + '.txt'
        PoW(TxBlockFile, nameChainFile, PoWLen, TxLen)
    while len(listPoWs) > 0:
        listPoWs.pop()


if __name__ == "__main__":
    main()
