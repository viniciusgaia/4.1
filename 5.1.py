N=int(input("Digite o número de termos: "))
R=int(input("Digite a razão: "))
P=int(input("Digite o primeiro termo: "))
S=0
X=0
while X<N:
    print(P)
    S=S+P
    P=P*R
    X=X+1
print("Soma dos termos = %d" % S)
