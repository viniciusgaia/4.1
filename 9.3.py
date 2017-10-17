N=int(input())
L=[]
Y=-999999999
while N>0:
     X=int(input())
     L.append(X)
     N=N-1
     if X>Y:
        Y=X
print(L)
print(Y)