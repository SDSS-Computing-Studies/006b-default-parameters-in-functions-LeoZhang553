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
    return b

# b is the missing side
# convert cosine law into quadratic fomula
def cosineLaw(a,d,c,oppositeSide=True):
    pass
    

def quadratic(a,b,c):
    r=toRadians(c)
    e=b**2 - 4*a*c
    s1=(-b+math.sqrt(e))/(2**a)
    s2=(-b-math.sqrt(e))/(2**a)
    List=[s1,s2]
    print(List)
    return List


def solution():
    a,b=quadratic(a,b,c)
    if a>0:
        print(a)
    else:
        print(b)
