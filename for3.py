#coding: utf8
num=input("¿Cuantos valores va a introducir?")


while (num<0):
	print("¡Imposible!")
	num=input("Intentelo de nuevo:")
num1=input("Escriba un numero:")
	
for i in range (1,num+1):
	num2=input("Escriba un numero mayor que"+" "+str(num1)+":")
	if (num2<num1):
print str(num2)+" no es mayor que"+str(num1)+"!"
