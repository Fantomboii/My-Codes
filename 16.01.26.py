#Given two numbers X and N, write a program to print the sum of N terms in the given series.
#Series: X^1, X^3, X^5, ...N terms
#code

X=int(input())
N=int(input())
sum=0
a=0
for i in range(1,N+1):
    a=(2*i)-1
    a=X**a
    sum=sum+a
print(sum)
