#!/usr/bin/env python

from datetime import datetime

import argparse
import json
import sys
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action='store', type=str, help='path to json file', required=True)
parser.add_argument('-s', '--sort', action='store', type=str, help='json key to sort value')
parser.add_argument('-sd', '--descending', action='store_true', help='sort descending')
parser.add_argument('-hd', '--header', action='append', type=str, help='output headers')
parser.add_argument('-o', '--output', action='append', type=str, help='json keys to output')
parser.add_argument('-td', '--todate', action='append', type=str, help='json keys to transform to date')

args = parser.parse_args()

if not os.path.isfile(args.file):
    print('error: specified path is not a file')
    sys.exit()

if not os.path.exists(args.file):
    print('error: file not exist')
    sys.exit()

if not args.file.endswith('.json'):
    print('error: not json filed given')
    sys.exit()

# load data from file
f = open(args.file)
data = json.load(f)

# sort
if (args.sort):
    data.sort(key=lambda x: x[args.sort], reverse=args.descending)

download = os.path.join(os.path.expanduser('~'), 'downloads')
c = csv.writer(open('{}/output.csv'.format(download), 'w', newline=''))

if (args.header):
    c.writerow(args.header)

for d in data:
    if args.todate:
        for td in args.todate:
            d[td] = datetime.utcfromtimestamp(d[td]).strftime('%Y-%m-%d')

    if args.output:
        c.writerow([d[o] for o in args.output])
    else:
        c.writerow([d[i] for i in d])

print('successfully convert json to csv')