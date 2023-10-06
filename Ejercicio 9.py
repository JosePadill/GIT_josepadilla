# Escribir un programa que pregunte al usuario una cantidad a invertir.

cantidad=float(input("Que cantidad va invertir: "));
interes=float(input("Cual es su interes: "));
tiempo=float(input("Que cantidad de años: "));

ganancia=(cantidad/100)*interes;
gananciatotal=round(ganancia*tiempo);

print("Capital obtenido: "+str(gananciatotal));
