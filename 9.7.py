N=0
while N<1 or N>50:
     N=int(input())
P=N
V=[]
X=1
while N>0:
     from random import randint
     R=randint(1, 99)
     V.append(R)
     N=N-1
print(V)
while X>0:
     X=int(input())
     M=P-1
     A="Não está"
     while M>=0:
          if X==V[M]:
               A="Está"
          M=M-1
     print(A)