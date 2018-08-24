from random import randint,choice, randrange

def character_random( xfact = None, yfact = None):
    character = ["good","bad", 'friendly','greateful','selfish']
    n_character = []
    if xfact == None:
        xfact = character
    if yfact == None:
        yfact = n_character
    for z in range(1,len(character)):
        n = choice(xfact)
        yfact.append(n)
        xfact.remove(n)
    rand = ', '.join(yfact)
    return rand