#Given two numbers X and N, write a program to print the sum of N terms in the given series.
#Series:
#X, XX, XXX, ... N terms

#code:

X=int(input())
N=int(input())
sum=0
a=0
for i in range(1,N+1):
    a=str(X)*i
    sum=sum+int(a)
print(sum)
