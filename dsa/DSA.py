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
Generate prime number p, q; and a generator g. Write them in a .txt file.

q is 256 bit integer.
p is 2048 bit integer.
q|p-1: q divides p minus 1
g is a generator. It generates a subgroup of Z*_p with q number of elements.
'''

# =====================================
# Libraries
# =====================================
import random  # Used for random generators

# Not used anymore, because this is not reliable as Crypto library
# import pyprimes  # Used to check primeness of numbers

from Crypto.Util import number  # Used to generate prime random numbers
# More info is here: http://pythonhosted.org/pycrypto/

# Used to generate hash value
import sys
import hashlib
if sys.version_info < (3, 6):
    import sha3


# =====================================
# Functions
# =====================================
# Takes 'integer'
# Returns 'integer'
def checkBitLength(n):
    # Usage
    # >>> checkBitLength(100)
    # 7
    return n.bit_length()


def writeToFile(string, fileName):
    # Open a file
    fo = open(fileName, "a")  # File opens in append mode
    # Fill the text into the file
    fo.write(string)
    fo.write('\n')
    # Close opened file
    fo.close()


# Takes one number
# Returns a 'long' number
def generate_p(p_Len, q):
    print 'Looking  for a  \'p\'.'
    try:
        p_Len = bitLen_p
        q_Len = bitLen_q
    except NameError as e:
        p_Len = 2048
        q_Len = 256
    except Exception as e:
        raise e
    while True:
        temp = number.getRandomNBitInteger(p_Len - q_Len)
        p = q * temp + 1
        if number.isPrime(p) and checkBitLength(p) == p_Len:
            if (p - 1) % q == 0:
                break
    print 'Found one!'
    return p


# Takes no parameter
# Returns a 'long' number
def generate_q(q_Len):
    try:
        q_Len = bitLen_q
    except NameError as e:
        q_Len = 256
    except Exception as e:
        raise e
    while True:
        q = number.getPrime(q_Len)
        print 'q generated'
        if number.isPrime(q) and checkBitLength(q) == q_Len:
            break
    return q


# Takes two numbers
# Returns a number, a generator
def generate_g(p, q):
    while True:
        a = random.randint(0, p)
        temp = (p - 1) / q
        g = pow(a, temp, p)
        if (g % p) != 1:
            return g


# Takes no parameter
# Returns 3 'long'
def DL_Param_Generator(small_bound, large_bound):
    q = generate_q(small_bound)
    p = generate_p(large_bound, q)
    # g is a generator of a subgroup in Z*_p with q elements
    g = generate_g(p, q)
    return q, p, g


# Takes initial DSA parameters
# Returns private and public keys respectively
def KeyGen(p, q, g):
    alpha = random.randint(0, q)  # 0 < alpha < q
    return (alpha, pow(g, alpha, p))


# Takes public DSA elements
# Returns signature parameters
def SignGen(message, p, q, g, alpha, beta):
    # Message hashed using SHA3 and returned in hex
    h = hashlib.sha3_256(message).hexdigest()
    h = int(h, 16)  # Hash converted into decimal
    h = h % q

    k = random.randint(0, q)  # Takes a random int between 0 and q
    r = (pow(g, k, p)) % q  # r = (g^k (mod p)) (mod q)
    s = (alpha * r + k * h) % q  # s = (alpha*r + k*h) (mod q)
    return (r, s)  # Return signature elements


# Takes 7 parameters.
# Aside from the message, those are public parameters of DSA
# Returns a 'string' message.
def SignVer(message, r, s, p, q, g, beta):
    # Message hashed using SHA3 and returned in hex
    h = hashlib.sha3_256(message).hexdigest()
    h = int(h, 16)  # Hash converted into decimal
    h = h % q

    v = number.inverse(h, q)  # Return the inverse of h mod q.
    z_1 = (s * v) % q
    z_2 = ((q - r) * v) % q
    u = (pow(g, z_1, p) * pow(beta, z_2, p)) % p
    # u = g^z_1 * beta^z_2 (mod p)
    if r == (u % q):
        print 'Accepted'
        return 1
        # return 'Accepted.'
    else:
        print 'Rejected'
        return 0
        # return 'Rejected.'


# =====================================
# Initials
# =====================================
outputFiles = ['DSA_params.txt', 'DSA_pkey.txt',
               'DSA_skey.txt', 'SingleTransaction.txt']
bitLen_p = 2048
bitLen_q = 256
q__ = 65551171644048854335181462879371743212664500566064056242121626458339348803607
p__ = 16884640886488047401237666558668516796981597367205419586509389007849824870829537040479464466870711267255932960020315339220349192484372157236061918158667506868940599327763363813731299460491316503345869876259583550985332605841551186324345197600803782071574244669010466971446641141400285718866808680561360384647685888723498410943657808897136004654359916711019879363413031007210057289416821000345567956231423296177708071149758425889248762916065060677665260237247585588806641263947576457518507588399642291825208334646045307980743638188901898032068685409150584091095330775211678303390226107718670997737265833806564263277147
m = 'Special message for Eylul.'

# =====================================
# Main
# =====================================
def main():
    q, p, g = DL_Param_Generator(bitLen_q, bitLen_p)
    # Print DSA_params.txt file
    lines = '\n'.join([str(q), str(p), str(g)])
    writeToFile(lines, outputFiles[0])

    (alpha, beta) = KeyGen(p, q, g)
    # Print DSA_pkey.txt file
    lines = '\n'.join([str(q), str(p), str(g), str(beta)])
    writeToFile(lines, outputFiles[1])
    # Print DSA_skey.txt file
    lines = '\n'.join([str(q), str(p), str(g), str(alpha)])
    writeToFile(lines, outputFiles[2])
    (r, s) = SignGen(m, p, q, g, alpha, beta)

    # print SignVer(m, p, q, g, r, s, beta)
    SignVer(m, r, s, p, q, g, beta)
    
    initialParameters = [p, q, g, alpha ,beta]
    publicParameters = [p, q, g, beta, r, s]
    secretParameters = [alpha]
    return initialParameters


if __name__ == "__main__":
    main()
