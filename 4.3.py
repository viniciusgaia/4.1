A=float(input("Insira o primeiro número: "))
B=float(input("Insira o segundo número: "))
if A>B:
    print("%.2f é o maior número." % A)
    print("%.2f é o menor número." % B)
elif B>A:
    print("%.2f é o maior número." % B)
    print("%.2f é o menor número." % A)
else:
    print("Os dois números são iguais")
