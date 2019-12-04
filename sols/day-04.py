'''
    @name           day-04
    @author         griffinmelnick
    @required       ../ins/day-04.txt
'''

import re

def sol_a(ins):
    start, end, count = int(ins[0]), int(ins[1]), 0
    for i in range(start, end):
        split = str(i)
        inc = list(split) == sorted(split)
        dbl = True in [ (len(lh) >= 2) for lh, rh in re.findall(r'((.)\2*)', split) ]
        count += (inc and dbl)
    return count


def sol_b(ins):
    start, end, count = int(ins[0]), int(ins[1]), 0
    for i in range(start, end):
        split = str(i)
        inc = list(split) == sorted(split)
        dbl = True in [ (len(lh) == 2) for lh, rh in re.findall(r'((.)\2*)', split) ]
        count += (inc and dbl)
    return count


if ( __name__ == "__main__" ):
    ins = [ l.strip().split('-') for l in open( "../ins/day-04.txt", 'r' ) ]
    print( "Sol. 4a - " + str( sol_a(ins[0]) ) )
    print( "Sol. 4b - " + str( sol_b(ins[0]) ) )

