#Write a program that reads a number N and finds the count of digits from 1 to N.
#code

N=int(input())
count=0
for i in range(1,N+1):
    if i<10:
        count=count+1
    if 10<=i<100:
        count=count+2
    if 100<=i<1000:
        count=count+3
    if 1000<=i<10000:
        count=count+4
    if 10000<=i<100000:
        count=count+5
    if 100000<=i<1000000:
        count=count+6
print(count)
