#!/usr/bin/env python3

import requests
import argparse
import shutil
import json
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action='store', type=str, help='path to json file', required=True)
parser.add_argument('-k', '--key', action='store', type=str, help='object key to generate qrcode')
parser.add_argument('-n', '--name', action='store', type=str, help='object key to save as image name')

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

for i, d in enumerate(data):
    info = d[args.key] if args.key is not None else d
    name = d[args.name] if args.name is not None else 'qrcode-{}'.format(i)
    url = 'https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl={}&choe=UTF-8&chld=L|1'.format(info)

    r = requests.post(url, stream=True)
    with open('{}.png'.format(name), 'wb') as output:
        shutil.copyfileobj(r.raw, output)
    del r

print('successfully convert json to qr-code')