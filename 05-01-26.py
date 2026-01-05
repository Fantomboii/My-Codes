#print the reverse of the given string
S=input()
a=""
for i in range(len(S)):
    a=S[i]+a
print(a)
