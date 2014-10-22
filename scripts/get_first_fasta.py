# print first <n> elements from fasta

import sys, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:")
except getopt.GetoptError:
    exit(2)

if len(opts) < 2:
    print('script.py -n <number> -f <source_file>')
    exit(1)

for opt, arg in opts:
    if opt in "-n":
        n = int(arg)
    elif opt in "-f":
        source_file = arg

f = open(source_file, "r")

count = 0

for line in f:
    s = line.strip()

    if s[0:1] == '>':
        count += 1

    if count > n:
        break

    print(s)

