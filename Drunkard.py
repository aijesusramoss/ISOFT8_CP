import time
import random

while True:

    nombre_estado = {"Carlitos": 0, "Antuna": 0, "Zuñiga": 0, "Cesar": 0, "Ramiro": 0}
    valores = random.sample(range(1, 6), len(nombre_estado))  
    nombre_estado = dict(zip(nombre_estado.keys(), valores))  

    def tomar(nombre):
        if nombre_estado[nombre] == 1:
            print(f"{nombre} tomando cerveza...")
            time.sleep(1)

    def usar_baño(nombre):
        if nombre_estado[nombre] == 2:
            print(f"{nombre} orinando...")
            time.sleep(1)
            print(f"{nombre} salió del baño...")

    def llamar_ex(nombre):
        if nombre_estado[nombre] == 3:
            print(f"{nombre} llamando a su ex...")

    def cantar(nombre):
        if nombre_estado[nombre] == 4:
            print(f"{nombre} está cantando...")
    
    def ver_tiktok(nombre):
        if nombre_estado[nombre] == 5:
            print(f"{nombre} está viendo TikTok")

    acciones = [tomar, usar_baño, llamar_ex, cantar, ver_tiktok]

    def main():
        for accion in acciones:
            for nombre in nombre_estado:
                accion(nombre)
    print(f'================================Termino El Ciclo ========================================')


    main()
