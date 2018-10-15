# BONUS TASK 1
def f(s, n):
    s = s.lower()
    l = list(s)
    result = ''
    for i in l:
        if i.isalpha():
            result += abc[((ord(i) - ord('a')) % 25 + n) % 25]
        else:
            result += i
    return result

import random
import argparse
parser = argparse.ArgumentParser(description='Process input and output.')
parser.add_argument('input', type=str, nargs='+',
                    help='input file')
parser.add_argument('output', type=str, nargs='+',
                    help='output file')
parser.add_argument('type', type=str, nargs='+',
                    help='"encoding" or "decoding"')
args = parser.parse_args()

abc = 'abcdefghijklmnopqrstuvwxyz'

# !!! encoding and decoding key
n = 3


input_file = open(vars(args)['input'][0], 'r')
output_file = open(vars(args)['output'][0], 'w')
Type = vars(args)['type'][0]
for string in input_file:
    for word in string.split():
        if Type == 'encoding':
            output_file.write(' ' + f(word, n))
        else:
            output_file.write(' ' + f(word, -1 * n))
    output_file.write('\n')
output_file.close()
