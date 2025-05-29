import time
import random

while True:
    #este ciclo permite reasignar valores a cada persona al terminar cada ronda.

    nombre_estado = {"Carlitos": 0, "Antuna": 0, "Zuñiga": 0, "Cesar": 0, "Ramiro": 0} #inicia un diccionario con los nombres de los borrrachos y su estado inicial
    valores = random.sample(range(1, 6), len(nombre_estado))                           #crea una lista con valores del 1-5 sin repetir
    nombre_estado = dict(zip(nombre_estado.keys(), valores))                           #le asigna un número a cada persona para que realicen una actividad diferente cada quien

    def tomar(nombre): #función para simular que la persona está tomando.
        if nombre_estado[nombre] == 1:
            print(f"{nombre} tomando cerveza...")
            time.sleep(1)

    def usar_baño(nombre): #función para simular que la persona está yendo al baño
        if nombre_estado[nombre] == 2:
            print(f"{nombre} orinando...")
            time.sleep(1)
            print(f"{nombre} salió del baño...")

    def llamar_ex(nombre): #función para simular que la persona está llamado a su ex
        if nombre_estado[nombre] == 3:
            print(f"{nombre} llamando a su ex...")

    def cantar(nombre): #funcion para simular que una persona está cantando
        if nombre_estado[nombre] == 4:
            print(f"{nombre} está cantando...")
    
    def ver_tiktok(nombre): #funcion para simular que una persona está viendo tiktok
        if nombre_estado[nombre] == 5:
            print(f"{nombre} está viendo TikTok")

    acciones = [tomar, usar_baño, llamar_ex, cantar, ver_tiktok]  #lista con las acciones disponibles
    

    def main():
        for accion in acciones:
            for nombre in nombre_estado: #ciclo que itera entre los borrachos y las acciones, y asigna acciones a cada uno dependiendo de su estado
                accion(nombre)
        print(f'================================Termino El Ciclo ========================================')

    main()
