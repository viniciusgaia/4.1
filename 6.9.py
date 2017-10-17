N=int(input("Digite um número: "))
A=0
B=1
X=2
D=str(A)+", "+str(B)
while X<N:
    C=A+B
    D=str(D)+", "+str(C)
    A=B
    B=C
    X=X+1
print(D)
