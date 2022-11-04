#Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película 
#y posterior a ello pide que el usuario introduzca el número de días de atraso, 
#y así se muestra al final el total a pagar.

def peliculas():
    print("Categorías de películas\t\t Días de atraso")
    print("1. Acción: 5€\t\t\t 0.5€/dia")
    print("2. Comedia: 3€\t\t\t 0.5€/dia")
    print("3. Terror: 4€\t\t\t 0.5€/dia")
    print("4. Infattil: 2€\t\t\t 0.5€/dia")
    print("5. Documental: 1€\t\t 0.5€/dia")
    print("6. Otros: 6€\t\t\t 0.5€/dia")

def categorias():
    categoria = int(input("Introduzca el código de la categoría de la película: "))
    if categoria == 1:
        total = 5.0
    elif categoria == 2:
        total = 3.0
    elif categoria == 3:
        total = 4.0
    elif categoria == 4:
        total = 2.0
    elif categoria == 5:
        total = 1.0
    elif categoria == 6:
        total = 6.0
    else:
        print("Categoría no válida")
    
    return total

def dias_atraso(total):
    dias = int(input("Introduzca el número de días de atraso: "))
    for i in range(dias):
        total += 0.5
    
    return total
    
def total_pagar(total):
    print("El total a pagar es de", total, "€")

def main():
    peliculas()
    total = categorias()
    total = dias_atraso(total)
    total_pagar(total)

main()