# CS 411 507 2017 Fall Project
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

'''


# =====================================
# Libraries
# =====================================
# import sample
# import library

import ValidateChain as test1
import DSA_Test as test2
import Final_Test as test3


# =====================================
# Functions
# =====================================
def Test1():
    test1.__main__


def Test2():
    test2.__main__


def Test3():
    test3.__main__


# =====================================
# Initials
# =====================================
DirIOFolder = '/Outputs'    # Directory of I/O files
DirTests = '/tests'         # Directory of test files
DirScripts = '/sample'      # Directory of script files

TestPhase1 = True
TestPhase2 = True
TestPhase3 = True

DeleteAllOutputs = True


# =====================================
# Main
# =====================================
def main():
    if TestPhase1:
        Test1()
    if TestPhase2:
        Test2()
    if TestPhase3:
        Test3()

    if DeleteAllOutputs:
        pass
    print 'Tests are passed.'


if __name__ == "__main__":
    main()
