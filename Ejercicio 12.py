#

barras=int(input("Introduzca las barras vendidas que no son del dia: "));

print("Precio habitual: 3:49e");
descuento=float((3.49/100)*60);

print("Descuento por barra: " + str(descuento));
preciofinal=float(3.49-descuento);

total=barras*preciofinal;

print("Precio total final: " +str(total));
