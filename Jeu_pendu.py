
class Application(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Le jeu du pendu')                    # création du titre de la fenètre
        self.root.iconbitmap('images/pendu_image_Poupe.ico')  # création de l'icone
        self.root.resizable(False, False)                     # permet de garder une taille de fenêtre fixe
        self.root.geometry("905x637")                         # définie la taille de la fenêtre

        # création du background de la fenêtre de commencement

        background_image = PhotoImage(file='images/images_background/9-pendu-full-ConvertImage.png')
        self.background_label = Label(self.root, image=background_image)
        self.background_label.pack()

        # création de tous les widgets dont on a besoin à partir du lancement de l'application jusqu'à la fin du jeu
        # font='times 18' permet de changer la caligraphie du test

        self.bouton_jouer = Button(self.root, text='Jouer', command=self.game_init, font='times 18')
        self.bouton_jouer.place(x=250, y=480)

        self.bouton_quitter = Button(self.root, text='Quitter', command=self.quitter_application, font='times 18')
        self.bouton_quitter.place(x=600, y=480)

        self.bouton_valider = Button(self.root, text='Valider', command=self.game_actu, font='times 18')
        self.bouton_valider.place_forget()


        self.bouton_recommencer = Button(self.root, text="Recommencer", command=self.game_init, font='times 18')
        self.bouton_recommencer.place_forget()


        self.label_message_bienvenue = Label(self.root, text='Bienvenue au jeu du pendu !', font='times 24')
        self.label_message_bienvenue.place(x=320, y=100)

        self.label_lettres_tentees = Label(self.root, text="Lettres déjà essayées :", font='times 14')
        self.label_lettres_tentees.place_forget()


        self.label_entrer_lettre = Label(self.root, text="Entrez une lettre:", font='times 18')
        self.label_entrer_lettre.place_forget()


        self.label_commentaire = Label(self.root, text="Bravo vous avez trouvé une lettre!", font='times 12')
        self.label_commentaire.place_forget()


        self.label_message_fin = Label(self.root, text="Bravo vous avez gagné !!!", font='times 14')
        self.label_message_fin.place_forget()

        self.label_lettres_cachees = Label(self.root, text="", font='times 18')
        self.label_lettres_cachees.place_forget()


        self.entree = Entry(self.root, width=14, font='times 18')
        self.entree.place_forget()


        self.root.mainloop()

    def game_init(self):

        # réinitialisation des variables de jeu

        self.mot_a_trouver = self.motatrouver()
        self.lettres_trouvees = []
        self.nb_max_coups = 9
        self.nb_coups = 0
        self.lettres_testees = []
        texte_cache = self.mot_masque()

        # réinitialisation du background

        self.background(0)

        # les boutons jouer et recommencer sont invisibles et on place les boutons valider et quitter

        self.bouton_jouer.place_forget()
        self.bouton_quitter.place(x=145, y=550)
        self.bouton_valider.place(x=675, y=550)
        self.bouton_recommencer.place_forget()

        # message de bienvenue et de fin caché

        self.label_message_bienvenue.place_forget()
        self.label_message_fin.place_forget()
        self.label_lettres_cachees.configure(text=texte_cache)  # le texte affiche le mot masqué avec des tirets
        self.label_lettres_cachees.place(x=430, y=100)
        self.label_entrer_lettre.place(x=375, y=530)
        self.entree.place(x=375, y=570)
        self.label_lettres_tentees.place(x=10, y=150)
        self.label_lettres_tentees.configure(text="Lettres déjà essayées : ", font='times 12')

    def motatrouver(self):

    # cette fonction rend un mot tiré au hasard dans la liste de mot

        liste_mots = [
            "hepia",
            "python",
            "poule",
            "tortue",
            "ecole",
            "renard",
            "poisson",
            "chat",
            "table",
            "superman",
            "stupeur",
            "bisous",
            "saperlipopette",
            "piscine"
        ]
        self.mot_a_trouver = rd.choice(liste_mots)
        return self.mot_a_trouver

    def mot_masque(self):

    # cette fonction retourne le mot masqué avec les lettres trouvées qui s'affichent

        mot_masque = ""

        for lettre in self.mot_a_trouver:

            if lettre in self.lettres_trouvees:
                mot_masque += lettre

            else:

                mot_masque += "_ "

        return mot_masque

    def quitter_application(self):

    # cette fonction permet de fermer et quitter l'application

        self.root.destroy()
        self.root.quit()

    def background(self, x):

    # cette fonction rend l'image en fonction du x choisit

        # implémentation des images dans une liste

        backgrounds = [PhotoImage(file='images/images_background/0-background-ConvertImage.png'),
                       PhotoImage(file='images/images_background/1-pendu-sans-barre-verticale-ConvertImage.png'),
                       PhotoImage(file='images/images_background/2-pendu-sans-barre-horizon-ConvertImage.png'),
                       PhotoImage(file='images/images_background/3-pendu-sans-tete-ConvertImage.png'),
                       PhotoImage(file='images/images_background/4-pendu-sans-corps-ConvertImage.png'),
                       PhotoImage(file='images/images_background/5-pendu-sans-bras-gauche-ConvertImage.png'),
                       PhotoImage(file='images/images_background/6-pendu-sans-bras-droit-ConvertImage.png'),
                       PhotoImage(file='images/images_background/7-pendu-sans-jambe-droite-ConvertImage.png'),
                       PhotoImage(file='images/images_background/8-pendu-sans-jambe-gauche-ConvertImage.png'),
                       PhotoImage(file='images/images_background/9-pendu-full-ConvertImage.png')]

        background_image = backgrounds[x]                        # l'image correspond au numéro choisit
        self.background_label.configure(image=background_image)  # configuration image
        self.background_label.image = background_image           # implémentation image

    def game_actu(self):

    # lorsqu'on appuis sur le bouton valider cela lance cette fonction qui actualise le jeu

        lettre = self.entree.get()     #la lettre qui se trouve dans l'entree est prise
        lettre = lettre.lower()        # on la met en miniscule

        if lettre.isalpha() is True and len(lettre) == 1:                                                      # si la lettre est une lettre de longueur 1 :
            if lettre in self.lettres_testees:                                                                 # et si la lettre se trouve déjà dans les lettre testees :
                self.label_commentaire.configure(text="Vous avez déjà entré cette lettre", font='times 12')    # alors on configure le commentaire
                self.label_commentaire.place(x=100, y=500)                                                     # et on affiche le commentaire

            else:                                            # si c'est une nouvelle lettre :
                self.lettres_testees.append(lettre)          # on met la lettre dans les lettres testées

                if lettre in self.mot_a_trouver:             # et si la lettre ce trouve dans le mot à trouver
                    self.lettres_trouvees.append(lettre)     # on met la lettre dans les lettre trouvées

                    if self.mot_a_trouver == self.mot_masque():                                              # si le mot à trouver est égale a ce que rend la fonction mot masque alors le mot est trouvé
                        self.end_game("Bravo ! Vous avez deviné le mot '{}' !".format(self.mot_a_trouver))   # et on peut lancer la fonction de fin du jeu (end_game) avec le message écrit ci-contre.
                                                                                                             # le .format(self.mot_a_trouver) permet de mettre le mot entier dans le text à la place des "{}"
                    else:
                        self.label_commentaire.configure(text="Bravo vous avez trouvé une lettre!", font='times 12')  # sinon le mot n'est pas trouvé mais la lettre est bonne et on configure le commentaire
                        self.label_commentaire.place(x=100, y=500)                                                    # puis on le place
                        self.label_lettres_cachees.configure(text=self.mot_masque())                                  # et on mets a jour le mot caché avec les tirets puisque une lettre a été trouvée

                else:                                                                                       # si la lettre n'est pas dans le mot à trouver
                    self.nb_coups += 1                                                                      # on rajoute 1 au nombre de coups
                    self.background(self.nb_coups)                                                          # et on change le background avec l'image qui correspond au nombre de coup (le pendu se pend)
                    self.label_commentaire.configure(text="Dommage, essayez encore !", font='times 12')     # on configure le commentaire
                    self.label_commentaire.place(x=100, y=500)                                              # et on le place

        else:                                                                                           # si dans l'entrée ce n'est pas une unique lettre
            self.label_commentaire.configure(text="Vous n'avez pas entré une lettre", font='times 12')  # on configure le commentaire et on le place
            self.label_commentaire.place(x=100, y=500)

        if self.nb_coups == self.nb_max_coups:                                                        # si le nombre de coup max est atteint (9)
            self.end_game("Dommage, vous avez perdu ! Le mot était: '{}'".format(self.mot_a_trouver)) # on lance la fonction end_game avec le message ci-contre

        self.label_lettres_tentees.configure(text="Lettres déjà essayées : {} ".format(", ".join(self.lettres_testees)), font='times 12')  # dans tout les cas on met à jour les lettres qui ont été testées et on les affiches
                                                                                                                                           # .format(", ".join(self.lettres_testees)) permet d'afficher les lettres qui se trouve dans la liste en les séparant d'une virgule et d'un espace

    def end_game(self, message):

        # à la fin du jeu, le bouton valider disparaît et le bouton recommencer est placé

        self.bouton_valider.place_forget()
        self.bouton_recommencer.place(x=605, y=550)
        self.bouton_quitter.place(x=145, y=550)

        # tous les labels et les zones d'entrées sont cachés et un message de fin annonce si la partie est gagnée ou pas

        self.label_commentaire.place_forget()
        self.label_lettres_cachees.place_forget()
        self.label_lettres_tentees.place_forget()
        self.label_entrer_lettre.place_forget()
        self.entree.place_forget()
        self.label_message_fin.configure(text=message)  # on utilise un paramètre 'messsage' ce qui permet d'appeler le label
                                                        # dans les 2 situations possibles et d'adapter le message en fonction
        self.label_message_fin.place(x=300, y=50)

# Programme principal :
if __name__ == '__main__':
    from tkinter import *
    import random as rd

    f = Application()  # instanciation de l'objet application
