# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla

n=int(input("Introduzca el primer numero: "));
m=int(input("Introduzca el segundo numero: "));

c=int(n/m);
r=n%m;

print("El cociente es : "+ str(c)+" El resuido es: "+str(r));
