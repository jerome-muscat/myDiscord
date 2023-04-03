import mysql.connector
########################Message################################
#----------------tous se qui a était écrit--------------------#
################################################################
class Utilisateur:
    def __init__(self, hote, utilisateur, motdepasse, bdd):
        self.hote = hote
        self.utilisateur = utilisateur
        self.motdepasse = motdepasse
        self.bdd = bdd
###################connection/closing###########################
#------------------connection/closing--------------------------#
################################################################
    def connect(self):
        self.bd = mysql.connector.connect(
            host = self.hote,
            user = self.utilisateur,
            password = self.motdepasse,
            database = self.bdd
        )
        self.cursor = self.bd.cursor()

    def close(self):
        self.cursor.close()
        self.bd.close()
###################CRUD###########################
#-----------------create-------------------------#
##################################################
    def ajout(self, nom, prenom, email, motdepasse, pseudo_discord, age):
        self.connect()
        ajout_req = f'insert into utilisateur (nom, prenom, email, mdp, pseudo, age, id_privilege) \
            \nvalues ("{nom}", "{prenom}", "{email}", "{motdepasse}", "{pseudo_discord}", {age}, 3)'
       
        self.cursor.execute(ajout_req)

        self.bd.commit()
        self.close()
###################CRUD###########################
#------------------read--------------------------#
##################################################
    def lecture(self):
        self.connect()
        lecture_req = f"select * from utilisateur"
        self.cursor.execute(lecture_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat

    def lectureCondition(self, condition):
        self.connect()
        lecture_cond_req = f"select * from utilisateur where {condition}"
        self.cursor.execute(lecture_cond_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat

    def lectureCondition_mdp(self, condition):
        self.connect()
        lecture_cond_req = f'select mdp from utilisateur where {condition}"'
        self.cursor.execute(lecture_cond_req)
        resultat = self.cursor.fetchone()[0]
        print(resultat)
        self.close()
        return resultat

    def maj(self, champ, nouvelle_valeur, condition):
        self.connect()
        maj_req = f"update utilisateur set {nouvelle_valeur} where {condition}"
        self.cursor.execute(maj_req)
        self.bd.commit()
        self.close()

    def supr(self, condition):
        self.connect()
        supr_req = f"delete from utilisateur where {condition}"
        self.cursor.execute(supr_req)
        self.bd.commit()
        self.close()
    
    def verif_email(self, email):
        self.connect()
        req = f'select * from utilisateur where "email" = "{email}"'
        self.cursor.execute(req)
        result = self.cursor.fetchone()
        if result != None:
            return False
        else:
            return True
        self.close()