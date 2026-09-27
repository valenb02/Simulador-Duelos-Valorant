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

def estado_inicial_duelo() -> dict[str, tuple[str,float,str]]:
    dicc_res : dict[str[tuple[str,float,str]]] = {}
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
        dicc_res[personaje] = (lado,150,arma)

        i += 1
    return dicc_res


