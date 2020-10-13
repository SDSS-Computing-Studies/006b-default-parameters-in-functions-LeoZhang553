#!python3

def factorPair(a,factor):
    List1=[]
    b=int(a/factor)
    if b>= factor:
        List1.append(factor)
        List1.append(b)
        return List1
    else:
        List1.append(b)
        List1.append(factor)
        return List1

print( factorPair(24,12) )
print( factorPair(40,1) )
