#!/usr/bin/python3

import os


for line in open('/home/nicohille/Downloads/sshdlog'):
    if "invalid user" in line:
        print(line)


