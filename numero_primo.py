def funcion_cuenta(a):
  b=0
  while(b<=a):
    if(int(b/2)*2==b):
      print(b)
    
    else:
      print(b,"No es par")
    
    b=b+1

  print("he acabado!")


def funcion_primo(a):
  b=2
  if(a==2):
    print(a)
    return(1)

  while(a>b):
    if(a%b==0):
      return(0) 
      """se puede dividir- no es primo"""
    b=b+1
  if(b==a):
    print(a)
    return(1)




numero=int(input("dime un numero:"))

contador=2
while contador<=numero:
  funcion_primo(contador)
  contador=contador+1
print("ya no quiero mas !")