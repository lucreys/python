import random
import time
import os
while True:
    tablero = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]
    posicionesbarcos={}
    barcoseliminados=0
    municion=10
    for indice in range(3):
        while True:
            filapos=random.randint(0, 3)
            columnaspos=random.randint(0, 2)
            if (filapos, columnaspos) not in posicionesbarcos.values():
                posicionesbarcos[indice]=[filapos, columnaspos]
                tablero[filapos][columnaspos]="-"
                break
    for fila in tablero:
        print(fila)
    print("Bienvenido jugador.\n¿Estás listo?")
    resp = input("=>").lower()
    if resp == "si":
        print("Hay 3 barcos que tienes que hundir. Buena suerte, el tablero es de 3x4.")
        while True:
            if barcoseliminados == 3:
                print("¡Felicidades! Has hundido todos los barcos.")
                break
            if municion == 0:
                print("Se te ha acabado la munición. ¡Has perdido!")
                print("¿Deseas volver a jugar?")
                resp=input("=>")
                if resp=="si":
                    time.sleep(1)
                    os.system("cls")
                    
                elif resp=="no":
                    break
                else:
                    print("Las respuestas solo se aceptan en formato 'si' o 'no'. Otro formato es incorrecto.")
                break
            try:
                fila = int(input("Ingresa la fila (1-4) en la que crees que se encuentra el barco.\n> "))
                columna = int(input("Ingresa la columna (1-3) en la que crees que se encuentra el barco.\n> "))
                if fila < 1 or fila > 4 or columna < 1 or columna > 3:
                    print("Debes colocar valores de acuerdo a lo acordado.")
                    continue
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue
            municion-=1
            fila-=1
            columna-=1
            print("BOOM")
            if [fila, columna] in posicionesbarcos.values():
                if tablero[fila][columna]!="X":
                    print("Has acertado el tiro en el objetivo")
                    tablero[fila][columna]="X"
                    barcoseliminados+=1
                else:
                    print("Le has dado a un barco ya destruido")
            else:
                print("Has fallado el tiro")
                tablero[fila][columna]="0"
            for fila in tablero:
                print(fila)
            print(f"Munición restante: {municion}")
            print(f"Barcos eliminados: {barcoseliminados}")
        print("¿Deseas volver a jugar?")
        resp=input("=>")
        if resp=="si":
            time.sleep(1)
            os.system("cls")
            
        elif resp=="no":
            print("Hasta luego que tenga un buen dia")
            break
        else:
            print("Las respuestas solo se aceptan en formato 'si' o 'no'. Otro formato es incorrecto.")
    elif resp == "no":
        print("Que tengas un buen día, hasta luego.")
        break
    else:
        print("Las respuestas solo se aceptan en formato 'si' o 'no'. Otro formato es incorrecto.")
        
print("hola")
        
        
        
        
        
        
        
        
        
        
        
        