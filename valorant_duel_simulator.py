import random


# dict[str,dict[tuple,dict[str,int]]]
daño_armas = {
    "Classic": {
        (0, 30): {"cabeza": 78, "torso": 26, "pierna": 22},
        (30, 50): {"cabeza": 66, "torso": 22, "pierna": 19}
    },

    "Ghost": {
        (0, 30): {"cabeza": 105, "torso": 30, "pierna": 26},
        (30, 50): {"cabeza": 88, "torso": 25, "pierna": 21}
    },

    "Bandit": {
        (0, 10): {"cabeza": 152, "torso": 39, "pierna": 33},
        (10, 30): {"cabeza": 128, "torso": 39, "pierna": 33},
        (30, 50): {"cabeza": 112, "torso": 34, "pierna": 28}
    },

    "Sheriff": {
        (0, 30): {"cabeza": 159, "torso": 55, "pierna": 47},
        (30, 50): {"cabeza": 145, "torso": 50, "pierna": 43}
    },

    "Frenzy": {
        (0, 20): {"cabeza": 78, "torso": 26, "pierna": 22},
        (20, 50): {"cabeza": 63, "torso": 21, "pierna": 18}
    },

    "Stinger": {
        (0, 15): {"cabeza": 68, "torso": 27, "pierna": 23},
        (15, 50): {"cabeza": 57, "torso": 23, "pierna": 19}
    },

    "Spectre": {
        (0, 15): {"cabeza": 78, "torso": 26, "pierna": 22},
        (15, 30): {"cabeza": 66, "torso": 22, "pierna": 18},
        (30, 50): {"cabeza": 60, "torso": 20, "pierna": 17}
    },

    "Bulldog": {
        (0, 50): {"cabeza": 116, "torso": 35, "pierna": 30}
    },

    "Guardian": {
        (0, 50): {"cabeza": 195, "torso": 65, "pierna": 49}
    },

    "Phantom": {
        (0, 20): {"cabeza": 156, "torso": 39, "pierna": 33},
        (20, 50): {"cabeza": 140, "torso": 35, "pierna": 30}
    },

    "Vandal": {
        (0, 50): {"cabeza": 160, "torso": 40, "pierna": 34}
    },

    "Warden": {
        (0, 50): {"cabeza": 200, "torso": 50, "pierna": 42}
    },

    "Marshal": {
        (0, 50): {"cabeza": 202, "torso": 101, "pierna": 85}
    },

    "Outlaw": {
        (0, 50): {"cabeza": 238, "torso": 140, "pierna": 119}
    },

    "Operator": {
        (0, 50): {"cabeza": 255, "torso": 150, "pierna": 120}
    },

    "Ares": {
        (0, 30): {"cabeza": 75, "torso": 30, "pierna": 26},
        (30, 50): {"cabeza": 70, "torso": 28, "pierna": 24}
    },

    "Odin": {
        (0, 30): {"cabeza": 95, "torso": 38, "pierna": 33},
        (30, 50): {"cabeza": 78, "torso": 31, "pierna": 26}
    }
}


personajes : list[str] = ["Jett", "Reyna", "Iso", "Yoru", "Raze", "Phoenix", "Waylay", "Neon",
                        "Clove", "Omen", "Brimstone", "Astra", "Harbor", "Miks", "Viper",
                        "Cypher", "Sage", "Killjoy", "Chamber", "Veto", "Deadlock", "Vyse",
                        "Sova", "Skye", "Fade", "Gekko", "Breach", "Kay/O", "Tejo"]


#afuera escopetas y melee
armas : list[str] = ["Vandal", "Phantom", "Guardian", "Warden", "Bulldog",
                     "Spectre", "Stinger", "Marshal", "Outlaw", "Ares",
                     "Odin", "Operator", "Classic", "Ghost", "Bandit", "Frenzy",
                     "Sheriff"]

bandos : list[str] = ["ATTACKER", "DEFENDER"]

def elegir_personaje() -> str:
    return(random.choice(personajes))

def elegir_arma() -> str:
    return(random.choice(armas))


def agentes(dicc: dict[str, tuple[str,str,float,str,int]]) -> list[str]:
    lista_de_jugadores : list[str] = []

    for jugador in dicc.keys():
        lista_de_jugadores.append(jugador)

    return lista_de_jugadores

def tupla_agente_y_arma(dicc: dict[str, tuple[str,str,float,str,int]]) -> list[tuple[str,str]]:
    tupla_res : list[tuple[str,str]] = []
    for jugadores in dicc.keys():
        tupla_res.append((jugadores, dicc[jugadores][3]))
    return tupla_res

def sacar_agente(lista: list[str], agente: str) -> str:
    for nombre in lista:
        if nombre != agente:
            return nombre
    
def armas_elegidas(lista_tuplas_agente_y_arma: list[tuple[str,str]], agente: str) -> str:
    for tupla in lista_tuplas_agente_y_arma:
        if tupla[0] == agente:
            return tupla[1]


def disparo_aleatorio() -> str:
    lista_opciones : list[str] = ["cabeza", "torso", "pierna"]
    return(random.choice(lista_opciones))

##########################################
def distancia_del_duelo() -> float:
    return(random.uniform(0.0,50.0))

'''crea el diccionario que guarda la info de los jugadores que se enfrentaran
 jugador1: (agente, lado, distancia, arma, hp)'''
def estado_inicial_duelo() -> dict[str, tuple[str,str,float,str,int]]:
    dicc_res : dict[str,tuple[str,str,float,str,int]] = {}
    distancia_duelo : float = distancia_del_duelo()
    hp : int = 150

    i : int = 0

    while i < 2: 

        personaje : str = elegir_personaje()
        arma : str = elegir_arma()

        if i == 0 :
            lado: str = random.choice(bandos)
            jugador: str = "jugador1"
        else:
            if lado == "ATTACKER":
                lado = "DEFENDER"
            else:
                lado = "ATTACKER"
            jugador: str = "jugador2"

        dicc_res[jugador] = (personaje,lado,distancia_duelo,arma,hp)

        i += 1
    return dicc_res

'''funcion que elige aleatoriamente quien dispara a quien y pone esa info en una quintupla:
(disparador,arma con la que se dispara, victima, parte del cuerpo disparada, distancia )'''
def disparos(dicc: dict[str, tuple[str,str,float,str,int]], tirador: str) -> tuple[str,str,str,str,float]:
    segundo_agente : str = sacar_agente(agentes(dicc), tirador)
    tuplas_agente_arma : list[tuple[str,str]] = tupla_agente_y_arma(dicc)
    arma_primer_agente : str = armas_elegidas(tuplas_agente_arma, tirador)
    direccion_disparo : str = disparo_aleatorio()

    return(tirador, arma_primer_agente, segundo_agente, direccion_disparo, dicc[tirador][2])

'''funcion que calcula el daño que hace el disparo segun el arma, direccion y distancia a la que fue el disparo'''
def calcular_daño(arma: str, direccion: str, distancia: float) -> int:
    daño : int = 0
    for gun in daño_armas.keys():
        if arma == gun:
            for intervalo in daño_armas[gun]:
                if intervalo[0] <= distancia <= intervalo[1]:
                    daño += daño_armas[gun][intervalo][direccion]
    return daño


'''funcion que modifica el diccionario, especificamente el hp que se le descuenta al personaje que esta recibiendo el daño'''
def modificar_diccionario(dicc: dict[str, tuple[str,str,float,str,int]],tirador:str) -> str:
    info_primer_disparo : tuple[str,str,str,str,float] = disparos(dicc,tirador)
    arma : str = info_primer_disparo[1]
    dañado : str = info_primer_disparo[2]
    direcc : str = info_primer_disparo[3]
    distancia : float = info_primer_disparo[4]
    hp_a_descontar : int = calcular_daño(arma,direcc,distancia)
    hp_actual : int = dicc[dañado][4]
    nuevo_hp : int = hp_actual - hp_a_descontar
    print(f'{tirador} le ha disparado a {dañado} con {arma}! en la/el {direcc}')

    dicc[dañado] = (dicc[dañado][0], dicc[dañado][1], dicc[dañado][2], dicc[dañado][3], nuevo_hp)
    return tirador

#modificar_diccionario(estado_inicial_duelo())

#def ciclo_del_duelo(tirador: str)