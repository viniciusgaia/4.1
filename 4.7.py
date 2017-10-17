A=float(input("Insira o primeiro coeficiente da equação: "))
B=float(input("Insira o segundo coeficiente da equação: "))
C=float(input("Insira o terceiro coeficiente da equação: "))
D=(B**2)-4*A*C
X1=(-B+(D**0.5))/(2*A)
X2=(-B-(D**0.5))/(2*A)
if D<0:
    print("Não existem raízes reais para Delta negativo: ")
elif D==0:
    print("Existe apenas uma raiz para Delta igual a 0: ")
    print("A raiz é %.2f" % X1)
else:
    print("Existem duas raízes reais para Delta positivo: ")
    print("A primeira raiz é %.2f" % X1)
    print("A segunda raiz é %.2f" % X2)
