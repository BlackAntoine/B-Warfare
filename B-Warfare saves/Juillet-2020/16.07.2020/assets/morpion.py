
import copy
from sklearn.neural_network import MLPClassifier
import numpy as np
import random
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree


class Morpion:

    #Permet d'initialiser le jeu
    def __init__(self):
        #Création et initialisation du plateau de jeu
        self.plateau=[['-','-','-'],['-','-','-'],['-','-','-']]
        #Déclaration du premier Joueur
        self.J1='X'
        #Déclaration du second Joueur
        self.J2='O'
        #Création d'une base d'observations qui contiendra l'historique des parties jouées
        self.base_de_jeu=[]
        #Création d'une base de résultats contiendra l'historique des résultats des parties jouées
        self.base_resultat_jeu=[]
        #Création d'un classifieur de type Arbre de décision
        #self.clf = tree.DecisionTreeClassifier()
        #Création d'un classifieur de type réseau de neurones
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6, 2), random_state=1)
        #Création d'un classifieur de type RandomForest
        #self.clf = RandomForestClassifier(n_estimators=50, max_depth=2,random_state=0)

    #Fonction de réinitialisation du tableau
    def intialiser_plateau(self):
        self.plateau=[['-','-','-'],['-','-','-'],['-','-','-']]

    #Fonction de jeu qui fera jouer l'ia pour l'entraîner
    def ai_jeu(self,i):

    #Fonction qui convertira le plateau de signe en plateau de données numériques compréhensibles pour un réseau de neurones
    def convert_plateau(self, plateau):

    #Fonction d'entraînement par renforcement de l'ia, elle fera l'ia jouer de nombreuses fois contre un joueur
    # dont les mouvements seront aléatoire
    def train_ai_jeu(self):
        #L'IA va jouer 10 fois 10000 jeu pour apprendre
        for i in range (0, 10):
            victoire_j1=0
            victoire_ia=0
            egalite=0
            # Pour j allant de zéro à 10000
            for j in range (0,10000):
                #IA joue une partie
                sauvegarde_plateaux, result = self.ai_jeu(i)
                #Si la fonction ai_jeu a renvoyé que j1 est vainqueur
                if (result==self.J1):
                    #Son nombre de victoire est incrémenté
                    victoire_j1+=1
                #sinon si elle a renvoyé que J2 est vainqueur
                elif (result==self.J2):
                    #le nombre de victoire de l'ia est incrémenté
                    victoire_ia+=1
                else :
                    #sinon le nombre d'égalité est incrémenté
                    egalite+=1
                #Pour tout les plateau de la dernière partie jouée
                for k in range (0,len(sauvegarde_plateaux)):
                    #La plateau sous forme de matrice de 3 x 3 est passé en vecteur de taille 9
                    sauvegarde_plateaux[k]=np.array(sauvegarde_plateaux[k]).reshape(-1)
                    #l'ensemble des données alphabétiques son convertie en données numériques
                    sauvegarde_plateaux[k]=self.convert_plateau(sauvegarde_plateaux[k])
                    sauvegarde_plateaux[k]=sauvegarde_plateaux[k].astype(np.float64)
                    #Si J1 0 gagné
                    if( result ==self.J1):
                        #Ajouts des plateau a la base d'observations
                        self.base_de_jeu.append(sauvegarde_plateaux[k])
                        #Ajout de 0 à la base de résultat pour dire que J1 à gagné sur ce plateau
                        self.base_resultat_jeu.append(0)
                    #Si l'IA a gagné 0
                    elif ( result ==self.J2):
                        #Ajouts des plateau a la base d'observations
                        self.base_de_jeu.append(sauvegarde_plateaux[k])
                        #Ajout de 1 à la base de résultat pour dire que J1 à gagné sur ce plateau
                        self.base_resultat_jeu.append(1)

            #Affichage des victoires après 10000 partie
            print ("Itération = ", i , " victoire J1 = ",victoire_j1, "victoire IA = ",victoire_ia, "egalite = ",egalite)
            #Actualisation de l'intelligence de l'ia
            self.train_ai_player()

    def train_ai_player(self):
        # Normalisation des données (absolument nécessaire pour un réseau de neurones)
        self.scaler = preprocessing.StandardScaler().fit(self.base_de_jeu)
        X_train=self.scaler.transform(self.base_de_jeu)
        #Entrainement du classifieur chargé de choisir les coups de l'IA
        self.clf.fit ( X_train,self.base_resultat_jeu)

    #Contient le code qui assure le bon déroulement du jeu en lui même
    def jeu(self):
        morpion.afficher_plateau()
        bool_fin_jeu=False
        #Tant que le jeu n'est pas fini
        while bool_fin_jeu==False:
            #Le joueur 1 joue
            morpion.jouer(self.J1)
            morpion.afficher_plateau()
            #Test de victoire de J1
            resultat_test_fin_jeu=self.test_fin_jeu(self.J1)
            #Si J1 à gagné
            if( resultat_test_fin_jeu==self.J1):
                #Affiche Joueur 1 à gagné
                print ("Joueur " + self.J1 +" a gagné" );
                return self.J1
            elif ( resultat_test_fin_jeu==True):
                #Affiche Égalité entre les joueurs
                print ("Égalité entre les joueurs" );
                return "égalité"
            #Le joueur 2 joue
            morpion.jouer(self.J2)
            morpion.afficher_plateau()
            resultat_test_fin_jeu=self.test_fin_jeu(self.J2)
            #Test de victoire de J2
            if( resultat_test_fin_jeu!=False):
                print ("Joueur " + self.J2 +" a gagné" );
                return self.J2
            elif ( resultat_test_fin_jeu==True):
                print ("Égalité entre les joueurs" );
                return "égalité"

         #Renvoie l'ensemble des mouvements possibles pour le joueur passé en paramètre
    def generateur_de_mouvement(self,joueur):
        #Déclaration d'une liste qui contiendra tout les mvts possible
        liste_mouvement_possible=[]
        #Pour tout les cases du plateau
        for i in range (0, 3):
            for j in range (0, 3):
                #Si la case courante est vide
                if (self.plateau[i][j]=="-"):
                    #Création d'un mouvement virtuel et ajout de celui-ci a la liste des mouvements possibles
                    virtual_plateau=copy.deepcopy(self.plateau)
                    virtual_plateau[i][j]=joueur
                    liste_mouvement_possible.append(virtual_plateau)

        return liste_mouvement_possible

    #Fonction qui entraîne l'ia sur les parties passées
    def train_ai_player(self):
         # Normalisation des données (absolument nécessaire pour un réseau de neurones)
        self.scaler = preprocessing.StandardScaler().fit(self.base_de_jeu)
        X_train=self.scaler.transform(self.base_de_jeu)
        #Entrainement du classifieur chargé de choisir les coups de l'IA
        self.clf.fit ( X_train,self.base_resultat_jeu)


    #Fonction permet à l'adversaire de l'ia de jouer son tour
    def entraineur_ai_joue(self,list_mvt_possible):
         #Selon la liste des mouvements possibles un mouvement aléatoire est joué
        if( len(list_mvt_possible)>1):
            indice_mvt=random.randint(0,len(list_mvt_possible)-1)
            self.plateau=list_mvt_possible[indice_mvt]
        else :
            self.plateau=list_mvt_possible[0]

    #Permet à l'ia de jouer son tour
    def ai_player_joue(self,joueur,list_mvt_possible):
         #Copie des mouvement possibles
        list_mvt_possible_copy=copy.deepcopy(list_mvt_possible)
        # Conversion de la copie des mouvement possibles en données numériques
        for i in range (0,len(list_mvt_possible_copy)):
            list_mvt_possible_copy[i]=self.convert_plateau(np.array(list_mvt_possible_copy[i]).reshape(-1)).astype(np.float64)
        #Normalisation des données des plateaux numériques
        X_test=self.scaler.transform(list_mvt_possible_copy)
        #L'IA calcul de la probabilité de gagner selon chacun des mouvement possible
        proba_success_mvt=self.clf.predict_proba(X_test)
        indice_mvt=0
        #Pour tout les probabilités de gagner des mouvements possible, on choisi la plus grande
        for i in range (0, len(proba_success_mvt)):
            if(proba_success_mvt[indice_mvt][1]<proba_success_mvt[i][1]):
                indice_mvt=i

        self.plateau=list_mvt_possible[indice_mvt]

    #Affiche le plateau de jeu
    def afficher_plateau(self):
            def afficher_plateau(self):
        for i in range (0, 3):
            for j in range (0, 3):
                print ("|", end="")
                print (self.plateau[i][j], end="")
            print ("|")
        print ("-----------------------------------------")


    #Test si il y a un vainqueur où si il y a plus de mouvement possible
    def test_fin_jeu(self,joueur):
        def test_fin_jeu(self,joueur):
        #vérifie le joueur courant n'a pas aligné son signe sur une ligne
        for i in range (0,3):
            compteur=0
            for j in range (0,3):
                if self.plateau[i][j]==joueur:
                    compteur+=1
            #Si il a aligné son signe 3 fois en horizontal
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur

        #vérifie le joueur courant n'a pas aligné son signe sur une colonne
        for i in range (0,3):
            compteur=0
            for j in range (0,3):
                if self.plateau[j][i]==joueur:
                    compteur+=1
            #Si il a aligné son signe 3 fois en vertical
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur
        # Test de diagonales 1
        compteur=0
        for i in range (0,3):
            if self.plateau[i][i]==joueur:
                    compteur+=1
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur
        compteur=0
        # Test de diagonales 2
        for i in range (0,3):
            if self.plateau[2-i][i]==joueur:
                    compteur+=1
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur

        #vérifie qu'il reste de la place sur le plateau en comptant les signes de tout les joueurs
        compteur=0
        for i in range (0,3):
            for j in range (0,3):
                if( self.plateau[i][j]!='-'):
                    compteur+=1
        #Si il n'y a plus de place sur le plateau
        if compteur==8:
            # On retourne vrai pour dire que le jeu est fini
            return True
        #Le jeu n'est pas encore fini on retourne false
        return False

    #Permet à un joueur de jouer son tour
    def jouer(self, joueur):
        #Demande les coordonnées où le joueur souhaite jouer
        x = input("Entrez l'abscisse compris entre 1 et 3 : ")
        y = input("Entrez l'ordonnée compris entre 1 et 3 : ")
        #Affectation de la marque du joueur à la position x et y du plateau
        self.plateau[int(x)][int(y)]=joueur


morpion=Morpion()
morpion.train_ai_jeu()
