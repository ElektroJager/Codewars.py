from itertools import permutations , product

def plus(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return -1
    return a/b

ops = [(plus,'+'),(sub, '-'), (mul,'*'), (div,'/')]

def equal_to_24(a1,b1,c1,d1):
    perm, op_perm =  permutations([a1,b1,c1,d1]), list(product(ops,repeat = 3))

    for p in perm:
        a, b, c, d = p[0], p[1], p[2], p[3]
        for op in op_perm:
            if op[2][0](op[0][0](a,b),op[1][0](c,d)) == 24: return '({} {} {}) {} ({} {} {})'.format(a,op[0][1],b,op[2][1],c,op[1][1],d)
            if op[0][0](a,op[1][0](b,op[2][0](c,d))) == 24: return '{} {} ({} {} ({} {} {}) )'.format(a,op[0][1],b,op[1][1],c,op[2][1],d)
            if op[0][0](a,op[1][0](op[2][0](b,c),d)) == 24: return '{} {} (({} {} {}) {} {} )'.format(a,op[0][1],b,op[2][1],c,op[1][1],d)
            if op[0][0](op[1][0](a,op[2][0](b,c)),d) == 24: return '({} {} ({} {} {})) {} {}'.format(a,op[1][1],b,op[2][1],c,op[0][1],d)
            if op[0][0](op[1][0](op[2][0](a,b),c),d) == 24: return '(({} {} {}) {} {}) {} {}'.format(a,op[2][1],b,op[1][1],c,op[0][1],d)

    return "It's not possible!"
