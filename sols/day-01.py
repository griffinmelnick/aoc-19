'''
    @name           day-01
    @author         griffinmelnick
    @required       ../ins/day-01.txt
'''

import math

''' recursive helper to sum all values down to 0 '''
def sol_b_helper(n):
    tmp = math.floor(n/3) - 2
    if ( tmp <= 0 ):
        return 0
    else:
        return tmp + sol_b_helper(tmp)


def sol_a(ins):
    return sum( [ ( math.floor(n/3) - 2 ) for n in ins ] )


def sol_b(ins):
    return sum( [ sol_b_helper(n) for n in ins ] )


if ( __name__ == "__main__" ):
    ins = [ int( l.strip() ) for l in open( "../ins/day-01.txt", 'r' ) ]
    print( "Sol. 1a - " + str( sol_a(ins[:]) ) )
    print( "Sol. 1b - " + str( sol_b(ins[:]) ) )

