N=int(input())
M=N
L=[]
while M>0:
     X=int(input())
     L.append(X)
     M=M-1
while N>M:
     print(L[M])
     M=M+1