L=[]
X=int(input())
Y=0
Z=0
while X>0:
    L.append(X)
    X=int(input())
    Y=Y+1
while Y>0:
    print(L[Z])
    Y=Y-1
    Z=Z+1
