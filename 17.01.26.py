#Given a number N, write a program to print a Butterfly of (2N)-1 rows using stars (*).
#code:

N=int(input())
for i in range(1,N+1):
    print("* "*(i)+" "*(4*(N-i))+"* "*(i))
for i in range(1,N):
    print("* "*(N-i)+" "*(4*(i))+"* "*(N-i))
