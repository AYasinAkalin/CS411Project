# Implementing Cryptocurrency with Block Chains
## Introduction
This is the Term Project of CS411 Cryptography Course in Sabanci University.
We were required to develop essential building blocks of cryptocurrency using block chains.

It had three phases:

* Developing software for proof of work
* Developing software for digital signature
* Developing software for other buiding blocks and integration 

## Setup

This software is written in Python 2.7. Unix systems have python by default. To install dependencies on Mac OS X or on Ubuntu bash:

    $ sudo easy_install pip
    $ pip install -r requirements.txt

## Test
To test the whole program, just run:

    $ python setup.py

Test individual modules seperately follow on of the methods.

### Method 1
Change 'True's to 'False' to disable test modules in setup.py

	TestPhase1 = True
	TestPhase2 = True
	TestPhase3 = True

	TestPhase1 = False
	TestPhase2 = True
	TestPhase3 = False

Then run

    $ python setup.py

### Method 2
Or run following codes seperately.
To test Phase 1, run

	$ python ValidateChain.py

To test Phase 2, run

	$ python DSA_Test.py

To test Phase 3, run

	$ python Final_Test.py
