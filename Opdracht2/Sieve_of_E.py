import time
T1 = time.perf_counter()
import sys
f=open("prime.dat", "w")
pp = 2
ps = [pp]
lim=int(sys.argv[1])
while pp < lim:
   pp += 1
   for a in ps:
       if pp%a==0:
           break
   else:
      if pp not in ps:
         ps.append(pp)


for i in ps:
   f.write(str(i))
   f.write("\n")
   
T2 = time.perf_counter()



print("Found " + str(len(ps)) + " Prime numbers smaller than "+ str(lim) + " in " +str(T2-T1))