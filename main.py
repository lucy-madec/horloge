import time

# Heure sous forme de Tuple
heure_form_tuple = (0, 0, 0)
heure_actuelle = list(heure_form_tuple)

# Saisie de l'heure par l'utilisateur
heures = int(input("Modifier l'heure :"))
minutes = int(input("Modifier les minutes :"))
secondes = int(input("Modifier les secondes :"))

# Paramétrer alarme
alarme = None

class horloge():

    def afficher_heure():
        global heure_actuelle
        affichage_heure = "{:02d}:{:02d}:{:02d}".format(heure_actuelle[0],heure_actuelle[1],heure_actuelle[2])
        print(affichage_heure)

    def regler_heure(edit_heures, edit_minutes, edit_secondes):
        global heure_actuelle
        heure_actuelle = [edit_heures, edit_minutes, edit_secondes]
        horloge.afficher_heure()

    def regler_alarme():
        global alarme
        choix_alarme = input("Voulez-vous mettre une alarme ? Réponse uniquement par Oui ou par Non  :  ")
        if choix_alarme == "Oui":
            edit_heures = int(input("Choisissez l'heure :"))
            edit_minutes = int(input("Choisissez les minutes :"))
            edit_secondes = int(input("Choisissez les secondes :"))
            alarme = [edit_heures, edit_minutes, edit_secondes]
            print("Alarme modifiée avec succès.")

        elif choix_alarme == "Non":
            horloge.afficher_heure()
            horloge.raffraichir_heure()
        
        else:
            print("Réponse non valide. Veuillez répondre seulement par Oui ou par Non")
            horloge.regler_alarme()

    def verifier_alarme():
        global heure_actuelle, alarme
        if alarme is not None and heure_actuelle == alarme:
            print("Il est l'heure de se réveiller Les Plateformiens !")

    def raffraichir_heure():
        global heure_actuelle
        while True:
            time.sleep(1)      
            heure_actuelle[2] += 1
            if heure_actuelle[2] == 60:
                heure_actuelle[1] += 1
                heure_actuelle[2] = 0
                if heure_actuelle[1] == 60:
                    heure_actuelle[0] += 1
                    heure_actuelle[1] = 0
            
            horloge.afficher_heure()
            horloge.verifier_alarme()


horloge.regler_heure(heures, minutes, secondes)
horloge.regler_alarme()

while True:
    horloge.raffraichir_heure()
