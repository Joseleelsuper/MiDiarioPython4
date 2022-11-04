#De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. 
#El programa determinará el total a pagar, como una factura.
#Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades, 
#y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??

def codigos():
    print("Código camiseta: 1\nCódigo pantalón: 2\nCódigo calcetines: 3\nCódigo gorra: 4\nCódigo zapatillas: 5")
    codes = int(input("Introduzca el código del producto que desea comprar: "))
    ropa(codes)

def ropa(codes):
    if codes == 1:
        print("Camiseta: $100.00")
        cantidad = int(input("Introduzca la cantidad de camisetas que desea comprar: "))
        total = cantidad*100
        print("El total a pagar es: ", total)
    elif codes == 2:
        print("Pantalón: $200.00")
        cantidad = int(input("Introduzca la cantidad de pantalones que desea comprar: "))
        total = cantidad*200
        print("El total a pagar es: ", total)
    elif codes == 3:
        print("Calcetines: $50.00")
        cantidad = int(input("Introduzca la cantidad de calcetines que desea comprar: "))
        total = cantidad*50
        print("El total a pagar es: ", total)
    elif codes == 4:
        print("Gorra: $75.00")
        cantidad = int(input("Introduzca la cantidad de gorras que desea comprar: "))
        total += cantidad*75
        print("El total a pagar es: ", total)
    elif codes == 5:
        print("Zapatillas: $300.00")
        cantidad = int(input("Introduzca la cantidad de zapatillas que desea comprar: "))
        total = cantidad*300
        print("El total a pagar es: ", total)
    else:
        print("Código no válido")
    comprar()

def comprar():
    productos = str(input("¿Desea comprar otro producto? [S/N]: "))
    if productos == "S":
        main()
    else:
        print("Gracias por su compra.")

def main():
    codigos()

main()