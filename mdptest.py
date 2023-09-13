import time

Lettres = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","?","!","@"]

Mottester = ""



def brutforce(mot):
    NombreTentative = 0
    try:
        T1 = time.time()
        nombre = int(mot)
        nombretester = 0
        nombrenontrouvée = True
        while nombrenontrouvée:
            if nombre == 0:
                t2 = time.time()
                t3 = t2 - T1
                nombrenontrouvée = False
                return(nombre, t3, nombre)
            elif nombre == nombretester:
                t2 = time.time()
                t3 = t2 - T1
                nombrenontrouvée = False
                return(nombre, t3, nombre)
            nombretester += 1
            print(nombretester)

    except:
        T1 = time.time()
        for r in Lettres:
            for q in Lettres:
                for p in Lettres:
                    for o in Lettres:
                        for n in Lettres:
                            for m in Lettres:
                                for l in Lettres:
                                    for k in Lettres:
                                        for j in Lettres:
                                            for i in Lettres:
                                                for h in Lettres:
                                                    for g in Lettres:
                                                        for f in Lettres:
                                                            for e in Lettres:
                                                                for d in Lettres:
                                                                    for c in Lettres:
                                                                        for b in Lettres:
                                                                            for a in Lettres:
                                                                                Mottester = (f"{r}{q}{p}{o}{n}{m}{l}{k}{j}{i}{h}{g}{f}{e}{d}{c}{b}{a}")
                                                                                NombreTentative += 1
                                                                                print("test : %s    tentative : %s" % (Mottester, NombreTentative))
                                                                                if Mottester == mot:
                                                                                    t2 = time.time()
                                                                                    t3 = t2 - T1
                                                                                    return(mot, t3, NombreTentative)

print("Bienvenue, ce programme en python a été créé dans le but de tester sont mot de passe dans le but de savoir en combien de temps, votre mot de passe peut être connu. Ce programme n'a en aucun cas été créé pour brutforcer des mots de passes ni pour servir à autre chose qu'à voir en combien de temps votre mot de passe se fait prendre. Mon programme n'est pas le plus rapide, je vous conseille de ne pas vous fiez au temps donner par mon programme car il se peut que quelqu'un d'autre puisse le trouver plus facilement. Je vous conseille pour vos mot de passe de faire un mot de passe de minimum 8 lettres/chiffres/lettres spéciales et faites attention à ne pas donner vos mot de passe à quelqu'un en qui vous n'avez pas confiance ni de laisser trainer (si vous en avez) vos papiers avec les mots de passe de divers compte.")

while 1:
    print()
    motdepasse = input("""Entrez le mot de passe à tester :
""")
    print("""Le mot de passe était : %s
Le mot a été trouvé en %s
Le nombre d'essai était %s""" % brutforce(motdepasse))