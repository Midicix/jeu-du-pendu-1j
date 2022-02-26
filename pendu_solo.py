from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import tkinter as tk
import sys
from random import randint

# Création de la fenêtre

##########################################
#color :
couleur_personnage = "red"
couleur_fond = "#5FB691" #On peut mettre les couleurs en hexadécimal, par exemple, ici, mettre "gray" ou "#5FB691"
couleur_structure = "black"
couleur_titre = "black"
couleurs_titre_categories = "red"
couleurs_message_erreurs1 = "yellow"
couleurs_lettre_erreur = "Blue"
couleurs_lettre_juste = "Green"
police_lettre = "Rubik 30 bold"

#dimension
hauteur_page = 1000
largeur_page = 750

##########################################

fenetre = Tk()
canvas = Canvas(fenetre, width=hauteur_page, height=largeur_page, bg = couleur_fond, highlightthickness=0)
canvas.pack(padx=0, pady=0)
fenetre.geometry('1000x750')
fenetre.config(bg=couleur_fond)
fenetre.title("Jeu du pendu")

canvas.create_text(525, 20, text="Le Jeu officiel du Pendu par Aloïs",
                fill=couleur_titre,
                font="Adventure 30 bold")

#################################################################################

canvas.create_text(900, 60, text="Message d'erreurs :",
                fill=couleurs_titre_categories,
                font= ("Times", 15 , "bold", "underline"))

message_erreur1 = canvas.create_text(890, 100, text="",
                fill=couleurs_message_erreurs1,
                font="Times 15 bold")

message_erreur2 = canvas.create_text(890, 100, text="",
                fill=couleurs_message_erreurs1,
                font="Times 15 bold")

message_erreur3 = canvas.create_text(890, 100, text="",
                fill=couleurs_message_erreurs1,
                font="Times 15 bold")

#################################################################################

canvas.create_text(890, 265, text="Lettres fausses :",
                fill=couleurs_titre_categories,
                font= ("Times", 15 , "bold", "underline"))

#guide : canvas.create_line(largeur, hauteur, largeur, hauteur, fill="black", width=5)

#################################################################################

case_lettre_erreur1 = canvas.create_text(835, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur2 = canvas.create_text(855, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur3 = canvas.create_text(875, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur4 = canvas.create_text(895, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur5 = canvas.create_text(915, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur6 = canvas.create_text(935, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur7 = canvas.create_text(955, 290, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

#############

case_lettre_erreur8 = canvas.create_text(835, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur9 = canvas.create_text(855, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur10 = canvas.create_text(875, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur11 = canvas.create_text(895, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur12 = canvas.create_text(915, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur13 = canvas.create_text(935, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

case_lettre_erreur14 = canvas.create_text(955, 310, text="",
                fill=couleurs_lettre_erreur,
                font="Times 15 bold")

#######################################

trait_mot1 = canvas.create_line(100, 675, 50, 675, fill=couleur_fond, width=2.5)
trait_mot2 = canvas.create_line(175, 675, 125, 675, fill=couleur_fond, width=2.5)
trait_mot3 = canvas.create_line(250, 675, 200, 675, fill=couleur_fond, width=2.5)
trait_mot4 = canvas.create_line(325, 675, 275, 675, fill=couleur_fond, width=2.5)
trait_mot5 = canvas.create_line(400, 675, 350, 675, fill=couleur_fond, width=2.5)
trait_mot6 = canvas.create_line(475, 675, 425, 675, fill=couleur_fond, width=2.5)
trait_mot7 = canvas.create_line(550, 675, 500, 675, fill=couleur_fond, width=2.5)
trait_mot8 = canvas.create_line(625, 675, 575, 675, fill=couleur_fond, width=2.5)
trait_mot9 = canvas.create_line(700, 675, 650, 675, fill=couleur_fond, width=2.5)
trait_mot10 = canvas.create_line(775, 675, 725, 675, fill=couleur_fond, width=2.5)
trait_mot11 = canvas.create_line(850, 675, 800, 675, fill=couleur_fond, width=2.5)
trait_mot12 = canvas.create_line(925, 675, 875, 675, fill=couleur_fond, width=2.5)

#################################################################################

jambe2 = canvas.create_line(500, 375, 550, 500, fill=couleur_fond, width=5)

jambe1 = canvas.create_line(500, 375, 450, 500, fill=couleur_fond, width=5)

bras1 = canvas.create_line(500, 275, 450, 375, fill=couleur_fond, width=5)

bras2 = canvas.create_line(500, 275, 550, 375, fill=couleur_fond, width=5)

corps = canvas.create_line(500, 375, 500, 250, fill=couleur_fond, width=5)

tete = canvas.create_oval(475, 200, 525, 250, outline=couleur_fond, width=5)

oeil1_part1 = canvas.create_line(495, 220, 485, 210, fill=couleur_fond, width=2.5)
    
oeil1_part2 = canvas.create_line(495, 210, 485, 220, fill=couleur_fond, width=2.5)

oeil2_part1 = canvas.create_line(515, 220, 505, 210, fill=couleur_fond, width=2.5)
    
oeil2_part2 = canvas.create_line(515, 210, 505, 220, fill=couleur_fond, width=2.5)

######################################
    
angle_bas = canvas.create_line(200, 500, 250, 550, fill=couleur_fond, width=5)
    
angle_haut = canvas.create_line(200, 125, 250, 75, fill=couleur_fond, width=5)

corde = canvas.create_line(500, 75, 500, 200, fill=couleur_fond, width=5)
    
poutre_horizontale = canvas.create_line(550, 75, 150, 75, fill=couleur_fond, width=5)

poutre_verticale = canvas.create_line(200, 550, 200, 75, fill=couleur_fond, width=5)

sol = canvas.create_line(700, 550, 150, 550, fill=couleur_fond, width=5)

#################################################################################

#20 px d'écarts entre chaques lettres (horizontalement) et 20px (verticalement)

co_lettre_y = 655 #20px de moins que le trait, pour être au dessus
co_lettre1_x = 75 #entre le premier x et le deuxième du trait (milieu des deux)
co_lettre2_x = 150
co_lettre3_x = 225
co_lettre4_x = 300
co_lettre5_x = 375
co_lettre6_x = 450
co_lettre7_x = 525
co_lettre8_x = 600
co_lettre9_x = 675
co_lettre10_x = 750
co_lettre11_x = 825
co_lettre12_x = 900


lettre_texte1 = canvas.create_text(co_lettre1_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte2 = canvas.create_text(co_lettre2_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte3 = canvas.create_text(co_lettre3_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte4 = canvas.create_text(co_lettre4_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte5 = canvas.create_text(co_lettre5_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte6 = canvas.create_text(co_lettre6_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte7 = canvas.create_text(co_lettre7_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte8 = canvas.create_text(co_lettre8_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte9 = canvas.create_text(co_lettre9_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte10 = canvas.create_text(co_lettre10_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte11 = canvas.create_text(co_lettre11_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

lettre_texte12 = canvas.create_text(co_lettre12_x, co_lettre_y, text="",
    fill=couleurs_lettre_juste,
    font=police_lettre)

##########################################################################################

message_mot = canvas.create_text(400, 725, text="",
    fill=couleur_titre,
    font="Adventure 30 bold")

##########################################################################################

boutonR = Button(fenetre, font='Times 20 bold', bg='orange',
                 fg='blue', text='new game', height=0, width=0,
                 command=lambda: rejouer(), padx=15, pady=5)

boutonS = Button(fenetre, font='Times 20 bold', bg='orange',
                 fg='red', text='quit', height=0, width=0,
                 command=lambda: stop())

btn = Button(fenetre, height=1, width=10, text="Confirmer", command=lambda: getEntry())
btn.pack()

saisie = tkinter.Entry()
saisie.config(state = tkinter.NORMAL)

boutonS_fenetre = canvas.create_window(965, 20, window=boutonS)
boutonR_fenetre = canvas.create_window(70, 20, window=boutonR)
saisie_fenetre = canvas.create_window(925, 200, window=saisie)
btn_fenetre = canvas.create_window(925, 225, window=btn)

##########################################################################################

liste_bouton = [btn]
liste_lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
liste_lettre_erreur_afficher = [case_lettre_erreur1, case_lettre_erreur2, case_lettre_erreur3, case_lettre_erreur4, case_lettre_erreur5, case_lettre_erreur6, case_lettre_erreur7, case_lettre_erreur8, case_lettre_erreur9,case_lettre_erreur10, case_lettre_erreur11, case_lettre_erreur12, case_lettre_erreur13, case_lettre_erreur14]
liste_trait = [trait_mot1, trait_mot2, trait_mot3, trait_mot4, trait_mot5, trait_mot6, trait_mot7, trait_mot8, trait_mot9, trait_mot10, trait_mot11, trait_mot12]
liste_dessin = [sol, poutre_verticale, poutre_horizontale, angle_bas, angle_haut, corde]
liste_dessin1 = [tete]
liste_dessin2 = [corps, jambe1, jambe2, bras1, bras2]
liste_dessin3 = [oeil1_part1, oeil1_part2]
liste_dessin4 = [oeil2_part1, oeil2_part2]
liste_lettre_mot = []
liste_lettre_erreur = []


liste_mot = ['Hello','Bonsoir','Bonjour','ARRETE','ABRUPT','ABSENT','ABUSER','ACCENT','ACCORD','ACCROC','ACTEUR','ACTION','ACTIVE','ACTUEL','ADORER','ADROIT','ADULTE','AGACER','AGITER','AGNEAU','ALARME','ALCOOL','ALERTE','ALLURE','AMANDE','AMENDE','AMENER','AMICAL','AMUSER','ANANAS','ANCIEN','ANIMAL','ANNEAU','ANNUEL','ARDENT','ARGENT','ASPECT','AUCUNE','AUTANT','AUTEUR','AUTOUR','AVALER','AVANCE','AVENIR','AVENUE','AVERSE','AVIRON','AVOCAT','AVOINE','AVOUER','BROSSE','BAGAGE','BAISER','BALCON','BALLON','BAMBIN','BAMBOU','BANANE','BANDIT','BANQUE','BARQUE','BASSIN','BATEAU','BATTRE','BAVARD','BERCER','BERGER','BESOIN','BEURRE','BILLET','BLEUET','BLOUSE','BONBON','BONDIR','BONNET','BOUCHE','BOUCLE','BOUDER','BOUDIN','BOUGER','BOUGIE','BOURSE','BOUTON','BOXEUR','BREBIS','BRIQUE','BRISER','BROCHE','BRODER','BRUTAL','BUFFET','BUREAU','CASTOR','CABANE','CACHER','CADEAU','CADRAN','CAHIER','CAISSE','CALCUL','CALMER','CAMERA','CAMION','CAMPER','CANARD','CANAUX','CARNET','CARTON','CASIER','CASSER','CAUSER','CENTRE','CERCLE','CERISE','CHACUN','CHAISE','CHALET','CHANCE','CHAQUE','CHASSE','CHATTE','CHEMIN','CHEVAL','CHEVEU','CIGARE','CIMENT','CINEMA','CIRQUE','CITRON','CLASSE','CLIENT','CLIMAT','CLOCHE','CLOUER','COCHON','COFFRE','COGNER','COLLER','COMBAT','COMMUN','COMPAS','COMPTE','CONTER','CONTRE','COPAIN','COPIER','COPINE','COQUET','CORDON','CORNET','COUCHE','COUDRE','COULER','COUPER','COURBE','COURIR','COURSE','COUSIN','CRASSE','CRAYON','CREUSE','CREVER','CROIRE','CRUCHE','CUISSE','CUIVRE','DROGUE','DANGER','DANSER','DEBOUT','DEBRIS','DECHET','DEDANS','DEFAUT','DEHORS','DELICE','DEMAIN','DEPART','DEPUIS','DESERT','DESSIN','DESSUS','DETAIL','DETOUR','DEVANT','DEVOIR','DIABLE','DIRECT','DISQUE','DIVERS','DOCILE','DOLLAR','DOMINO','DONNER','DORMIR','DOUBLE','DOUCHE','DOUTER','DURANT','ESSAIM','ECLAIR','ECLUSE','ECORCE','ECRIER','ECRIRE','ECURIE','EFFORT','EGARER','EGLISE','ELEVER','EMPLIR','EMPLOI','ENCORE','ENFANT','ENFUIR','ENNEMI','ENORME','ENTIER','ENTRER','ENVERS','ENVIER','EPAULE','EPELER','EPONGE','EPOQUE','EPOUSE','EQUIPE','ERABLE','ERREUR','ESPACE','ESPECE','ESPION','ESPOIR','ESPRIT','ESSIEU','ESTIME','ETABLE','ETABLI','ETALER','ETIRER','ETOFFE','ETOILE','ETROIT','EVITER','EXAMEN','FRAUDE','FACHER','FACILE','FAIBLE','FAMEUX','FARINE','FAUSSE','FAVORI','FENDRE','FERMER','FEROCE','FESTIN','FIDELE','FIEVRE','FIGURE','FINALE','FLAMME','FLECHE','FLEUVE','FLOCON','FLOTTE','FONCER','FONDRE','FORCER','FORGER','FORMER','FRAISE','FROLER','FUREUR','FUSEAU','GATEAU','GAGNER','GARAGE','GARDER','GAUCHE','GENTIL','GERANT','GERMER','GIRAFE','GLACER','GLOIRE','GOUTER','GOUTTE','GRAINE','GRAMME','GRANGE','GRAPPE','GRASSE','GRIFFE','GRILLE','GRIPPE','GROSSE','GROTTE','GROUPE','GUENON','GUERIR','GUERRE','GUEULE','GUIDER','HACHIS','HABILE','HANCHE','HANGAR','HASARD','HOCKEY','HUILER','HUITRE','HUMAIN','HUMBLE','HUMEUR','HUMIDE','INDIEN','IMITER','IMPAIR','INFINI','INJURE','INTIME','ISOLER','JOUEUR','JALOUX','JAMAIS','JAMBON','JAPPER','JARDIN','JAUNIR','JEUNER','JOUJOU','JOYEUX','JUMENT','JUNGLE','KLAXON','KARATE','KIMONO','LARDON','LACHER','LAITUE','LANCER','LANGUE','LAPINE','LAVABO','LAVEUR','LECHER','LEGUME','LEQUEL','LETTRE','LIEVRE','LIMITE','LIONNE','LIVRER','LOCAUX','LOISIR','LONGER','LONGUE','LUTTER','MAISON','MACHER','MADAME','MAIGRE','MAILLE','MAITRE','MAJEUR','MALADE','MANCHE','MANEGE','MANGER','MANIER','MANQUE','MANUEL','MARBRE','MARCHE','MARIER','MARQUE','MASQUE','MASSIF','MEFIER','MEMBRE','MENAGE','MENTIR','MENTON','MERITE','MESURE','METIER','METTRE','MEUBLE','MIENNE','MIETTE','MILIEU','MINUIT','MINUTE','MIROIR','MISERE','MOBILE','MODELE','MOMENT','MONTER','MONTRE','MOQUER','MORALE','MORDRE','MORTEL','MOTEUR','MOUCHE','MOULIN','MOURIR','MOUSSE','MOUTON','MUGUET','MUSCLE','MUSEAU','NOVICE','NAGEUR','NAITRE','NARINE','NATION','NATURE','NAVIRE','NEIGER','NIVEAU','NOMBRE','NOMMER','NORMAL','NOUVEL','NUMERO','ORIENT','OBSCUR','ODORAT','OFFERT','OFFRIR','OIGNON','OISEAU','OPERER','ORANGE','ORDURE','OUVERT','OUVRIR','PLANTE','PAILLE','PALAIS','PANIER','PAPIER','PAQUET','PARADE','PARDON','PAREIL','PARENT','PARFUM','PARLER','PAROLE','PARTIE','PARTIR','PARURE','PASSER','PATATE','PATRIE','PATRON','PAUVRE','PAVAGE','PECHER','PEIGNE','PELAGE','PELURE','PENDRE','PENSER','PERCER','PERDRE','PERMIS','PERRON','PESANT','PETALE','PEUPLE','PHOQUE','PHRASE','PIERRE','PIGEON','PIGNON','PILOTE','PILULE','PINCER','PIQUER','PIQUET','PIQURE','PIRATE','PLACER','PLAINE','PLAIRE','PLAQUE','PLUTOT','POESIE','POINTE','POINTU','POIVRE','POLICE','PONDRE','PORTER','POSTAL','POSTER','POTEAU','POUDRE','POULET','POULIE','POUMON','POUTRE','PRETER','PRETRE','PREUVE','PRIERE','PRINCE','PRISON','PROCHE','PROFIT','PROJET','PROPRE','PROMPT','PUBLIC','PYJAMA','QUICHE','QUATRE','QUELLE','QUILLE','QUINZE','RAVAGE','RABAIS','RACINE','RADEAU','RAGOUT','RAISIN','RAISON','RANGER','RAPIDE','RASOIR','RATEAU','RAPACE','RECORD','REFLET','REFUGE','REGARD','REGIME','REGION','REGRET','REMEDE','RENARD','RENDRE','REQUIN','RESTER','RETARD','RETOUR','REVEIL','REVERS','REVOIR','RIDEAU','RIGOLE','RINCER','RISQUE','RIVAGE','ROCHER','ROMPRE','RONGER','ROSIER','ROUGIR','ROULER','ROUSSE','RUELLE','RYTHME','SORTIE','SAISON','SALADE','SALUER','SAMEDI','SAUMON','SAUTER','SAUVER','SAVANT','SAVOIR','SEANCE','SECHER','SECOND','SECRET','SEJOUR','SENTIR','SERRER','SERVIR','SEVERE','SIECLE','SIGNAL','SIGNER','SIMPLE','SIRENE','SOCIAL','SOLDAT','SOLEIL','SOLIDE','SOMBRE','SOMMET','SONGER','SONNER','SONORE','SORTIR','SOUPER','SOUPIR','SOUPLE','SOURCE','SOURIS','STATUE','SUIVRE','TOMATE','TACHER','TAILLE','TALENT','TANTOT','TAPAGE','TEINTE','TEMOIN','TENDRE','TENNIS','TENTER','TICKET','TIMBRE','TIMIDE','TIROIR','TOMBER','TONDRE','TORDRE','TORTUE','TOUFFE','TOUPIE','TRACER','TRAFIC','TRAIRE','TREFLE','TREIZE','TRENTE','TRESOR','TRESSE','TRICOT','TRISTE','TROUPE','TRUITE','TULIPE','TUNNEL','UTOPIE','UNIQUE','URGENT','VACCIN','VALEUR','VALISE','VALOIR','VALSER','VANTER','VAPEUR','VEILLE','VENDRE','VENTRE','VERGER','VERNIS','VERROU','VERSER','VESTON','VIADUC','VIANDE','VIERGE','VILAIN','VIOLET','VIOLON','VISITE','VISSER','VIVANT','VOGUER','VOISIN','VOLCAN','VOLEUR','VOLUME','VOYAGE','WHISKY','YAOURT','ZOUAVE','ZIGZAG','ZAPPER','ZEBRER','ZENITH','ZEPHYR','ZESTER','ZINZIN','ZOMBIE','ZOOMER','KATANA','YOURTE','YODLER','WAPITI','WASABI','WIDGET']
def init_mot():
    global mot, mots
    x = randint(0,len(liste_mot)-1)
    print(len(liste_mot))
    print(liste_mot[2])
    mot = liste_mot[x]
    mots = mot.upper()
    for c in range(len(mots)):
        liste_lettre_mot.append(mots[c])

compteur_erreur = 0
compteur_juste = 0
contenue = saisie.get()
liste_lettre_entre = []

def getEntry():
    global compteur_erreur, contenue, compteur_relancer, liste_lettre_entre, liste_trait, liste_dessin, liste_dessin1, liste_dessin2, liste_dessin3, liste_dessin4
    canvas.itemconfig(message_erreur1, text="")
    canvas.itemconfig(message_erreur2, text="")
    canvas.itemconfig(message_erreur3, text="")
    if compteur_relancer == 1 :
        liste_lettre_entre = []
    else :
        contenue = saisie.get()
        contenu = contenue.upper()
        if contenu not in liste_lettre_entre :
            verification()
            verification_victoire()
        else :
            canvas.itemconfig(message_erreur3, text="Cette lettre est \ndéjà entrée")
            
        liste_lettre_entre.append(contenu)
        
        if len(contenu) >= 2 :
            canvas.itemconfig(message_erreur2, text="Il ne faut pas \nplus d'un caractère")
            remove_text()
        elif len(contenu) < 1 :
            canvas.itemconfig(message_erreur2, text="Il faut mettre \nun seul caractère")
            remove_text()
        elif len(contenu) == 1 :
            if contenu not in liste_lettre :
                canvas.itemconfig(message_erreur1, text="Il faut mettre une lettre")
            elif contenu not in liste_lettre_mot :
                if contenu not in liste_lettre_erreur :
                    if compteur_erreur == 0 :
                        lettre_erreur1 = contenu
                        canvas.itemconfig(case_lettre_erreur1, text=lettre_erreur1)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin:
                            if compteur_dessin <= 0 :
                                canvas.itemconfig(dessin, fill = couleur_structure)
                                compteur_dessin += 1
                        
                    elif compteur_erreur == 1 :
                        lettre_erreur2 = contenu
                        canvas.itemconfig(case_lettre_erreur2, text=lettre_erreur2)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin:
                            if compteur_dessin <= 1 :
                                canvas.itemconfig(dessin, fill = couleur_structure)
                                compteur_dessin += 1
                        
                    elif compteur_erreur == 2 :
                        lettre_erreur3 = contenu
                        canvas.itemconfig(case_lettre_erreur3, text=lettre_erreur3)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin:
                            if compteur_dessin <= 2 :
                                canvas.itemconfig(dessin, fill = couleur_structure)
                                compteur_dessin += 1
                        
                    elif compteur_erreur == 3 :
                        lettre_erreur4 = contenu
                        canvas.itemconfig(case_lettre_erreur4, text=lettre_erreur4)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin:
                            if compteur_dessin <= 3 :
                                canvas.itemconfig(dessin, fill = couleur_structure)
                                compteur_dessin += 1
                        
                    elif compteur_erreur == 4 :
                        lettre_erreur5 = contenu
                        canvas.itemconfig(case_lettre_erreur5, text=lettre_erreur5)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin:
                            if compteur_dessin <= 4 :
                                canvas.itemconfig(dessin, fill = couleur_structure)
                                compteur_dessin += 1

                    elif compteur_erreur == 5 :
                        lettre_erreur6 = contenu
                        canvas.itemconfig(case_lettre_erreur6, text=lettre_erreur6)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin:
                            if compteur_dessin <= 5 :
                                canvas.itemconfig(dessin, fill = couleur_structure)
                                compteur_dessin += 1

                    elif compteur_erreur == 6 :
                        lettre_erreur7 = contenu
                        canvas.itemconfig(case_lettre_erreur7, text=lettre_erreur7)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin1:
                            if compteur_dessin <= 0 :
                                canvas.itemconfig(dessin, outline=couleur_personnage)
                                compteur_dessin += 1

                    elif compteur_erreur == 7 :
                        lettre_erreur8 = contenu
                        canvas.itemconfig(case_lettre_erreur8, text=lettre_erreur8)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin2:
                            if compteur_dessin <= 0 :
                                canvas.itemconfig(dessin, fill = couleur_personnage)
                                compteur_dessin += 1
                 
                    elif compteur_erreur == 8 :
                        lettre_erreur9 = contenu
                        canvas.itemconfig(case_lettre_erreur9, text=lettre_erreur9)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin2:
                            if compteur_dessin <= 1 :
                                canvas.itemconfig(dessin, fill = couleur_personnage)
                                compteur_dessin += 1
                        
                    elif compteur_erreur == 9 :
                        lettre_erreur10 = contenu
                        canvas.itemconfig(case_lettre_erreur10, text=lettre_erreur10)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin2:
                            if compteur_dessin <= 2 :
                                canvas.itemconfig(dessin, fill = couleur_personnage)
                                compteur_dessin += 1

                    elif compteur_erreur == 10 :
                        lettre_erreur11 = contenu
                        canvas.itemconfig(case_lettre_erreur11, text=lettre_erreur11)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin2:
                            if compteur_dessin <= 3 :
                                canvas.itemconfig(dessin, fill = couleur_personnage)
                                compteur_dessin += 1

                    elif compteur_erreur == 11 :
                        lettre_erreur12 = contenu
                        canvas.itemconfig(case_lettre_erreur12, text=lettre_erreur12)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin2:
                            if compteur_dessin <= 4 :
                                canvas.itemconfig(dessin, fill = couleur_personnage)
                                compteur_dessin += 1

                    elif compteur_erreur == 12 :
                        lettre_erreur13 = contenu
                        canvas.itemconfig(case_lettre_erreur13, text=lettre_erreur13)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        compteur_dessin = 0
                        for dessin in liste_dessin3:
                            canvas.itemconfig(dessin, fill = couleur_personnage)

                    elif compteur_erreur == 13 :
                        lettre_erreur14 = contenu
                        canvas.itemconfig(case_lettre_erreur14, text=lettre_erreur14)
                        compteur_erreur += 1
                        liste_lettre_erreur.append(contenu)
                        for dessin in liste_dessin4:
                            canvas.itemconfig(dessin, fill = couleur_personnage)
                        perdu()
                else :
                    canvas.itemconfig(message_erreur3, text="Cette lettre est \ndéjà entrée")
            remove_text()

def getEntry2(event):
    getEntry()

##########################################################################################

def main():
    liste_lettre_texte = [lettre_texte1, lettre_texte2, lettre_texte3, lettre_texte4, lettre_texte5, lettre_texte6, lettre_texte7, lettre_texte8, lettre_texte9 , lettre_texte10, lettre_texte11, lettre_texte12]
    boutonR.config(state = tkinter.DISABLED)
    for c in liste_lettre_texte :
            canvas.itemconfig(c, text="")
    init_mot()
    trait_mot()

def remove_text():
    saisie.delete(0, len(saisie.get()))
    
def del_dessin():
    for dessin in liste_dessin:
        canvas.itemconfig(dessin, fill = couleur_fond)
    for dessin in liste_dessin1:
        canvas.itemconfig(dessin, outline = couleur_fond)
    for dessin in liste_dessin2:
        canvas.itemconfig(dessin, fill = couleur_fond)
    for dessin in liste_dessin3:
        canvas.itemconfig(dessin, fill = couleur_fond)
    for dessin in liste_dessin4:
        canvas.itemconfig(dessin, fill = couleur_fond)
    
def trait_mot():
    global liste_lettre, compteur_lettres_reeles, liste_trait, mots
    compteur_local = 0
    if len(mots) < 2 or len(mots) > 12:
        arret_forcer()
    else :
        for trait in liste_trait:
            if compteur_local != len(mots) :
                compteur_local += 1
                canvas.itemconfig(trait, fill = couleur_structure)
    for c in range(len(mots)):
        if c not in liste_lettre :
            compteur_lettres_reeles += 1 
    caractere_speciaux()
    caractere_speciaux2()

compteur_lettre = 0

def caractere_speciaux():
    global compteur_victoire, compteur_relancer, liste_lettre_mot, compteur_lettre
    liste_lettre_texte = [lettre_texte1, lettre_texte2, lettre_texte3, lettre_texte4, lettre_texte5, lettre_texte6, lettre_texte7, lettre_texte8, lettre_texte9 , lettre_texte10, lettre_texte11, lettre_texte12]
    caractere = "-"
    if compteur_relancer == 1 :
        position = 0
        compteur_lettre = 0
        compteur_relancer = 0
        compteur_victoire = 0
        liste_lettre_mot = []
    else : 
        if caractere in mots :
            position = 0
            compteur_lettre = 0
            lettre = caractere
            len_lettre = liste_lettre_mot.count(lettre)
            compteur_victoire += len_lettre
            while compteur_lettre < len_lettre :
                w = liste_lettre_mot.index(lettre, position) # Find next letter starting a position x
                position = w + 1
                compteur_lettre += 1
                if position == 1 :
                    canvas.itemconfig(lettre_texte1, text=lettre)
                    disparition_trait_mot1()
                elif position == 2 :
                    canvas.itemconfig(lettre_texte2, text=lettre)
                    disparition_trait_mot2()
                elif position == 3 :
                    canvas.itemconfig(lettre_texte3, text=lettre)
                    disparition_trait_mot3()
                elif position == 4 :
                    canvas.itemconfig(lettre_texte4, text=lettre)
                    disparition_trait_mot4()
                elif position == 5 :
                    canvas.itemconfig(lettre_texte5, text=lettre)
                    disparition_trait_mot5()
                elif position == 6 :
                    canvas.itemconfig(lettre_texte6, text=lettre)
                    disparition_trait_mot6()
                elif position == 7 :
                    canvas.itemconfig(lettre_texte7, text=lettre)
                    disparition_trait_mot7()
                elif position == 8 :
                    canvas.itemconfig(lettre_texte8, text=lettre)
                    disparition_trait_mot8()
                elif position == 9 :
                    canvas.itemconfig(lettre_texte9, text=lettre)
                    disparition_trait_mot9()
                elif position == 10 :
                    canvas.itemconfig(lettre_texte10, text=lettre)
                    disparition_trait_mot10()
                elif position == 11 :
                    canvas.itemconfig(lettre_texte11, text=lettre)
                    disparition_trait_mot11()
                elif position == 12 :
                    canvas.itemconfig(lettre_texte12, text=lettre)
                    disparition_trait_mot12()
                    
def caractere_speciaux2():
    global compteur_victoire, compteur_relancer, liste_lettre_mot, compteur_lettre
    liste_lettre_texte = [lettre_texte1, lettre_texte2, lettre_texte3, lettre_texte4, lettre_texte5, lettre_texte6, lettre_texte7, lettre_texte8, lettre_texte9 , lettre_texte10, lettre_texte11, lettre_texte12]
    caractere = " "
    if compteur_relancer == 1 :
        position = 0
        compteur_lettre = 0
        compteur_relancer = 0
        compteur_victoire = 0
        liste_lettre_mot = []
    else : 
        if caractere in mots :
            position = 0
            compteur_lettre = 0
            lettre = caractere
            len_lettre = liste_lettre_mot.count(lettre)
            compteur_victoire += len_lettre
            while compteur_lettre < len_lettre :
                w = liste_lettre_mot.index(lettre, position) # Find next letter starting a position x
                position = w + 1
                compteur_lettre += 1
                if position == 1 :
                    canvas.itemconfig(lettre_texte1, text=lettre)
                    disparition_trait_mot1()
                elif position == 2 :
                    canvas.itemconfig(lettre_texte2, text=lettre)
                    disparition_trait_mot2()
                elif position == 3 :
                    canvas.itemconfig(lettre_texte3, text=lettre)
                    disparition_trait_mot3()
                elif position == 4 :
                    canvas.itemconfig(lettre_texte4, text=lettre)
                    disparition_trait_mot4()
                elif position == 5 :
                    canvas.itemconfig(lettre_texte5, text=lettre)
                    disparition_trait_mot5()
                elif position == 6 :
                    canvas.itemconfig(lettre_texte6, text=lettre)
                    disparition_trait_mot6()
                elif position == 7 :
                    canvas.itemconfig(lettre_texte7, text=lettre)
                    disparition_trait_mot7()
                elif position == 8 :
                    canvas.itemconfig(lettre_texte8, text=lettre)
                    disparition_trait_mot8()
                elif position == 9 :
                    canvas.itemconfig(lettre_texte9, text=lettre)
                    disparition_trait_mot9()
                elif position == 10 :
                    canvas.itemconfig(lettre_texte10, text=lettre)
                    disparition_trait_mot10()
                elif position == 11 :
                    canvas.itemconfig(lettre_texte11, text=lettre)
                    disparition_trait_mot11()
                elif position == 12 :
                    canvas.itemconfig(lettre_texte12, text=lettre)
                    disparition_trait_mot12()

##########################################################################################

co_lettre_y = 655 #20px de moins que le trait, pour être au dessus
co_lettre1_x = 75 #entre le premier x et le deuxième du trait (milieu des deux)
co_lettre2_x = 150
co_lettre3_x = 225
co_lettre4_x = 300
co_lettre5_x = 375
co_lettre6_x = 450
co_lettre7_x = 525
co_lettre8_x = 600
co_lettre9_x = 675
co_lettre10_x = 750
co_lettre11_x = 825
co_lettre12_x = 900

##########################################################################################

def disparition_trait_mot1():
    canvas.itemconfig(trait_mot1, fill = couleur_fond)

def disparition_trait_mot2():
    canvas.itemconfig(trait_mot2, fill = couleur_fond)

def disparition_trait_mot3():
    canvas.itemconfig(trait_mot3, fill = couleur_fond)

def disparition_trait_mot4():
    canvas.itemconfig(trait_mot4, fill = couleur_fond)

def disparition_trait_mot5():
    canvas.itemconfig(trait_mot5, fill = couleur_fond)
    
def disparition_trait_mot6():
    canvas.itemconfig(trait_mot6, fill = couleur_fond)
    
def disparition_trait_mot7():
    canvas.itemconfig(trait_mot7, fill = couleur_fond)

def disparition_trait_mot8():
    canvas.itemconfig(trait_mot8, fill = couleur_fond)

def disparition_trait_mot9():
    canvas.itemconfig(trait_mot9, fill = couleur_fond)
    
def disparition_trait_mot10():
    canvas.itemconfig(trait_mot10, fill = couleur_fond)

def disparition_trait_mot11():
    canvas.itemconfig(trait_mot11, fill = couleur_fond)

def disparition_trait_mot12():
    canvas.itemconfig(trait_mot12, fill = couleur_fond)
    
def disparition_trait():
    global liste_trait
    for trait in liste_trait:
        canvas.itemconfig(trait, fill = couleur_fond)
    
##########################################################################################

compteur_victoire = 0
compteur_relancer = 0

def verification():
    global contenue, liste_lettre_mot, compteur_victoire, compteur_relancer, liste_lettre_texte
    liste_lettre_texte = [lettre_texte1, lettre_texte2, lettre_texte3, lettre_texte4, lettre_texte5, lettre_texte6, lettre_texte7, lettre_texte8, lettre_texte9 , lettre_texte10, lettre_texte11, lettre_texte12]
    if compteur_relancer == 1 :
        compteur_relancer = 0
        compteur_victoire = 0
        compteur_lettre = 0
        position = 0
        liste_lettre_mot = []
    else : 
        position = 0
        compteur_lettre = 0
        lettre = contenue.upper()
        len_lettre = liste_lettre_mot.count(lettre)
        while compteur_lettre < len_lettre :
            w = liste_lettre_mot.index(lettre, position) # Find next letter starting a position x
            position = w + 1
            compteur_lettre += 1
            compteur_victoire += 1
            if position == 1 :
                canvas.itemconfig(lettre_texte1, text=lettre)
            elif position == 2 :
                canvas.itemconfig(lettre_texte2, text=lettre)
            elif position == 3 :
                canvas.itemconfig(lettre_texte3, text=lettre)
            elif position == 4 :
                canvas.itemconfig(lettre_texte4, text=lettre)
            elif position == 5 :
                canvas.itemconfig(lettre_texte5, text=lettre)
            elif position == 6 :
                canvas.itemconfig(lettre_texte6, text=lettre)
            elif position == 7 :
                canvas.itemconfig(lettre_texte7, text=lettre)
            elif position == 8 :
                canvas.itemconfig(lettre_texte8, text=lettre)
            elif position == 9 :
                canvas.itemconfig(lettre_texte9, text=lettre)
            elif position == 10 :
                canvas.itemconfig(lettre_texte10, text=lettre)
            elif position == 11 :
                canvas.itemconfig(lettre_texte11, text=lettre)
            elif position == 12 :
                canvas.itemconfig(lettre_texte12, text=lettre)
                
compteur_lettres_reeles = 0

def rejouer() :
    global compteur_relancer, liste_lettre, liste_lettre_mot, liste_lettre_erreur, liste_lettre_entre, compteur_erreur, mot, mots
    #Fonction reset à coder (qui sera appellé avec le bouton rejouer)
    recommencer = tkinter.messagebox.askretrycancel("Pendu", "Voulez-vous commencer une nouvelle partie ?")
    if recommencer == True:
        compteur_relancer += 1
        disparition_trait()
        del_dessin()
        verification_victoire()
        liste_lettre_mot = []
        liste_lettre_erreur = []
        liste_lettre_entre = []
        compteur_erreur = 0
        getEntry()
        for c in range(len(mots)):
            liste_lettre_mot.append(mots[c])
        for bouton in liste_bouton:
            bouton.configure(state=NORMAL)
        for lettre_fausse in liste_lettre_erreur_afficher :
            canvas.itemconfig(lettre_fausse, text="")
        canvas.itemconfig(message_mot, text="")
        canvas.itemconfig(message_mot_reponse, text="")
        saisie.config(state = tkinter.NORMAL)
        caractere_speciaux()
        caractere_speciaux2()
        verification()
        remove_text()
        main()
        

def verification_victoire():
    global compteur_victoire, compteur_lettres_reeles, compteur_relancer
    if compteur_relancer == 1 :
        compteur_victoire = 0
        compteur_lettres_reeles = 0
    else :
        compteur_entier = compteur_victoire + compteur_lettres_reeles
        if compteur_victoire == len(mots) :
            messagebox.showinfo('Bravo', 'Tu es un BOSS')
            eteindre_bouton()

def eteindre_bouton():
    for bouton in liste_bouton:
        bouton.configure(state=DISABLED)
    saisie.config(state = tkinter.DISABLED)
    boutonR.config(state = tkinter.NORMAL)
        
def perdu():
    eteindre_bouton()
    canvas.itemconfig(message_mot, text="le mot étais : "+ mots)
    messagebox.showinfo('Bravo', 'Tu es un LOSER')

def stop() :
    message = messagebox.askyesno("quitter l'application", "Voulez-vous vraiment quitter le jeu ?")
    if message == True :
        sys.exit()

def arret_forcer() :
    sys.exit()

##########################################################################################

fenetre.bind('<Return>', getEntry2)
main()
fenetre.mainloop()