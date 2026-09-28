import random

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
    lista_de_nombres_res : list[str] = []
    for jugadores in dicc.keys():
        lista_de_nombres_res.append(dicc[jugadores][0])
    return lista_de_nombres_res

def tupla_agente_y_arma(dicc: dict[str, tuple[str,str,float,str,int]]) -> list[tuple[str,str]]:
    tupla_res : list[tuple[str,str]] = []
    for jugadores in dicc.keys():
        tupla_res.append((dicc[jugadores][0], dicc[jugadores][3]))
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
    lista_opciones : list[str] = ["la cabeza", "el torso", "las piernas"]
    return(random.choice(lista_opciones))

##########################################
def distancia_del_duelo() -> float:
    return(random.uniform(0.0,50.0))

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


def disparos(dicc: dict[str, tuple[str,str,float,str,int]]):
    primer_agente : str = random.choice(agentes(dicc))
    segundo_agente : str = sacar_agente(agentes(dicc), primer_agente)
    tuplas_agente_arma : list[tuple[str,str]] = tupla_agente_y_arma(dicc)
    arma_primer_agente : str = armas_elegidas(tuplas_agente_arma, primer_agente)
    direccion_disparo : str = disparo_aleatorio()

    print(f'{primer_agente} le ha disparado a {segundo_agente} con {arma_primer_agente}! en {direccion_disparo}')

#disparos(estado_inicial_duelo())
