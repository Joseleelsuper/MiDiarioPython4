#Este programa pide primeramente la cantidad total de compras de una persona. 
#Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. 
#Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. 
#Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. 
#Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, 
#y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, 
#de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.

import random

def descuento(compras):
    if compras < 100:
        print("Lo sentimos, usted no aplica a la promoción, su compra debe de ser mayor a $100.00")
    else:
        #randomizar entre blanco, rojo, azul, amarillo y verde
        bola = random.randint(0,4)
        print("Aleatoriamente se ha seleccionado la bola número: ", bola)
        if bola == 0:
            print("Lo sentimos, usted no aplica a la promoción")
        elif bola == 1:
            print("Usted ha ganado un descuento del 10%")
            compras*=0.9
        elif bola == 2:
            print("Usted ha ganado un descuento del 20%")
            compras*=0.8
        elif bola == 3:
            print("Usted ha ganado un descuento del 25%")
            compras*=0.75
        else:
            print("Usted ha ganado un descuento del 50%")
            compras*=0.5

    print("El valor a pagar es: ", compras)

def main():
    compras = float(input("Introduzca el valor total de sus compras: "))
    descuento(compras)

main()
