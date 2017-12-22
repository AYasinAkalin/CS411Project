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
# Helper functions for Tx generation
from library import transactionHelpers as TxLib


# =====================================
# Functions
# =====================================
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
    serial = TxLib.generateSerialNum()
    payer = TxLib.generatePayer(lenID)
    payee = TxLib.generatePayee(lenID)
    amount = TxLib.generateAmount(3)
    p = 'p: ' + str(DSA_params[0])
    q = 'q: ' + str(DSA_params[1])
    g = 'g: ' + str(DSA_params[2])
    beta = 'Public Key (beta): ' + str(DSA_params[4])
    linesToBeHashed = '\n'.join(
        [header, serial, payer, payee, amount, p, q, g, beta]) + '\n'
    return linesToBeHashed


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
    TxLib.writeToFile(lines.rstrip(), outputFiles[3])
    print 'All text files are created.'


if __name__ == "__main__":
    main()
