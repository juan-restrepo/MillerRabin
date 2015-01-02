MillerRabin
===========

Python code implementing the Miller-Rabin primality test


This code asks the user to imput a positive integer and the desired number of times the test will be run (as it is a probabilistic test, it will need to be run multiple times to minimize the chance of a false positive).

It has fast exponentiation included, to speed up calculations.

It prints the randomly chosen integers used for the test and a list with the large odd power and the subsequent squares that shows where the test determines a number is composite, if at all.
