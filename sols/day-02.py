'''
    @name           day-02
    @author         griffinmelnick
    @required       ../in/day-02.txt
'''

def sol_a(ins):
    ''' account for "1202 program alarm" '''
    ins[1] = 12
    ins[2] = 2

    i = 0
    while True:
        opcode = ins[i]
        if ( opcode != 99 ):
            i1, i2, i3 = ins[ (i+1) : (i+4) ]
            ins[i3] = (ins[i1] + ins[i2]) if opcode == 1 else (ins[i1] * ins[i2])
        else:
            break
        i += 4
    return ins[0]


def sol_b(ins):
    for noun in range(0, 100):
        for verb in range(0, 100):
            tmp_ins = ins[:]
            tmp_ins[1], tmp_ins[2] = noun, verb

            i = 0
            while True:
                opcode = tmp_ins[i]
                if ( opcode != 99 ):
                    i1, i2, i3 = tmp_ins[ (i+1) : (i+4) ]
                    tmp_ins[i3] = (tmp_ins[i1] + tmp_ins[i2]) if opcode == 1 else (tmp_ins[i1] * tmp_ins[i2])
                else:
                    break
                i += 4

            if ( tmp_ins[0] == 19690720 ):
                return 100 * noun + verb


if ( __name__ == "__main__" ):
    ins = []
    for l in open( "../in/day-02.txt", 'r' ):
        ins += [ int(n) for n in l.strip().split(',') ]
    print( "Sol. 2a - " + str( sol_a(ins[:]) ) )
    print( "Sol. 2b - " + str( sol_b(ins[:]) ) )

