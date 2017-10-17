X=1
V1=Q=S=0
V2=10**10
while X>0:
    X=int(input("Digite um número: "))
    if X>0:
        Q=Q+1
        S=S+X
        while X>V1:
            V1=X
        while X<V2:
            V2=X
M=S/Q
print("O maior valor informado é %d" % V1)
print("O menor valor informado é %d" % V2)
print("Foram informados %d valores" % Q)
print("A soma dos valores informados é igual a %d" % S)
print("A média dos valores informados é igual a %d" % M)
