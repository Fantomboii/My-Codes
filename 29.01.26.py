#Program to print hollow pyramid of N rows using "*"
N=int(input())
for i in range(1,N+1):
    if i==1:
        row=" "*(N-1)+"* "
    elif i==N:
        row="* "*N
    else:    
        row=" "*(N-i)+"* "+" "*((i-2)*2)+"* "
    print(row)
