from customtkinter import *
import tkinter.messagebox as messagebox
from my_class.Mot_de_passe import Mot_de_passe
from my_class.Utilisateur import Utilisateur
import re

root = CTk()
root.geometry("800x500+450+150")
root.title("Connexion")
utilisateur = Utilisateur('localhost', 'root', 'root', 'mydiscord')
mot_de_passe = Mot_de_passe()

fenetre = CTkFrame(root)
fenetre.place(relx=0.5, rely=0.5, anchor=CENTER)
# fenetre.pack()

def valid_reinit_mdp(page_reset_mdp, mdp_entry, mdp2_entry, mail_entry):

    statut_mot_de_passe = mot_de_passe.verif_mdp(mdp_entry.get())

    verif = False

    if mdp2_entry.get() == "" or mdp_entry.get() == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs !")

    elif mdp_entry.get() != mdp2_entry.get():
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas !")

    elif statut_mot_de_passe == "Mot de passe non valide":
        messagebox.showerror("Erreur", "Le mot de passe n'est pas assez sécurisé. \
                             \nIl doit contenir au moins 8 caractères et doit être composé d'au moins un chiffre, une minuscule, une majuscule et un caractère spécial !")
    
    else:
        try:
            utilisateur.maj(f'"mdp" = {mdp_entry.get()}', f'"mail" = {mail_entry.get()}')
            verif = True

        except:
            messagebox.showerror("Erreur", "Une erreur est survenue !")

    if verif:
        page_reset_mdp.destroy()
        reponse = messagebox.askyesno("Réinitialisation du mot de passe", "Voulez vous vraiment réinisialisez mot de passe !")
        if reponse:
            messagebox.showinfo("Réinitialisation du mot de passe", "Le mot de passe a été réinitialisé avec succès !")

def valid_mail_reset_mdp(mail_entry, page_reset_mdp_mail):
    email_format = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if mail_entry.get() == "" or mail_entry.get() not in utilisateur.lecture():
        messagebox.showerror("Erreur", "Aucun compte n'est associé à ce compte !")

    elif not re.search(email_format, mail_entry.get()):
        messagebox.showerror("Erreur", "L'adresse mail n'est pas valide !") 

    else:
        page_reset_mdp_mail.destroy()
        page_reset_mdp = CTkToplevel(root)
        page_reset_mdp.geometry("400x150+800+400")
        page_reset_mdp.title("Réinitialisation du mot de passe")

        mdp_label = CTkLabel(page_reset_mdp, text="Réinitialisation du mot de passe")
        mdp_entry = CTkEntry(page_reset_mdp, width=180, validate = 'key', show="*")
        mdp_checkbox = BooleanVar()
        mdp_checkbox.set(False)
        mdp_checkbox_button = CTkCheckBox(page_reset_mdp, variable=mdp_checkbox, text="Afficher le mot de passe", command= lambda *args: toggle_password(mdp_entry, mdp_checkbox))

        mdp2_label = CTkLabel(page_reset_mdp, text="Confirmer le mot de passe")
        mdp2_entry = CTkEntry(page_reset_mdp, width=180, validate = 'key', show="*")
        mdp2_checkbox = BooleanVar()
        mdp2_checkbox.set(False)
        mdp2_checkbox_button = CTkCheckBox(page_reset_mdp, variable=mdp2_checkbox, text="Afficher le mot de passe", command= lambda *args: toggle_password(mdp2_entry, mdp2_checkbox))

        mdp_label.grid(row=0, column=0, columnspan=2)
        mdp_entry.grid(row=1, column=0, padx=10)
        mdp_checkbox_button.grid(row=1, column=1)

        mdp2_label.grid(row=2, column=0, columnspan=2)
        mdp2_entry.grid(row=3, column=0, padx=10)
        mdp2_checkbox_button.grid(row=3, column=1)

        valid_reinit_mdp_button = CTkButton(page_reset_mdp, text="Valider", command= lambda: valid_reinit_mdp(page_reset_mdp, mdp_entry, mdp2_entry, mail_entry))
        valid_reinit_mdp_button.grid(row=4, column=0, columnspan=2, pady=5)

        page_reset_mdp.grab_set()

def valid_creation_compte(fenetre, nom_entry, prenom_entry, email_entry, age_entry, mdp_entry, mdp2_entry, pseudo_discord_entry):
    statut_mot_de_passe = mot_de_passe.verif_mdp(mdp_entry.get())

    verif = False
    email_format = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    values = [nom_entry.get(), prenom_entry.get(), email_entry.get(), pseudo_discord_entry.get(), age_entry.get()]

    if nom_entry.get() == "" or prenom_entry.get() == "" or email_entry.get() == "" or age_entry.get() == "" or mdp_entry.get() == "" or mdp2_entry.get() == "" or pseudo_discord_entry.get() == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs !")

    elif statut_mot_de_passe == "Mot de passe non valide":
        messagebox.showerror("Erreur", "Le mot de passe n'est pas assez sécurisé. \
                             \nIl doit contenir au moins 8 caractères et doit être composé d'au moins un chiffre, une minuscule, une majuscule et un caractère spécial !")
    
    elif not re.search(email_format, email_entry.get()):
        messagebox.showerror("Erreur", "L'adresse mail n'est pas valide !")

    elif mdp_entry.get() != mdp2_entry.get():
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas !")
    
    else:
        try:
            if utilisateur.verif_email(values[2]):
                utilisateur.ajout(values[0], values[1], values[2], statut_mot_de_passe, values[3], values[4])
                verif = True
        except:
            messagebox.showerror("Erreur", "L'adresse mail est déjà utilisée !")

    if verif:
        reponse = messagebox.showinfo("Création du compte", "Le compte a été créé avec succès !")
        if reponse:
            page_accueil(fenetre, nom_entry, mdp_entry)

def validation_connexion(fenetre, email_entry, mdp_entry):
    email_format = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if email_entry.get() == "" or mdp_entry.get() == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs !") 

    elif not re.search(email_format, email_entry.get()):
        messagebox.showerror("Erreur", "L'adresse mail n'est pas valide !")

    elif mot_de_passe.verif_mdp(mdp_entry.get()) == "Mot de passe non valide":
        messagebox.showerror("Erreur", "Le mot de passe n'est pas valide !")
    
    else:
        try:
            mdp_utilisateur = utilisateur.lectureCondition_mdp(f'"email" = "{email_entry.get()}"')
            if mdp_utilisateur == mdp_entry.get():
                page_accueil(fenetre, email_entry, mdp_entry)
                
        except:
            messagebox.showerror("Erreur", "Saisie erronnée !")

def reset_mdp():
    # Fonction pour réinitialiser le mot de passe
    page_reset_mdp_mail = CTkToplevel(root)
    page_reset_mdp_mail.title("Réinitialisation du mot de passe")
    page_reset_mdp_mail.geometry("200x110+900+400")

    mail_label = CTkLabel(page_reset_mdp_mail, text="Adresse mail")
    mail_entry = CTkEntry(page_reset_mdp_mail, width=180)

    mail_label.grid(row = 0, column = 0, columnspan = 2) 
    mail_entry.grid(row = 1, column = 0, columnspan = 2, padx = 10)

    valid_mail = CTkButton(page_reset_mdp_mail, text="Valider", command= lambda: valid_mail_reset_mdp(mail_entry, page_reset_mdp_mail))
    valid_mail.grid(row = 2, column = 0, columnspan = 2, pady = 10)
    page_reset_mdp_mail.grab_set()

def toggle_password(mdp_entry, mdp_checkbox):
    if mdp_checkbox.get():
        mdp_entry.configure(show='')
    else:
        mdp_entry.configure(show='*')

def page_accueil(fenetre, nom_entry, mdp_entry):
    statut_mot_de_passe = mot_de_passe.verif_mdp(mdp_entry.get())
    if statut_mot_de_passe == "Mot de passe non valide":
        messagebox.showerror("Erreur", "Le mot de passe n'est pas valide !")
    else:
        if nom_entry.get() == "" or mdp_entry.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs !")
        else:
            fenetre.destroy()
            fenetre = CTkFrame(root)
            fenetre.pack()
            accueil_label = CTkLabel(fenetre, text="Accueil", font=("Arial", 20))
            accueil_label.pack()

def page_creation_compte(fenetre):
    fenetre.destroy()
    fenetre = CTkFrame(root)
    root.title("Création de compte")

    fenetre.place(relx=0.5, rely=0.5, anchor=CENTER)
    creation_compte_label = CTkLabel(fenetre, text="Création de compte")

    nom_label = CTkLabel(fenetre, text="Nom")
    nom_entry = CTkEntry(fenetre, width=180)

    prenom_label = CTkLabel(fenetre, text="Prénom")
    prenom_entry = CTkEntry(fenetre, width=180)

    email_label = CTkLabel(fenetre, text="Adresse mail")
    email_entry = CTkEntry(fenetre, width=180)

    age_label = CTkLabel(fenetre, text="Age")
    age_entry = CTkEntry(fenetre, width=30)

    mdp_label = CTkLabel(fenetre, text="Mot de passe")
    mdp_entry = CTkEntry(fenetre, width=180, validate = 'key', show="*")
    mdp_checkbox = BooleanVar()
    mdp_checkbox.set(False)
    mdp_checkbox_button = CTkCheckBox(fenetre, variable=mdp_checkbox, text= "Afficher le mot de passe", command= lambda *args: toggle_password(mdp_entry, mdp_checkbox))

    mdp2_label = CTkLabel(fenetre, text="Confirmer le mot de passe")
    mdp2_entry = CTkEntry(fenetre, width=180, validate = 'key', show="*")
    mdp2_checkbox = BooleanVar()
    mdp2_checkbox.set(False)
    mdp2_checkbox_button = CTkCheckBox(fenetre, variable=mdp2_checkbox, text="Afficher le mot de passe", command= lambda *args: toggle_password(mdp2_entry, mdp2_checkbox))

    pseudo_discord_label = CTkLabel(fenetre, text="Pseudo discord")
    pseudo_discord_entry = CTkEntry(fenetre, width=180)

    valid_creation_compte_button = CTkButton(fenetre, text="Valider", command= lambda: valid_creation_compte(fenetre, nom_entry, prenom_entry, email_entry, age_entry, mdp_entry, mdp2_entry, pseudo_discord_entry))

    creation_compte_label.grid(row=0, column=0, columnspan=2)
    nom_label.grid(row= 1, column=0)
    nom_entry.grid(row=2, column=0, padx=10)
    prenom_label.grid(row=1, column=1)
    prenom_entry.grid(row=2, column=1, padx=10)
    email_label.grid(row=3, column=0)
    email_entry.grid(row=4, column=0, padx=10)
    age_label.grid(row=3, column=1)
    age_entry.grid(row=4, column=1, padx=10)
    mdp_label.grid(row=5, column=0)
    mdp_entry.grid(row=6, column=0, padx=10)
    mdp_checkbox_button.grid(row=6, column=1)
    mdp2_label.grid(row=7, column=0)
    mdp2_entry.grid(row=8, column=0, padx=10)
    mdp2_checkbox_button.grid(row=8, column=1)
    pseudo_discord_label.grid(row=9, column=0)
    pseudo_discord_entry.grid(row=10, column=0, padx=10,)
    valid_creation_compte_button.grid(row=9, column=1, rowspan=2, pady=30)

# page authentification
def page_authentification(fenetre):
    authentification_label = CTkLabel(fenetre, text="Conexion")
    mail_label = CTkLabel(fenetre, text="Adresse mail")
    mail_entry = CTkEntry(fenetre, width=180)
    mdp_label = CTkLabel(fenetre, text="Mot de passe")
    mdp_entry = CTkEntry(fenetre, width=180, validate = 'key', show="*")
    mdp_checkbox = BooleanVar()
    mdp_checkbox.set(False)
    mdp_checkbox_button = CTkCheckBox(fenetre, text="Afficher le mot de passe", variable=mdp_checkbox, command=lambda *args: toggle_password(mdp_entry, mdp_checkbox))

    authentification_label.grid(row=0, column=0, columnspan=4, pady=5)
    mail_label.grid(row=1, column=0)
    mail_entry.grid(row=2, column=0, padx=20)
    mdp_label.grid(row=1, column=1)
    mdp_entry.grid(row=2, column=1, padx=20)
    mdp_checkbox_button.grid(row=2, column=2)

    authentification_button = CTkButton(fenetre, text="Valider", command=lambda: validation_connexion(fenetre, mail_entry, mdp_entry))
    authentification_button.grid(row=3, column=0, columnspan=4, pady=5)

    creation_compte_button = CTkButton(fenetre, text="Créer un compte", command=lambda: page_creation_compte(fenetre))
    creation_compte_button.grid(row=4, column=0, columnspan=4, pady=5)

    reinitialiser_mdp_label = CTkLabel(fenetre, text="Mot de passe oublié ? Cliquez ici.")
    reinitialiser_mdp_label.grid(row=5, column=0, columnspan=4, pady=5)

    reinitialiser_mdp_label.bind("<Button-1>", lambda e: reset_mdp())

page_authentification(fenetre)

root.mainloop()