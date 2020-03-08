
'''import random

r=random.uniform(1,3)
d=random.randint(1,2)
nbre = int(input("quel est votre nombre mystere?"))

nbre_mystère = 7


if nbre>nbre_mystère:
    print("le nombre est plus petit")



elif nbre<nbre_mystère:
    print("le nombre est plus grand")

else:
    print("felicitation vous avez trouvé le nombre")


res = int(nbre) == nbre_mystère
print(res)

import random

a = random.randint(0, 15)

b = random.randint(0, 26)

if b > a:
    print("le nombre b est plus grand que le nombre a")

elif a > b:
    print("le nombre a est plus grand que b")

else:
    print("le nombre a et le nombre b sont egaux")


'''

import random

nombre_mystere = random.randint(0, 100)
essais = 0

while essais <= 15:
    nombre = input("Quel est le nombre mystère ? ")
# i check if my number has only number
    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        continue
#then i do a convertion von the number in interger
    nombre = int(nombre)

    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()

    essais += 1

print(f"Vous avez perdu. Le nombre mystère était {nombre_mystere}")





'''if nombre.isdigit():
    nombre = int(nombre)
    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
else:
    print("SVP, entrez un nombre valide.")  
'''

