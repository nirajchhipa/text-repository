import math 

a=[1,4,12,6,21,67,21,89,12,56,23,17,19]

b=[math.sqrt(x) for x in a if(x<50 and x%2==0) or (x>=50 and x%2==1)]
print b

temp=[21,23,30,36,39,39,35,34,33,28,22,31.2]
#c->f

#(c*9/5)+32

#[(x*9/5)+32 for x in temp]

def farenhite(centigrate):
        return centigrate*9/5+32

fvalues=[farenhite(x) for x in temp]
print fvalues
