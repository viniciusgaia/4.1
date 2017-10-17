A=(input("Insira o nome do lutador: "))
B=float(input("Insira o peso do lutador: "))
if B<65:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Pena" % B)
elif 65<=B<72:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Leve" % B)
elif 72<=B<79:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Ligeiro" % B)
elif 79<=B<86:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Meio médio" % B)
elif 86<=B<93:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Médio" % B)
elif 93<=B<100:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Meio pesado" % B)
else:
    print("O lutador " + A + " pesa %.1f kg e se enquadra na categoria Pesado" % B)
