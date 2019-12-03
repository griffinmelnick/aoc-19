'''
    @name           day-03
    @author         griffinmelnick
    @required       ../ins/day-03.txt
'''

steps = { 'l': (-1, 0), 'u': (0, 1), 'r': (1, 0), 'd': (0, -1) }

def sol_a(ins):
    p1, p2  = set(), set()
    at_p1, at_p2 = (0, 0), (0, 0)
    for s in ins[0]:
        step_dir = s[0].lower()
        for _ in range( int(s[1:]) ):
            at_p1 = ( ( at_p1[0] + steps[step_dir][0] ), ( at_p1[1] + steps[step_dir][1] ) )
            p1.add(at_p1)
    for s in ins[1]:
        step_dir = s[0].lower()
        for _ in range( int(s[1:]) ):
            at_p2 = ( ( at_p2[0] + steps[step_dir][0] ), ( at_p2[1] + steps[step_dir][1] ) )
            p2.add(at_p2)

    crosses = p1.intersection(p2)
    return min( [ sum( abs(i) for i in t ) for t in crosses ] )


def sol_b(ins):
    p1, p2  = dict(), dict()
    at_p1, at_p2 = (0, 0), (0, 0)
    step_p1, step_p2 = 0, 0
    for s in ins[0]:
        step_dir = s[0].lower()
        for _ in range( int(s[1:]) ):
            step_p1 += 1
            at_p1 = ( ( at_p1[0] + steps[step_dir][0] ), ( at_p1[1] + steps[step_dir][1] ) )
            if ( at_p1 not in p1 ):
                p1[at_p1] = step_p1
    for s in ins[1]:
        step_dir = s[0].lower()
        for _ in range( int(s[1:]) ):
            step_p2 += 1
            at_p2 = ( ( at_p2[0] + steps[step_dir][0] ), ( at_p2[1] + steps[step_dir][1] ) )
            if ( at_p2 not in p2 ):
                p2[at_p2] = step_p2

    crosses = set( p1.keys() ).intersection( set( p2.keys() ) )
    return min( [ p1[t] + p2[t] for t in crosses ] )


if ( __name__ == "__main__" ):
    ins = []
    for l in open( "../ins/day-03.txt", 'r' ):
        ins.append( [ x for x in l.strip().split(',') ] )
    print( "Sol. 3a - " + str( sol_a(ins[:]) ) )
    print( "Sol. 3b - " + str( sol_b(ins[:]) ) )

