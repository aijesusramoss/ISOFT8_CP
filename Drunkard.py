import time
import random

# Inicializar contadores de cervezas por persona
cervezas_tomadas = {"Carlitos": 0, "Antuna": 0, "Zuñiga": 0, "Cesar": 0, "Ramiro": 0}

# Bartender sirve la cerveza
def bartender_servir(nombre):
    print(f"Bartender sirviendo cerveza a {nombre}")
    cervezas_tomadas[nombre] += 1
    time.sleep(1)

# Acciones
def usar_baño(nombre):
    if cervezas_tomadas[nombre] > 0:
        print(f"Bartender anuncia: {nombre} entró al baño.")
        time.sleep(1)
        print(f"Bartender anuncia: {nombre} salió del baño.")

def llamar_ex(nombre):
    print(f"{nombre} llamando a su ex...")

def cantar(nombre):
    print(f"{nombre} está cantando...")

def ver_tiktok(nombre):
    print(f"{nombre} está viendo TikTok...")

# Acción mapeada con su número
acciones_func = {
    1: bartender_servir,
    2: usar_baño,
    3: llamar_ex,
    4: cantar,
    5: ver_tiktok
}

while True:
    nombre_estado = {"Carlitos": 0, "Antuna": 0, "Zuñiga": 0, "Cesar": 0, "Ramiro": 0}
    valores = random.sample(range(1, 6), len(nombre_estado))
    nombre_estado = dict(zip(nombre_estado.keys(), valores))

    print("\n========= NUEVO CICLO =========")
    
    for nombre, accion in nombre_estado.items():
        if accion == 2:
            if cervezas_tomadas[nombre] > 0:
                usar_baño(nombre)
            elif cervezas_tomadas[nombre] == 0:
                print(f"{nombre} no puede ir al baño, no ha tomado ni una cerveza.")
            else:
                print(f"{nombre} quería ir al baño, pero ya está ocupado.")
        elif accion == 3:
                llamar_ex(nombre)
        elif accion == 1:
            bartender_servir(nombre)
        elif accion == 4:
            cantar(nombre)
        elif accion == 5:
            ver_tiktok(nombre)
    
    print("========= Fin del ciclo =========\n")
    time.sleep(2)