import random

class Jugador:
    def __init__(self, nombre, vidas, puntuacionReal, puntuacion):
        self.nombre = nombre
        self.vidas = vidas
        self.puntuacionReal = puntuacionReal;
        self.puntuacion = puntuacion;

MAX_VIDAS = 1

pDado = {
    1: "Negro",
    2: "Rojo",
    3: "Jota",
    4: "Q",
    5: "K",
    6: "As",
    7: ("Negro", "Negro"),
    8: ("Rojo", "Rojo"),
    9: ("Jota", "Jota"),
    10: ("Q", "Q"),
    11: ("K", "K"),
    12: ("As", "As"),
    13: ("Rojo", "Negro"),
    14: ("Negro", "Rojo")
}

pPosibles = [4,5,6,7,8,9,10,11,"Pareja de Negros", "Pareja de Rojos", "Pareja de J", "Pareja de Q", "Pareja de K", "Pareja de As", "Kiriki"]


# Agrega la relación especial
pDado_relaciones = {
    ("Negro", "Negro"): "Pareja de Negros",
    ("Rojo", "Rojo"): "Pareja de Rojos",
    ("J", "J"): "Pareja de J",
    ("Q", "Q"): "Pareja de Q",
    ("K", "K"): "Pareja de K",
    ("As", "As"): "Pareja de As",
    ("Rojo", "Negro"): "Kiriki",
    ("Negro", "Rojo"): "Kiriki"
}

def escribirPuntuacionesPosibles():
    i = 4
    for puntuacion in pPosibles:
        print(f"{i}: {puntuacion}")
        i+=1

def leerPuntuacion():
    """
    Ingresa puntuacion numerica entre los posibles valores de la lista pPosibles (puntuaciones posibles)
    Returns:
        puntuacion (int): puntuacion dicha por el jugador
    """
    puntuacion = int(input("Ingrese la puntuacion que quiera decir: "))

    while(puntuacion<4 or puntuacion>18):
        puntuacion = int(input("Puntuacion incorrecta. Ingrese la puntuacion que quiera decir: "))

    return puntuacion

def lanzar_dados_jugador():
    """
    Tira los dados
    Returns:
        tuple: devuelve una tupla aleatoria con los valores de los dados. Ejemplo: ("Negro", "Negro")
    """
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Comprobamos si los dados son iguales (pareja) o son kiriki (negro y rojo, que sera 1 y 2)
    if((dado1 == dado2) or (dado1==1 and dado2==2) or (dado1==2 and dado2==1)):
        if((dado1==1 and dado2==2) or (dado1==2 and dado2==1)):
            puntuacionReal = 18
        else:
           if dado1 == 1:
            puntuacionReal = 12
           elif dado1 == 2:
            puntuacionReal = 13 
           elif dado1 == 3:
            puntuacionReal = 14
           elif dado1 == 4:
            puntuacionReal = 15 
           elif dado1 == 5:
            puntuacionReal = 16
           else:
            puntuacionReal = 17
    else:
       puntuacionReal = dado1 + dado2
    #puntuacion = (pDado.get(dado1), pDado.get(dado2))

    return str(pDado.get(dado1)), str(pDado.get(dado2)), puntuacionReal

def comprobar_verdad_jugador(pos_j_actual, pos_j_siguiente):
    """
    Determina si el jugador actual esta diciendo la verdad.
    Si es verdad, el jugador siguiente (el que levanta) pierde una vida.
    Si no, el jugador que ha dicho la puntuacion (actual) pierde una vida
    Args:
        pos_j_actual (int): posicion del jugador actual
        pos_j_siguiente (int): posicion del jugador siguiente

    Returns:
        bool: True si el jugador actual dice la verdad, False si no
    """
    if(jugadores[pos_j_actual].puntuacion <= jugadores[pos_j_actual].puntuacionReal):
        print(f"{jugadores[pos_j_actual].nombre} dice la verdad. {jugadores[pos_j_siguiente].nombre} pierde una vida")
        jugadores[pos_j_siguiente].vidas -= 1
        print(f"Vidas de {jugadores[pos_j_siguiente].nombre}: {jugadores[pos_j_siguiente].vidas}")
        return True
    else:
        print(f"PReal: {jugadores[pos_j_actual].puntuacionReal} Puntuacion: {jugadores[pos_j_actual].puntuacion}")
        print(f"{jugadores[pos_j_actual].nombre} no dice la verdad, pierde una vida")
        jugadores[pos_j_actual].vidas -= 1
        return False

def comprobarVidas(pos_jugador):
    """Quitamos una vida al jugador, si se queda sin vidas, lo eliminamos de la lista de jugadores

    Args:
        pos_jugador (int): posicion del jugador en la lista de jugadores

    Returns:
        bool: True si el jugador sigue con vidas, False si no
    """
    vidas = jugadores[pos_jugador].vidas
    if(vidas <= 0):
        print(f"{jugadores[pos_jugador].nombre} ha perdido todas sus vidas.")
        jugadores.pop(pos_jugador)
        return False
    else:
        return True

# Crear una lista vacía de jugadores
jugadores = []
pos_j_actual = 0
j_actual = 0

# Pedir al usuario el número de jugadores
num_jugadores = int(input("Ingrese el número de jugadores: "))

# Agregar jugadores a la lista utilizando un bucle for
for i in range(1, num_jugadores + 1):
    nombre = input(f"Ingrese el nombre del Jugador {i}: ")
    vidas = MAX_VIDAS
    jugadores.append(Jugador(nombre, vidas, 0, 0))

# Acceder a los jugadores y sus vidas
i = 1
for jugador in jugadores:
    print(f"Jugador {i}: {jugador.nombre} ")
    i+=1
i = -1

# Juego principal
j_actual = jugadores[0]

# Puntuacion a superar
superar = -1

while len(jugadores) > 1: #Existen jugadores aun
    # Error borrado de jugadores de la lista

    pos_j_siguiente = (pos_j_actual + 1) % len(jugadores)
    j_siguiente = jugadores[pos_j_siguiente]

    print("\n--------------------------------------------------")
    print(f"Turno de {j_actual.nombre}")

    # Lanzo los dados y ajusto la puntuacion del jugador
    input("Presiona Enter para lanzar los dados...")
    dado1, dado2, pRealJugador = lanzar_dados_jugador()

    jugadores[pos_j_actual].puntuacionReal = pRealJugador
    print(f"Puntuacion real: {jugadores[pos_j_actual].puntuacionReal}")

    # Muestro los datos al jugador
    print("Tus dados son:", dado1 + " y " + dado2)
    #escribirPuntuacionesPosibles()

    # Mientras la puntuacion no sea un digito entre 4 y 18, pedimos que ingrese la puntuacion
    # Si la puntuacion es correcta, la guardamos en el jugador
    while j_actual.puntuacion < 4 or j_actual.puntuacion > 18:
        try:
            j_actual.puntuacion = leerPuntuacion()
        except ValueError:
            print("Puntuacion incorrecta. Ingrese la puntuacion que quiera decir: ")
            j_actual.puntuacion = leerPuntuacion()
   
    if(j_actual.puntuacion <= superar):
        print(f"La puntuacion {j_actual.puntuacion} no supera la puntuacion {superar}.")
        print(f"El jugador {j_actual.nombre} pierde una vida.")
        j_actual.vidas -= 1
        if not comprobarVidas(pos_j_actual):
            pos_j_actual = (pos_j_actual + 1) % len(jugadores)
            j_actual = jugadores[pos_j_actual]
    else:
        print(f"El jugador {j_actual.nombre} dice que su puntuacion es: {j_actual.puntuacion}")

        if(j_actual.puntuacion == 18):
            print("Kiriki!")

            # Comprobamos si la puntuacion >= puntuacionReal (si dice la verdad o no)
            if j_actual.puntuacionReal == j_actual.puntuacion:
                tieneVidas = comprobarVidas(pos_j_siguiente)
                if(tieneVidas):
                    pos_j_siguiente = (pos_j_actual + 1) % len(jugadores)
            else:
                comprobarVidas(pos_j_actual)

            superar = -1
        else:
            decision = input(f"Jugador {j_siguiente.nombre}, ¿te lo crees? (si/no):")

            if(decision.lower() == 'si'):
                print(f"Jugador {j_siguiente.nombre} se lo cree, le toca tirar")
                superar = j_actual.puntuacion
            else:
                print(f"Jugador {j_siguiente.nombre} no se lo cree")

                # Comprobamos si la puntuacion >= puntuacionReal (si dice la verdad o no)
                if(comprobar_verdad_jugador(pos_j_actual, pos_j_siguiente)):
                    tieneVidas = comprobarVidas(pos_j_siguiente)
                    if(tieneVidas):
                        pos_j_siguiente = (pos_j_actual + 1) % len(jugadores)
                else:
                    comprobarVidas(pos_j_actual)
        
                superar = -1

    # Pasa al siguiente jugador (Actualizo posicion del jugador actual, y el jugador actual)
    pos_j_actual = (pos_j_actual + 1) % len(jugadores)
    j_actual = jugadores[pos_j_actual]

# Se termina el juego, el jugador que haya quedado en el array jugadores es el que ha ganado la partida
print(f"Fin del juego. El ganador es {jugadores[0].nombre}")