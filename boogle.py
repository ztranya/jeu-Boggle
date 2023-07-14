import random

                      #JEU BOOGLE SIMPLIFIÉ


# -------------------------------CRÉATION DE LA GRILLE DE JEU-------------------------------
## CETTE FONCTION VALIDE LA TAILLE ENTRER PAR L'UTILISATEUR


##CETTE FONCTION CRÉE UNE GRILLE ALÉATOIRE AVEC DES DÉS DONNÉS
def generer_grille(taille):

    ##Si taille non valide fonction retour None

    if taille !=4 and taille!= 5 and taille != 6 :
        return None

    ##formation des dés
    des = {}

    des['0'] =  ['E', 'T', 'U', 'K', 'N', 'O']
    des['1'] =  ['E', 'V', 'G', 'T', 'I', 'N']
    des['2'] =  ['D', 'E', 'C', 'A', 'M', 'P']
    des['3'] =  ['I', 'E', 'L', 'R', 'U', 'W']
    des['4'] =  ['E', 'H', 'I', 'F', 'S', 'E']
    des['5'] =  ['R', 'E', 'C', 'A', 'L', 'S']
    des['6'] =  ['E', 'N', 'T', 'D', 'O', 'S']
    des['7'] =  ['O', 'F', 'X', 'R', 'I', 'A']
    des['8'] =  ['N', 'A', 'V', 'E', 'D', 'Z']
    des['9'] =  ['E', 'I', 'O', 'A', 'T', 'A']
    des['10'] = ['G', 'L', 'E', 'N', 'Y', 'U']
    des['11'] = ['B', 'M', 'A', 'Q', 'J', 'O']
    des['12'] = ['T', 'L', 'I', 'B', 'R', 'A']
    des['13'] = ['S', 'P', 'U', 'L', 'T', 'E']
    des['14'] = ['A', 'I', 'M', 'S', 'O', 'R']
    des['15'] = ['E', 'N', 'H', 'R', 'I', 'S']

    des['16'] = ['A', 'T', 'S', 'I', 'O', 'U']
    des['17'] = ['W', 'I', 'R', 'E', 'B', 'C']
    des['18'] = ['Q', 'D', 'A', 'H', 'A', 'U']
    des['19'] = ['A', 'C', 'F', 'L', 'N', 'E']
    des['20'] = ['P', 'R', 'S', 'T', 'U', 'G']
    des['21'] = ['J', 'P', 'R', 'X', 'E', 'Z']
    des['22'] = ['E', 'K', 'V', 'Y', 'B', 'E']
    des['23'] = ['A', 'L', 'C', 'H', 'E', 'M']
    des['24'] = ['E', 'D', 'U', 'F', 'H', 'K']

    des['25'] = ['E', 'V', 'C', 'A', 'U', 'G']
    des['26'] = ['P', 'I', 'U', 'V', 'A', 'C']
    des['27'] = ['Y', 'L', 'M', 'B', 'I', 'U']
    des['28'] = ['K', 'D', 'R', 'V', 'U', 'O']
    des['29'] = ['O', 'T', 'C', 'Q', 'K', 'B']
    des['30'] = ['X', 'L', 'H', 'F', 'E', 'U']
    des['31'] = ['M', 'A', 'U', 'F', 'V', 'K']
    des['32'] = ['P', 'D', 'R', 'D', 'H', 'E']
    des['33'] = ['B', 'S', 'U', 'F', 'N', 'I']
    des['34'] = ['G', 'W', 'A', 'I', 'H', 'K']
    des['35'] = ['F', 'D', 'U', 'F', 'J', 'C']

    ##mélange des dés

    longueur_grille_au_long = taille ** 2

    ## mélange des dés

    numero_de_au_hasard = list(range(longueur_grille_au_long))
    des_melange = []
    while numero_de_au_hasard:
        ensemble_des_des = random.randint(0, len(numero_de_au_hasard) - 1)
        des_melange.append(numero_de_au_hasard.pop(ensemble_des_des))

    ##attribution des dés à chaque case
    grille_au_long = []
    des_depart = 0
    while longueur_grille_au_long > 0:
        numero_des = des_melange[des_depart]
        des_choisi = des[str(numero_des)]

        face_des = ((des_choisi)[random.randint(0, 5)])
        grille_au_long.append(face_des)
        des_depart += 1
        longueur_grille_au_long -= 1

    ##séparation de la grille en différentes lignes
    global grille
    grille = []
    start_grille = 0
    while len(grille) < taille:
        grille.append(grille_au_long[start_grille:(start_grille + taille)])
        start_grille += taille

    return (grille)

## CETTE FONCTION AFFICHE LA GRILLE
def affichage_grille(grille, taille):
    print("-" * 5 * taille)
    for element in grille:
        for indice in range(len(element)):
            if indice % 1 == 0:
                print('｜', end=" ")
            print(element[indice], end=" ")
        print('｜')
        print("-" * 5 * taille)


# -------------------------------DÉROULEMENT DE LA PARTIE-------------------------------

##CETTE FONCTION D'ASSURER L'ENTRÉE DE MOTS DE L'UTILISATEUR
def partie():
    global mots_valides
    global liste_mots
    global nbr_mots
    global plus_de_mots
    global point
    global mot

    mots_valides = []

    mot = ''
    liste_mots = []
    nbr_mots = 2
    plus_de_mots = True
    while plus_de_mots:
        mot = input('Entrez un mot (majuscules -- min 3 lettres). Max 10 mots : ')
        est_valide(grille, mot)

        if validité == True:
            print('LÉGALE')
            mots_valides.append(mot)

        else:
            print('ILLÉGALE')
        encore = input('Encore un autre mot? oui ou non (O ou N) : ')

        if encore == 'O':
            if nbr_mots <= 10:
                nbr_mots += 1
                liste_mots.append(mot)
                continue
            else:
                print('Vous avez atteint le nombre maximal de mots. Nous allons comptabiliser les points ')
                break
        else:
            plus_de_mots = False
            print('Nous allons comptabiliser les points')

    liste_mots.append(mot)
    print('Voici tous les mots valides:' + str(mots_valides))

    # Calcul des points
    point = 0
    calcul_point()


## CETTE FONCTION VALIDE QUE LE MOT ENTRÉ EST BIEN PRÉSENT DANS LA GRILLE DONNÉE
def est_valide(grille, mot):
    global validité

    # retour taille
    taille = len(grille)


    if len(mot) >= 3:
        for i in range(len(mot)):
            lettre = mot[i]

            # Prends chaque lettre donné une par une et cré une liste des positions des lettres qui lui sont semblables

            meme_lettre_loc = []
            for ligne_loc in range(taille):
                for col_loc in range(taille):
                    if grille[ligne_loc][col_loc] == lettre:
                        meme_lettre_loc.append((ligne_loc, col_loc))

            # La lettre est elle adjacente a la précedante

            if i > 0:
                lettre_prec = mot[i - 1]
                localisation_lettre_prec = []
                for ligne_loc in range(taille):
                    for col_loc in range(taille):
                        if grille[ligne_loc][col_loc] == lettre_prec:
                            localisation_lettre_prec.append((ligne_loc, col_loc))

                ##Vérifier si lettre suivante présenté à + ou - une ligne
                validité = False
                for (ligne_prec, colonne_prec) in localisation_lettre_prec:
                    for (ligne_loc, col_loc) in meme_lettre_loc:
                        if (ligne_prec - 1 <= ligne_loc <= ligne_prec + 1 and
                                colonne_prec - 1 <= col_loc <= colonne_prec + 1):
                            validité = True

                        ##Ne pas utiliser la même case deux fois
                        for (ligne_prec, colonne_prec) in localisation_lettre_prec:
                            for (ligne_loc, col_loc) in meme_lettre_loc:
                                if ligne_prec == ligne_loc and colonne_prec == col_loc :
                                    validité = False



                if not validité:
                    return False

        # If all characters are adjacent, return True
        return True

    else:
        return False

def echelle_point(i,taille):

    point = None
    if len(i) == 3:
        point = 1

    elif len(i) == 4:
        point = 2

    elif len(i) == 5:
        point = 3

    elif len(i) == 6:
        if taille == 4 or taille == 6:
            point = 5
        elif taille == 5:
            point = 4

    elif len(i) == 7:
        if taille == 4:
            point = 8
        elif taille == 5:
            point = 6
        elif taille == 6:
            point = 7

    elif len(i) == 8:
        point = 10

    elif len(i) >= 9:
        if taille == 4 or taille == 5:
            point = 10
        elif taille == 6:
            point = 12

    return (point)

def calcul_point():
    global point_cumulé
    global mots_acceptés
    global taille
    mots_acceptés = []
    point = 0
    taille = len(grille)
    point_cumulé = 0
    for i in  mots_valides:
        décision = input('Est-ce-que vous validez ce mot? [A] Accepté [R] Rejeté . Le mot est ' + i + ' : ')

        if décision == 'A':

            point_cumulé += echelle_point(i,taille)
            print('Le mot est accepté, vous avez ' + str(point_cumulé) + ' points.')
            mots_acceptés.append(i)
        elif décision == 'R':
            point += 0
            print('Le mot est rejeté, vous restez donc avec ' + str(point_cumulé) + ' points.')

    print('Les points ont été comptabilisés')


def calcul_gagnant(liste_des_point):
    points_plus_élevé = max(liste_des_point)
    joueur_point_plus_élevé = []

    # Va au travers de la list des points de chaque joueur et print si plusieurs sont gagnant et lesquels :
    for i in range(len(liste_des_point)):
        if liste_des_point[i] == points_plus_élevé:
            joueur_point_plus_élevé.append(i)

    if len(joueur_point_plus_élevé) > 1:
        print('NOUS AVONS UNE ÉGALITÉ ENTRE LES JOUEURS SUIVANTS : ')
        premiere_position_print = 0
        while premiere_position_print in range(len(joueur_point_plus_élevé)):
            print('JOUEUR ', joueur_point_plus_élevé[premiere_position_print])

            premiere_position_print += 1

    ## Sinon qui est le seul gagnant
    else:
        print('JOUEUR', liste_des_point.index(points_plus_élevé), 'a remporté la partie!')

def affichage_final () :
    taille = len(grille)
    for mot in liste_mots :

        ##affichage final points -- REJET ou ILLEGAL:
        if mot in mots_valides and mot in mots_acceptés :
            pointage = '('+str(echelle_point(mot,taille)) +')'
            signal = ' '
        elif mot in mots_valides and mot not in mots_acceptés : ##mot non accepté
            pointage = '(x)'
            signal = '-- REJETE'

        else : ##mot illégal
            pointage = '(x)'
            signal = '-- ILLEGAL'

        print ('-', mot,' '*(9-len(mot)), pointage, signal)


# -------------------------------INITIALISATION DE LA PARTIE-------------------------------

def jouer():

    ##Choisir le nombre de joueurs
    nombre_de_joueurs = (int(input("Choisissez le nombre de joueurs : ")))
    while nombre_de_joueurs == 1:
        nombre_de_joueurs = (int(input("Choisissez le nombre de joueurs : ")))

    ## tant que taille nest pas valide redemander une nouvelle taille -- demander ensuite l'affichage
    taille = int(input("Quel format désirez vous? 4x4, 5x5 ou 6x6 (Écrivez 4, 5 ou 6 pour répondre) : "))
    while generer_grille(taille) == None:
        taille = int(input("Ceci ne constitue pas un choix valide (Écrivez 4, 5 ou 6 pour répondre) : "))
        generer_grille(taille)
    affichage_grille(generer_grille(taille),taille)

    ##Partie de chaque joueur
    joueur = 1
    liste_des_point = [0]
    while joueur in range (0, nombre_de_joueurs+1) :
        print('\nJOUEUR ', joueur, '\n' + '-' * 30)
        partie()
        point_joueur = point_cumulé

        print('\nJOUEUR ', joueur, '\n' + '-' * 30)
        print('SOMMAIRE JOUEUR', joueur)
        affichage_final()

        print('=' * 30)
        print('TOTAL: ', point_joueur)
        liste_des_point.append (point_joueur)
        joueur += 1

    ##Connaitre le gagnant
    calcul_gagnant(liste_des_point)

    ##Fin de la partie
    recommencer = input('Voulez-vous recommencer une partie? O ou N : ')
    if recommencer == 'N':
        print('Plus de jeu')

    elif recommencer == 'O':
        print('NOUVELLE PARTIE!')
        jouer()

    else :
        print('CHOIX INVALIDE... Plus de jeu')


jouer()


def test () :

    ##données pour les tests

    taille = random.choice([4, 5, 6])

    grille = [['A', 'B', 'C'],
              ['D', 'E', 'F'],
              ['G', 'H', 'I']]

    ##TEST 1 : GENERER_GRILLE()

    def test_generer_grille():

        # 1 vérifier que la fonction ne générère que des grilles 4x4, 5x5, 6x6
        nombre_0_100 = [num for num in range(101)]
        nombre_0_100.remove(4)
        nombre_0_100.remove(5)
        nombre_0_100.remove(6)
        for num in nombre_0_100: assert generer_grille(num) == None

        # 2 Vérifier que 2 grilles générées ne sont jamais les memes

        for ligne in generer_grille(taille):
            assert ligne not in generer_grille(taille)

        # 3 Grille générée est avec les dimensions données

        assert len(generer_grille(taille)) == taille

        # 4 Grille bel et bien composée de lettres de l'alphabet

        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U',
                    'V', 'W', 'X', 'Y', 'Z', ]
        for ligne in generer_grille(taille):
            for lettre in ligne:
                assert lettre in alphabet

        # 5 Vérifier que la longueur de chaques colonnes est la meme que celles de chaque lignes rangés

        for ligne in generer_grille(taille):
            assert len(generer_grille(taille)) == len(ligne)

    ##TEST 2 : EST_VALIDE()
    def test_est_valide() :

        #1 Mot valide

        mot = 'AEIF'
        assert est_valide(grille,mot) == True

        #2 Mot invalide

        mot = 'ZIEA'
        assert est_valide(grille,mot) == False

        # 3 Mot trop court

        mot = 'AB'
        assert est_valide(grille, mot) == False

        #4 Utiliser la même case 2x

        mot = 'ABBCF'
        assert est_valide(grille, mot) == False

        #5 Les barrières de la grille sont respectées
        mot = 'CAB'
        assert est_valide(grille, mot) == False


    test_generer_grille()
    test_est_valide()


#test()
