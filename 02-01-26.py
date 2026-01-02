#read 2 numbers N and T and print numbersr from 1 to N which is divisible by T
N=int(input())
T=int(input())
for i in range(1,N+1):
    if i%T==0:
        print(i)
