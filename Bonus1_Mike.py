# BONUS TASK 1
def f(s):
    l = list(s)
    random.shuffle(l)
    result = ''.join(l)
    return result

import random
import argparse
parser = argparse.ArgumentParser(description='Process input and output.')
parser.add_argument('input', type=str, nargs='+',
                    help='input file')
parser.add_argument('output', type=str, nargs='+',
                    help='output file')
args = parser.parse_args()

input_file = open(vars(args)['input'][0], 'r')
output_file = open(vars(args)['output'][0], 'w')
for string in input_file:
    for word in string.split():
        if not word.isalpha():
            output_file.write(' ' + word[0] + f(word[1:-2]) + word[-2:])
        elif len(word) == 1:
            output_file.write(' ' + word)
        else:
            output_file.write(' ' + word[0] + f(word[1:-1]) + word[-1])
    output_file.write('\n')
output_file.close()