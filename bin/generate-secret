#!/usr/bin/env python

import argparse
import random
import string

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', action='store', type=int, help='lenth of generated string', default=16)

args = parser.parse_args()

print(''.join([random.choice('{}{}{}'.format(string.ascii_letters, string.digits, string.punctuation)) for _ in range(args.length)]))