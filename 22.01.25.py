#write a program to print the letter W of (N) rows using stars

#code:

N=int(input())
print("* "*((2*N)-1))
for i in range(N+1):
    print(" "*(i+1)+"* "*(N-(i+1))+" "*((i*2))+"* "*(N-(i+1)))
