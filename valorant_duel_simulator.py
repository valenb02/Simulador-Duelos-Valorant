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


def agentes(dicc: dict[str, tuple[str,float,str,int]]) -> list[str]:
    lista_de_nombres_res : list[str] = []
    for nombres in dicc.keys():
        lista_de_nombres_res.append(nombres)
    return lista_de_nombres_res

##########################################
def distancia_del_duelo() -> float:
    return(random.uniform(0.0,50.0))

def estado_inicial_duelo() -> dict[str, tuple[str,float,str,int]]:
    dicc_res : dict[str,tuple[str,float,str,int]] = {}
    distancia_duelo : float = distancia_del_duelo()
    hp : int = 150

    i : int = 0

    while i < 2: 

        if i == 0 :
            lado: str = random.choice(bandos)
        else:
            if lado == "ATTACKER":
                lado = "DEFENDER"
            else:
                lado = "ATTACKER"

        personaje : str = elegir_personaje()
        arma : str = elegir_arma()
        dicc_res[personaje] = (lado,distancia_duelo,arma,hp)

        i += 1
    return dicc_res


#funcion que pickea aleatoriamente a uno de los players, el player
#elegido será quien dispare primero. El disparo que de será elegido
# aleatoriamente, podrá ser a la pierna, torso o cabeza y se sacará
# la vida del diccionario que guarda el estado de la pelea la vida correspondiente
# segun el arma y a dónde fue el disparo

#modifica: diccionario. devuelve: 
#valen : str = "hola"
#print(f'{valen}')


# necesito que mi funcion:
# arranque uno disparando, y en el proximo turno, si es que el disparo no fue con: vandal o guardian a la cabeza, awp a cuerpo entonces en
# el proximo turno le toque si o si al otro jugador, y que a partir de ahi el juego siga ese bucle, van uno y uno (dispara uno, dispara el otro)
# y que se vaya 'hp' en el diccionario a medida que disparan. El juego terminará cuando el hp de alguno de los dos llegue a 0.

def tupla_agente_y_arma(dicc: dict[str, tuple[str,float,str,int]]) -> list[tuple[str,str]]:
    tupla_res : list[tuple[str,str]] = []
    for agente in dicc.keys():
        tupla_res.append((agente, dicc[agente][2]))
    return tupla_res

def sacar_agente(lista: list[str], agente: str) -> str:
    for nombre in lista:
        if nombre != agente:
            return nombre
    
def armas_elegidas(lista_tuplas_agente_y_arma: list[tuple[str,str]], agente: str) -> str:
    for tupla in lista_tuplas_agente_y_arma:
        if tupla[0] == agente:
            return tupla[1]

def disparos(dicc: dict[str, tuple[str,float,str,int]]):
    primer_agente : str = random.choice(agentes(dicc))
    segundo_agente : str = sacar_agente(agentes(dicc), primer_agente)
    tuplas_agente_arma : list[tuple[str,str]] = tupla_agente_y_arma(dicc)
    arma_primer_agente : str = armas_elegidas(tuplas_agente_arma, primer_agente)

    print(f'{primer_agente} has slained {segundo_agente} with {arma_primer_agente}')
    

    