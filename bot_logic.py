import random


def gen_faction():
    factions = [
        "ChechyaForce(Tim Russia!)",
        "OsirisForce(Tim Amerika!)",
        "InvertionForce(Tim Indonesia!)",
        "DutyForce(Tim China!)",
        "CentumForce(Tim Spanyol!)",
        "RenegadesForce(Tim Inggris!)",
        "FederalForce(Tim Ukraina!)",
        "AtlanticForce(Tim Kanada!)",
        "NationalForce(Tim India!)",
        "CerberusForce()"
    ]
    return random.choice(factions)

def gen_pass(join_faction):
    summon = ""
    for i in range(join_faction):
        faction = gen_faction()
        summon += faction + "\n"
    return summon


def gen_emodji():
    emodji = [":joy:", ":heart:", ":smile:", ":astonished:", ":angry:"]
    return random.choice(emodji)


def gen_coins():
    flip = random.randint(0, 2)
    if flip == 0:
        return "You Win!"
    else:
        return "You Lose"

def story_FW():
 story_fw = ""
