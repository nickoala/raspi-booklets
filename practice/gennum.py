#!/usr/bin/python3

"""
Generate postal codes for regex practice.
"""

import sys
import random

def _digit():
    # Pick a digit between 0-9
    return str(random.choice(range(0, 10)))

def _letter():
    # Pick a letter between A-Z
    return random.choice([chr(i) for i in range(ord('A'), ord('Z')+1)])

def _usa_postal_code():
    return ''.join([_digit() for i in range(0, 5)])

def _canada_postal_code():
    return '{} {}'.format(
            ''.join([_letter(), _digit(), _letter()]),
            ''.join([_digit(), _letter(), _digit()]))

def _uk_postal_code():
    def pick(f, g):
        def h():
            return f() if random.choice([True, False]) else g()
        return h

    def optional(f):
        return pick(f, lambda: '')

    return '{} {}'.format(
            ''.join([_letter(),
                     optional(_letter)(),
                     _digit(),
                     optional(pick(_letter, _digit))()]),
            ''.join([_digit(),
                     _letter(),
                     _letter()]))


# Default addresses
White_House_Address = '1600 Pennsylvania Avenue NW, Washington, DC 20500, USA'
Canadian_PM_Residence_Address = '24 Sussex Drive, Ottawa, ON K1M 1M4, Canada'
UK_PM_Office_Address = '10 Downing Street, Westminster, London SW1A 2AA, UK'

def main():
    try:
        # User can say how many to print. Default = 10
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print('You did not give me a number')
        exit(1)
    else:
        if n <= 0:
            print('The number must be larger than 0')
            exit(1)

    # Always include default addresses and generate the rest
    codes = [White_House_Address] \
                + [_usa_postal_code() for i in range(0, n-1)] \
          + [Canadian_PM_Residence_Address] \
                + [_canada_postal_code() for i in range(0, n-1)] \
          + [UK_PM_Office_Address] \
                + [_uk_postal_code() for i in range(0, n-1)]

    # Shuffle and print
    for c in random.sample(codes, len(codes)):
        print(c)


if __name__ == '__main__':
    main()
