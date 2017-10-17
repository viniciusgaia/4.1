N=0
while N<1 or N>50:
     N=int(input())
A=[]
NEG=[]
POS=[]
while N>0:
     X=int(input())
     A.append(X)
     N=N-1
     if X<0:
        NEG.append(X)
     if X>=0:
        POS.append(X)
print(NEG)
print(len(NEG))
print(POS)
print(len(POS))