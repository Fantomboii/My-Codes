# print rectange on M rows and N columns using * as borders and 0 inside
# code:

M=int(input())
N=int(input())
for i in range(1,M+1):
    if i==1 or i==M:
        row="* "*N
    else:
        row="* "+"0 "*(N-2)+"* "
    print(row)
