A=int(input("Insira um valor para A: "))
B=int(input("Insira um valor para B: "))
if A<B:
    print("A possui o menor valor: A = %.0f" % A)
elif B<A:
    print("B possui o menor valor: B = %.0f" % B)
else:
    print("A e B possuem o mesmo valor")
