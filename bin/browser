#!/usr/bin/env python3

import webbrowser
import argparse
import json

# use absolute path
configfolder = 'config'
configfile = '{}/browser.json'.format(configfolder)

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--forr', action='store', type=str, help='work, study or play', required=True)

args = parser.parse_args()

with open(configfile) as f:
    config = json.load(f)

browser = config[args.forr]['browser_path']
websites = config[args.forr]['websites']

b = webbrowser.get(browser)

for i in range(len(websites)):
    if i == 0:
        b.open(websites[i])
    else:
        b.open_new_tab(websites[i])
