import time
T1 = time.perf_counter()
import sys
f=open(sys.argv[2],"w")
N=int(sys.argv[1])

PrimeList = list(range(0,N))
PrimeList[1] = 0
for i in range(1,N):
    if PrimeList[i] !=0:
         for j in range(2*i,N,i):
          PrimeList[j] = 0

 
A=[] 
for i in PrimeList:
    if i!=0:
        A.append(i)
          
for i in A:
   f.write(str(i))
   f.write("\n")
   
T2 = time.perf_counter()



print("Found " + str(len(A)) + " Prime numbers smaller than "+ str(N) + " in " +str(T2-T1))