#! python3

import math

def tempConversion(degrees,unit="C"):
    if unit=='C':
        a = (degrees*9/5)+32
        return a
    elif unit=='F':
        a = (degrees - 32)*5/9
        return a


def factorPair(a,factor):
    b=int(a/factor)
    if b>= factor:
        List=[factor,b]
        return List
    else:
        List=[b,factor]
        return List


def toRadians(a):
    b=(a/180)*math.pi
    print(b)
    return b

def quadratic(a,b,c):
    e=b**2 - 4*a*c
    s1=(-b+math.sqrt(e))/(2**a)
    s2=(-b-math.sqrt(e))/(2**a)
    List=[s1,s2]
    return List

def solution(List):
    #a,b=cosineLaw(10,3,50,oppositeSide=False)
    a,b = List
    if a>0:
        return a
    else:
        return b
    
def cosineLaw(a,b,c,oppositeSide=True):
    c=toRadians(c)
    if oppositeSide==True:
        d=math.sqrt(a**2+b**2 - 2*a*b*math.cos(c))
        return d
    else:
        if a>b:
            # d**2 -2*d*b*math.cos(c)+b**2-a**2=0
            d=quadratic(1,2*b*math.cos(c),b**2-a**2)
            return solution(d)
        elif a<b:
            # d**2 -2*a*d*math.cos(c)+a**2-b**2=0
            d=quadratic(1,2*a*math.cos(c),a**2-b**2)
            return solution(d)

print(cosineLaw(10,3,50,oppositeSide=False))



    
