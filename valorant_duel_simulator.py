import random

personajes : list[str] = ["Jett", "Reyna", "Iso", "Yoru", "Raze", "Phoenix", "Waylay", "Neon",
                        "Clove", "Omen", "Brimstone", "Astra", "Harbor", "Miks", "Viper",
                        "Cypher", "Sage", "Killjoy", "Chamber", "Veto", "Deadlock", "Vyse",
                        "Sova", "Skye", "Fade", "Gekko", "Breach", "Kay/O", "Tejo"]

armas : list[str] = ["Vandal", "Phantom", "Guardian", "Warden", "Bulldog",
                     "Spectre", "Stinger", "Bucky", "Judge", "Marshal", "Outlaw", "Ares",
                     "Odin", "Operator", "Classic", "Ghost", "Bandit", "Frenzy", "Shorty",
                     "Sheriff", "Melee"]

bandos : list[str] = ["ATTACKER", "DEFENDER"]

'''
funciones auxiliares:
    elegir_personaje: elige y devuelve un personaje al azar de la lista de personajes
    elegir_arma: elige y devuelve un arma al azar de la lista de armas
'''

def elegir_personaje() -> str:
    return(random.choice(personajes))

def elegir_arma() -> str:
    return(random.choice(armas))


def agentes(dicc: dict[str, tuple[str,str,float,str,int]]) -> list[str]:
    lista_de_nombres_res : list[str] = []
    for jugadores in dicc.keys():
        lista_de_nombres_res.append(dicc[jugadores][0])
    return lista_de_nombres_res

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

def disparos(dicc: dict[str, tuple[str,str,float,str,int]]):
    primer_agente : str = random.choice(agentes(dicc))
    segundo_agente : str = sacar_agente(agentes(dicc), primer_agente)
    tuplas_agente_arma : list[tuple[str,str]] = tupla_agente_y_arma(dicc)
    arma_primer_agente : str = armas_elegidas(tuplas_agente_arma, primer_agente)

    print(f'{primer_agente} le ha disparado a {segundo_agente} con {arma_primer_agente}!')



