N=int(input("Digite a quantidade de números: "))
X=0
S=float(0)
while X<N:
    V=float(input("Digite um número: "))
    S=S+V
    X=X+1
print("Soma dos valores = %.2f" % S)
