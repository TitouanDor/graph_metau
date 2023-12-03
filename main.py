###importation###
from extract import*
from algo import*
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import datetime
import os

os.system("cls")

#####programme#####

#region initialisation_variable_de_base ###############################################

###liste###
l_or = []
l_platine = []
l_date = []
l_meteaux_choisi = []
dates = []
liste_annee = [i for i in range(1990 , 2023)]
liste_mois = [i for i in range(1 , 13)]


###booleen###
loop = True
verif_met = False
verif_date = False

###liste de liste###
Table = extraction("metaux.csv")

###Date limite###
start_date = datetime.date(1990 , 1 , 1)
end_date = datetime.date(2022 , 5 , 1)
current_date = start_date

#endregion ####################################################################

#region les listes l_date , l_or et l_platine sont remplit#####################
for i in Table:

    try: int(i[0])
    except: pass
    else: l_date.append(int(i[0]))

    try: float(i[1])
    except: pass
    else: l_or.append(float(i[1]))

    try: float(i[2])
    except: pass
    else: l_platine.append(float(i[2]))

#endregion#####################################################################

#region Generation de la liste des dates#######################################
while current_date <= end_date:
    dates.append(current_date)
    current_date += relativedelta(months = 1)
        
#endregion#####################################################################

#region assertion##############################################################
assert (Minimum([ 1 , 2 , 3 , 6 , 5 , 4 , 7 , 8 , 9 , 0]) == 0) , "erreur la fonction Minimum ne renvoie pas le minimum"
assert (moyenne([ 1 , 2 , 3 , 6 , 5 , 4 , 7 , 8 , 9 , 0]) == 4.5) , "erreur la fonction moyenne ne renvoie pas la moyenne"
assert (rechercheSequentielle([ 1 , 2 , 3 , 6 , 5 , 4 , 7 , 8 , 9 , 0] , 5) == 4) , "erreur la fonction rechercheSequentielle ne renvoie pas le bon indice"
#endregion#####################################################################

while loop:
    print(dates)

    verif_met = verif_date = False
    
    while verif_met == False:
        """Vérifie que le métal choisi soit bien l'or ou le platine"""

        choix_metaux = input("Vous souhaitez etudier le cours de quel minerai (or ou platine) : ")
        
        if (choix_metaux.upper() == "OR"):
            l_meteaux_choisi = l_or.copy()
            verif_met = True
            titre = "Graphique de l'evolution du prix de l'or en once en fonction du temps \nentre Janvier 1990 et Mai 2022"
            os.system("cls")

        elif (choix_metaux.upper() == "PLATINE"):
            l_meteaux_choisi = l_platine.copy()
            verif_met = True
            titre = "Graphique de l'evolution du prix du platine en once en fonction du temps \nentre Janvier 1990 et Mai 2022"
            os.system("cls")

        elif (choix_metaux == ""):
            loop = False
            verif_met = True
            verif_date = True

        else: 
            os.system("cls")
            print("Vous avez mal ortographie le metal souhaite ou l'option saisie n'est pas disponible.")

    while verif_date == False:
        """Vérifie que la date choisie soit bien un entier dans l'intervalle donnée"""

        mois , annee = map(int , input("Saisissez une date avec annee et mois \ncompris entre Janvier 1990 et Mai 2022\n(exemple 12/1999 pour le mois de décembre en 1999) : ").split("/"))
        
        if ((annee == 2022) and ( mois > 5)): 
            print("La date mise est indisponible veuillez mettre une date comprise entre Janvier 1990 et Mai 2022")
        
        elif (annee in liste_annee) and (mois in liste_mois):
            if (mois < 10): mois = "0" + str(mois)
            verif_date = True

        else:
            print("La date mise est indisponible veuillez mettre une date comprise entre Janvier 1990 et Mai 2022")

    if (loop == True):

        ###Calcul de la moyenne et creation de la liste de valeur pour le graphique###
        moy = moyenne(l_meteaux_choisi)
        l_moy = [moy for _ in range(len(l_date))]

        ###Calcul du minimum et creation de la liste de valeur pour le graphique###
        mini = Minimum(l_meteaux_choisi)
        l_mini = [mini for _ in range(len(l_date))]

        ###détermination de l'indice de la date et creation de la liste de valeur pour le graphique###
        choix_date = int(str(annee) + str(mois))
        date_format_bizzare = datetime.date(annee , int(mois) , 1)
        l_date_choisie = [date_format_bizzare for _ in range(len(l_date))]

        ###recher du prix a la date donnee et creation de la liste de valeur pour le graphe###
        prix_a_date = l_meteaux_choisi[int(rechercheSequentielle(l_date , choix_date))]
        
        l_ligne_pour_temps = [1 for _ in range(len(l_date) - 1)]
        l_ligne_pour_temps.insert(-1 , 2000)

        print(f"La valeur moyenne du metal est de : {moy} onces.\nSon prix le plus bas  est de : {mini} onces. \nLe prix du metal lors de la date {mois}/{annee} était de : {prix_a_date} onces")

        #region Graphique###

        ###creation des courbes###
        plt.plot(l_date_choisie , l_ligne_pour_temps , label = f"Date choisie {mois}/{annee} : {prix_a_date} onces" , color = "red")
        plt.plot(dates, l_meteaux_choisi , linewidth = 1.5 , label = "Prix au cours du temps" , color = "blue")
        plt.plot(dates , l_moy , linestyle = "dashed" , linewidth = 1 , label = f"Prix moyen : {round(moy , 2)} onces" , color = "orange")
        plt.plot(dates , l_mini , linestyle = "dashed" , linewidth = 1 , label = f"Prix minimun : {mini} onces" , color = "green")
        
        ###paramettre du graphe###
        plt.xticks(dates[::12] , [date.strftime("%Y") for date in dates[::12]] , rotation=45)
        plt.title(titre , fontdict = {"fontsize" : 14 , "fontweight" : "bold" })
        plt.ylabel("Prix en once")
        plt.xlabel("Annees")
        plt.legend() 
        plt.tight_layout()
        plt.show()

        #endregion
