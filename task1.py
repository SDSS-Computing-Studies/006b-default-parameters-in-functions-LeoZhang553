#!python3

import assignment

def tempConversion(degrees,unit="C"):
    if unit=='C':
        a = (degrees*9/5)+32
        return a
    elif unit=='F':
        a = (degrees - 32)*5/9
        return a

print( assignment.tempConversion(0) ) 
print( assignment.tempConversion( 72, "F") ) 



