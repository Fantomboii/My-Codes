#Given a number N, write a program that checks if N is not divisible by any number from 2 to 9.
#Print Divisible Number if the number N is divisible by any of the numbers from 2 to 9. Print Indivisible Number if the number N is not divisible by any of the numbers from 2 to 9.

#Input

#The input will be a single line containing an integer representing N

#Output

#The output should be a single line containing a string. Divisible Number should be printed if the number N is divisible by any of the numbers from 2 to 9. Indivisible Number should be printed if the number N is not divisible by any of the numbers from 2 to 9.

#solution
N=int(input())
flag=0
sum=0
for i in range(2,10):
    if N%i!=0:
        flag=0
    if N%i==0:
        flag=1
        sum=1
if sum==1:
    print("Divisible Number")
else:
    print("Indivisible Number")
