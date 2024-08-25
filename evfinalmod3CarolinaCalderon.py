print()
print("Evaluación final módulo 3: Introducción a Phyton")
print("Estudiante: Carolina Calderón, sección 068, Bootcamp Python trainee")
print()

# Lista inicial de nombres dada en el drilling
famosos = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", 
    "Messi", "Teller", "Einstein", "Pele", "Juanes"
]

# Listas vacías que usaré para clasificar los nombres
magos = []
cientificos = []
otros = []

# Ciclo para clasificar los nombres de los famosos en magos, científicos y otros
for famoso in famosos:
    if famoso == "Harry Houdini" or famoso == "David Blaine" or famoso == "Teller":
        magos.append(famoso)
    elif famoso == "Newton" or famoso == "Hawking" or famoso == "Einstein":
        cientificos.append(famoso)
    else:
        otros.append(famoso)

# Función para agregar 'El gran' antes del nombre de cada mago
def hacer_grandioso(lista_magos):
    largo = 0
    while largo < len(lista_magos):
        lista_magos[largo] = "El gran " + lista_magos[largo]
        largo += 1  

# Aplico función para agregar 'El gran' antes del nombre de cada mago
hacer_grandioso(magos)

# Función para imprimir los nombres de cada lista, la haré numeerada
def imprimir_nombres(nombre_lista, grupo):
    print(grupo)
    numerador = 1  
    for nombre in nombre_lista:
        print(f"{numerador}.- {nombre}")
        numerador += 1  

# Imprimir cada una de las listas modificadas
imprimir_nombres(famosos, "Todos los famosos:")  #Lista completa antes de modificarla
print()
imprimir_nombres(magos, "Magos famosos:")
print()
imprimir_nombres(cientificos, "Científicos famosos:")
print()
imprimir_nombres(otros, "Otros famosos:")
print()
