N=int(input())
L=[]
Y=999999999
Z=-999999999
while N>0:
     X=int(input())
     L.append(X)
     N=N-1
     if Y>X:
        Y=X
     if X>Z:
        Z=X
print(L)
print(Y)
print(Z)