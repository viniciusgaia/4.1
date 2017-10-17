N=int(input("Digite a quantidade de termos: "))
Prim=int(input("Digite o menor valor para o primeiro termo: "))
A=0
B=1
X=0
D=str(A)+", "+str(B)
while X<N:
    C=A+B
    D=str(D)+", "+str(C)
    X=X+1
    if C>Prim:
        A=B
        B=C
print(D)
