#!python3

def factorPair(a,factor):
    b=int(a/factor)
    if b>= factor:
        List=[factor,b]
        return List
    else:
        List=[b,factor]
        return List

print( factorPair(24,12) )
print( factorPair(40,1) )
