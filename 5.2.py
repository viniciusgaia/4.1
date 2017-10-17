P=0
N=0
X=1
while X!=0:
    X=int(input("Digite um número: "))
    if X>0:
        P=P+X
    elif X<0:
        N=N+X
print("Total dos positivos = %d" % P)
print("Total dos negativos = %d" % N)
