 # Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),

peso=float(input("Introduzca su peso: "));
altura=float(input("Introduzca su altura: "));

imc=round(peso/(altura**2),2);

print("Tu indice de masa corporal es: " +str(imc));
