import time
import random

# Listas de personas
mesa1 = ["Carlitos", "Antuna", "Zuñiga", "Cesar", "Ramiro"]
mesa2 = ["Mariana", "Fernanda", "Lucía", "Valeria", "Sofía"]

# Contador de cervezas por persona
cervezas_tomadas = {nombre: 0 for nombre in mesa1 + mesa2}

# Acciones
def bartender_servir(nombre):
    print(f"Bartender sirviendo cerveza a {nombre}")
    cervezas_tomadas[nombre] += 1
    time.sleep(0.5)

def rockola(nombre):
    print(f"{nombre} eligiendo canción en la rockola...")
    time.sleep(0.5)

def cantar(nombre):
    print(f"{nombre} está cantando...")

def bailar(nombre):
    print(f"{nombre} está bailando...")

# Acciones libres disponibles
acciones_libres = [cantar, bailar]

turno = 0

while True:
    print("\n========= NUEVO CICLO =========")

    if turno % 2 == 0:
        mesa_cerveza = "mesa1"
        mesa_rockola = "mesa2"
    else:
        mesa_cerveza = "mesa2"
        mesa_rockola = "mesa1"

    def ejecutar_acciones(mesa_nombre, nombres):
        personas = nombres.copy()
        random.shuffle(personas)

        acciones = {}

        # Asignar cerveza a una persona si le toca a la mesa
        if mesa_nombre == mesa_cerveza:
            elegido = personas.pop()
            acciones[elegido] = bartender_servir

        # Asignar rockola a una persona si le toca a la mesa
        if mesa_nombre == mesa_rockola:
            elegido = personas.pop()
            acciones[elegido] = rockola

        # Asignar acciones libres a los demás
        libres = acciones_libres * ((len(personas) + len(acciones_libres) - 1) // len(acciones_libres))
        for nombre, accion in zip(personas, libres):
            acciones[nombre] = accion

        # Ejecutar acciones
        for nombre, accion in acciones.items():
            accion(nombre)

    print("\n --- Acciones Mesa 1 --- ")
    ejecutar_acciones("mesa1", mesa1)

    print("\n --- Acciones Mesa 2 --- ")
    ejecutar_acciones("mesa2", mesa2)

    print("========= Fin del ciclo =========\n")
    turno += 1
    time.sleep(2)

