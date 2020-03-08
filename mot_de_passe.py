a = input("Entrez un mot de passe (min 8 caractères) : ")

mrd= "votre mot de passe est trop court"

if len(a)==0:

    print(mrd.upper())

elif len(a)<8:

    print(mrd.capitalize())

elif a.isdigit():

    print("votre mot de passe ne contient que des chiffres")
    #exit()

else:

    print("inscription terminée")