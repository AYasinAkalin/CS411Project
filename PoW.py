# CS 411 507 2017 Fall Project - Phase 3
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
from library import transactionHelpers as TxLib
import hashlib
import sha3


# =====================================
# Functions
# =====================================
# lenTx is the length of a single transaction information written in the file
def generateMerkleHash(fileName, lenTx):
    ''' 
    Function explanation
    lenTx: (int) Number of lines holding info for a single transaction
    '''
    content = TxLib.readInputFile(fileName)
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


def findPrevPoW(fName):
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
# Number of lines holding info for single transaction
TxLen = 10  # Number of lines in a transaction
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
