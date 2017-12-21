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
Random explanation

'''

# =====================================
# Workload
# =====================================
'''
*** Bitcoin transaction ***
Serial number: 129986701613722743128838545549399553824
p: 12376337094338799430773844124977509457217066353 ...
q: 45342338499442214089108938181222870730317855769999072394177227217388872148783
g: 875874273754043385544666877683999314698918600107797140 ...
Payer Public Key (beta): 1064795504184295781499096314130136074379661237724834 ...
Payee Public Key (beta): 1640914200063307349695701322479808357127910275781041 ...
Amount: 905 Satoshi
Signature (r): 66067765116041166658524374136414953666714993823918402058876243 ...
Signature (s): 54222466157856912512740736834055670138544475519297459412760616 ...
'''

# =====================================
# Libraries
# =====================================
import DSA
from library import transactionHelpers as TxLib

# =====================================
# Functions
# =====================================


def GenTxBlockHelper(p, q, g, count):
    # Generation phase
    (alpha1, beta1) = DSA.KeyGen(p, q, g)  # Keys of payer
    (alpha2, beta2) = DSA.KeyGen(p, q, g)  # Keys of payee
    sign1 = DSA.SignGen(message, p, q, g, alpha1, beta1)  # Signature of payer
    sign2 = DSA.SignGen(message, p, q, g, alpha2, beta2)  # Signature of payee

    # Output string generation
    header = '*** Bitcoin transaction ***'
    serial = TxLib.generateSerialNum()
    p_ = 'p: ' + str(p)
    q_ = 'q: ' + str(q)
    g_ = 'g: ' + str(g)
    beta1 = 'Payer Public Key (beta): ' + str(beta1)
    beta2 = 'Payee Public Key (beta): ' + str(beta2)
    amount = TxLib.generateAmount(lenAmount)
    r_ = 'Signature (r): ' + str(sign1[0])  # Signature element of payer
    s_ = 'Signature (s): ' + str(sign1[1])  # Signature element of payer
    linesToBeWritten = '\n'.join(
        [header, serial, p_, q_, g_, beta1, beta2, amount, r_, s_]) + '\n'
    return linesToBeWritten


def GenTxBlock(p, q, g, count):
    fullTransaction = ''
    for x in xrange(0, count):
        fullTransaction += GenTxBlockHelper(p, q, g, count)
    return fullTransaction.rstrip()


def findDSAParams():
    dirDef = TxLib.findDefDir()
    try:
        dirFile = dirDef + "/Outputs/"
        fo = open(dirFile + 'DSA_params.txt', "r")
        q = int(fo.readline())
        p = int(fo.readline())
        g = int(fo.readline())
        fo.close()
    except Exception as e:
        raise e
    return p, q, g


# =====================================
# Initials
# =====================================
message = "Special message for Eylul."
lenAmount = 3  # Number of digits of transactions
lenTxBlock = 8  # Number of transaction information in each file
numberOfFiles = 3  # Number of files containing transaction information

# =====================================
# Main
# =====================================


def main():
    p, q, g = findDSAParams()
    # print GenTxBlock(p, q, g, lenTxBlock)  # Debug
    # print TxLib.generateSerialNum()
    for x in xrange(0, numberOfFiles):
        fName = 'TransactionBlock' + str(x) + '.txt'
        TxLib.writeToFile(GenTxBlock(p, q, g, lenTxBlock), fName)


if __name__ == "__main__":
    main()
