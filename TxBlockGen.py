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
Creates imaginary signed Bitcoin transactions and
write them on a number of file(s).

Requires custom python modules:
    */DSA.py
    */library/transactionHelpers.py

Functions
    GenTxBlockHelper(p, q, g): Returns a single transaction info.
    GenTxBlock(p, q, g, count): Returns 'count' number of transaction info.
    findDSAParams(): Finds and returns already created DSA initial params
        p, q, g.
'''


# =====================================
# Libraries
# =====================================
import DSA
import sys
from library import transactionHelpers as TxLib


# =====================================
# Functions
# =====================================
def GenTxBlockHelper(p, q, g):
    '''
    Takes initial DSA parameters, generates random bitcoin transaction info.
    Generates keys for payer and payee. Signs transaction info with payers key.
    Then combines every public parameter into a string.

    Inputs
    p: DSA parameter. Numeric value
    q: DSA parameter. Numeric value
    g: DSA parameter. Numeric value

    Output
    Single bitcoin transaction information as string.

    Output Example
    *** Bitcoin transaction ***
    Serial number: 129986701613722743128838545549399553824
    p: 12376337094338799430773844124977509457217066353 ...
    q: 453423384994422140891089381812228707303 ...
    g: 87587427375404338554466687768399931469891860010 ...
    Payer Public Key (beta): 1064795504184295781499096314130136074379661237 ...
    Payee Public Key (beta): 1640914200063307349695701322479808357127910275 ...
    Amount: 905 Satoshi
    Signature (r): 66067765116041166658524374136414953666714993823918402053 ...
    Signature (s): 54222466157856912512740736834055670138544475519292760616 ...
    '''
    # Key Generation phase
    (alpha1, beta1) = DSA.KeyGen(p, q, g)  # Keys of payer
    (alpha2, beta2) = DSA.KeyGen(p, q, g)  # Keys of payee

    header = '*** Bitcoin transaction ***'
    serial = TxLib.generateSerialNum()
    p_ = 'p: ' + str(p)
    q_ = 'q: ' + str(q)
    g_ = 'g: ' + str(g)
    beta1_ = 'Payer Public Key (beta): ' + str(beta1)
    beta2_ = 'Payee Public Key (beta): ' + str(beta2)
    amount = TxLib.generateAmount(lenAmount)
    message = '\n'.join([
        header, serial, p_, q_, g_, beta1_, beta2_, amount]) + '\n'

    # Signature generation
    sign = DSA.SignGen(message, p, q, g, alpha1, beta1)  # Signature of payer
    r_ = 'Signature (r): ' + str(sign[0])  # Signature element of payer
    s_ = 'Signature (s): ' + str(sign[1])  # Signature element of payer

    # Output string generation
    linesToBeWritten = '\n'.join(
        [header, serial, p_, q_, g_, beta1_, beta2_, amount, r_, s_]) + '\n'
    return linesToBeWritten


def GenTxBlock(p, q, g, count):
    '''
    Takes 4 parameters. Returns a transaction block as a string.
    Look to GenTxBlockHelper function for more details.

    Inputs
    p: DSA parameter. Numeric value
    q: DSA parameter. Numeric value
    g: DSA parameter. Numeric value
    count: Number of transactions in transaction block. Integer
        This number must be power of 2.

    Output
    'Count' number of transaction info as a string.
    '''
    fullTransaction = ''
    for x in xrange(0, count):
        fullTransaction += GenTxBlockHelper(p, q, g)
    return fullTransaction.rstrip()


def findDSAParams(fileName='DSA_params.txt'):
    '''
    Takes a string parameter for file operation.
    Returns initial DSA parameters, namely p, q, g.

    Input
    fileName: Name of the file containing q, p, g respectively inside.
        Default is 'DSA_params.txt'

    Outputs
    p: DSA parameter. Numeric value
    q: DSA parameter. Numeric value
    g: DSA parameter. Numeric value
    '''
    content = TxLib.readInputFile(fileName)
    q = int(content[0])
    p = int(content[1])
    g = int(content[2])
    return p, q, g


# =====================================
# Initials
# =====================================
lenAmount = 3       # Number of digits of transactions
NumOfTxBlock = 8    # Number of transaction information in each file
numberOfFiles = 3   # Number of files containing transaction information


# =====================================
# Main
# =====================================
def main():
    print 'Path is:', sys.path[0]
    p, q, g = findDSAParams()
    # print GenTxBlock(p, q, g, NumOfTxBlock)  # Debug
    # print TxLib.generateSerialNum()
    for x in xrange(0, numberOfFiles):
        fName = 'TransactionBlock' + str(x) + '.txt'
        TxLib.writeToFile(GenTxBlock(p, q, g, NumOfTxBlock), fName)


if __name__ == "__main__":
    main()
