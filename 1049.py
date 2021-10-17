#Animal

pista1=input()
pista2=input()
pista3=input()

if pista1 == "vertebrado":
    if pista2 == "ave":
        if pista3 == "carnivoro":
            print('aguia')
        elif pista3 == "onivoro":
            print('pomba')
    elif pista2 == "mamifero":
        if pista3 == "onivoro":
            print('homem')
        elif pista3 == "herbivoro":
            print('vaca')
elif pista1 == "invertebrado":
    if pista2 == "inseto":
        if pista3 == "hematofago":
            print('pulga')
        elif pista3 == "herbivoro":
            print('lagarta')
    elif pista2 == "anelideo":
        if pista3 == "hematofago":
            print('sanguessuga')
        elif pista3 == "onivoro":
            print('minhoca')