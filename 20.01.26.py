#Given two numbers X and N, write a program to print the sum of N terms in the given series.

#Series:

#x, -x³, x5, -x7, xº, N terms
#code:

X=int(input())
N=int(input())
pov=1
sum=0
t=0
for i in range(N):
    if i%2!=0:
        t=(-X)**pov
        sum=sum+t
    if i%2==0:
        t=(X)**pov
        sum=sum+t
    pov=pov+2
print(sum)
