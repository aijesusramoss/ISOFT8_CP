import threading
import time

# Recursos compartidos
rockola = threading.Semaphore(1)     # Solo un grupo a la vez
mesa_billar = threading.Semaphore(1) # Solo un grupo a la vez
baño = threading.Lock()              # Solo un borracho a la vez

# Número de ciclos
CICLOS = 5

# Barrera para sincronizar ciclos
barrera = threading.Barrier(3)  # 3 grupos

# Funciones de recursos
def usar_rockola(grupo):
    with rockola:
        print(f"🎶 {grupo} está usando la Rockola...")
        time.sleep(2)
        print(f"✅ {grupo} terminó en la Rockola.")

def usar_mesa_billar(grupo):
    with mesa_billar:
        print(f"🎱 {grupo} está jugando en la Mesa de Billar...")
        time.sleep(3)
        print(f"✅ {grupo} terminó en la Mesa de Billar.")

def usar_baño(nombre_borracho):
    with baño:
        print(f"🚽 {nombre_borracho} está en el baño...")
        time.sleep(1.5)
        print(f"✅ {nombre_borracho} salió del baño.")

# Actividades de cada grupo en cada ciclo
def ciclo_borrachos(grupo, nombres, plan):
    turno_baño = 0  # índice del integrante que le toca ir al baño

    for ciclo, recurso in enumerate(plan, 1):
        print(f"\n🍺 Ciclo {ciclo} - {grupo} empieza")

        if recurso == "rockola":
            usar_rockola(grupo)
        elif recurso == "mesa":
            usar_mesa_billar(grupo)
        elif recurso == "baño":
            if turno_baño < len(nombres):  # mientras haya integrantes pendientes
                usar_baño(nombres[turno_baño])
                turno_baño += 1
            else:
                print(f"🚽 {grupo} ya no tiene integrantes pendientes para el baño.")

        print(f"🍺 Ciclo {ciclo} - {grupo} terminó")

        # esperar a los demás grupos para pasar al siguiente ciclo
        barrera.wait()

# Plan de uso de recursos → garantiza que todos usen cada recurso al menos 1 vez
plan_A = ["rockola", "mesa", "baño", "rockola", "mesa"]
plan_B = ["mesa", "baño", "rockola", "mesa", "rockola"]
plan_C = ["baño", "rockola", "mesa", "baño", "rockola"]

# Crear grupos
grupoA = ["A1", "A2", "A3"]
grupoB = ["B1", "B2", "B3"]
grupoC = ["C1", "C2", "C3"]

# Crear hilos
hiloA = threading.Thread(target=ciclo_borrachos, args=("Grupo A", grupoA, plan_A))
hiloB = threading.Thread(target=ciclo_borrachos, args=("Grupo B", grupoB, plan_B))
hiloC = threading.Thread(target=ciclo_borrachos, args=("Grupo C", grupoC, plan_C))

# Iniciar hilos
hiloA.start()
hiloB.start()
hiloC.start()

# Esperar finalización
hiloA.join()
hiloB.join()
hiloC.join()

print("\n🍻 ¡Simulación terminada después de 5 ciclos!")
