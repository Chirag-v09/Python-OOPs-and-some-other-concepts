# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:06:52 2021

@author: Chirag
"""


import math
import argparse

parser = argparse.ArgumentParser(description="Calculate Area of the Rectangle")
parser.add_argument('-l', '--length', type = int, metavar = '', required = True, help = "Length of Rectangle")
parser.add_argument('-b', '--breath', type = int, metavar = '', required = True, help = "Breath of Rectangle")
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action = 'store_true', help = 'print quiet')
group.add_argument('-v', '--verbose', action = 'store_true', help = 'print verbose')
args = parser.parse_args()


def rectangle_area(length, breath):
    return length*breath

if __name__ == '__main__':
    area = rectangle_area(args.length, args.breath)
    if args.quiet:
        print(area)
    elif args.verbose:
        print(f'Area of rectangle is {area} and length is {args.length} and breath is {args.breath}')
    else:
        print(f'Area of rectangle is {area}')
