# Escribir un programa que lea el número de payasos y muñecas 
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.


payasos=int(input("Numero de muñecas vendidos: "));
munecas=int(input("Numero de payasos vendidos: "));

pesopayasos=int(payasos*112);
pesomunecas=int(munecas*75);

pesototal=pesopayasos+pesomunecas;

pesototalkg=pesototal/1000;

print("El peso es de: "+str(pesototalkg)+"kg");