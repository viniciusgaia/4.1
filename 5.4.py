N=int(input("Digite a quantidade de números: "))
X=0
S=float(0)
while X<N:
    V=float(input("Digite um número: "))
    if V>0:
        S=S+V
    X=X+1
print("Soma dos valores positivos = %.2f" % S)
