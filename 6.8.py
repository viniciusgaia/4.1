X=int(input("Digite um número: "))
Y=2
Z=1
while Z==1 and Y<X:
      if X%Y==0:
          Z=0
      else:
          Y=Y+1
if Z==1:
      print("%d é um número primo." % X)
else:
      print("%d não é um número primo." % X)
