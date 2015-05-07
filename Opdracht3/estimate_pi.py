import sys
import math
import random

L=float(sys.argv[2])
def drop_needle(L):
    x=random.random()
    a=random.vonmisesvariate(0,0)
    c=math.cos(a)
    
    return x+L*c<=0 or x+L*c>=1


N=int(sys.argv[1])
C=[]

A = range(1,N+1)

for i in A:
    i>=1
    if drop_needle(L)==True:
        C.append(True)
        
print(str(len(C)) +" hits in "+ str(N) + " tries")

P=len(C)/N #kans op succes benaderen


if L<=1:
    print("Pi = "+ str(2*L/P))
else:
    A=2*L-2*(math.sqrt(L**2-1)+math.asin(1/L)) #alleen nodig als L>1
    print("Pi = "+ str(A/(P-1)))