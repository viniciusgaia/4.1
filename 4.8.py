A=float(input("Insira o primeiro lado do triângulo: "))
B=float(input("Insira o segundo lado do triângulo: "))
C=float(input("Insira o terceiro lado do triângulo: "))
if (A+B>C and A+C>B and B+C>A) and (A==B and B==C and A==C):
    print("As medidas inseridas formam um triâgulo Equilátero!")
elif (A+B>C and A+C>B and B+C>A) and (A==B or B==C or A==C):
    print("As medidas inseridas formam um triâgulo Isósceles!")
elif (A+B>C and A+C>B and B+C>A) and (A!=B and B!=C and A!=C):
    print("As medidas inseridas formam um triâgulo Escaleno!")
else:
    print("As medidas inseridas não formam um triâgulo!")
