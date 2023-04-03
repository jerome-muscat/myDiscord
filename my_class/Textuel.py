import mysql.connector
########################Tesxtuel################################
#-----------------tous se qui est écrit-------------------------#
################################################################
class Textuel:
    def __init__(self, hote, nom, bdd):
        self.hote = hote
        self.nom = nom
        self.bdd = bdd
###################connection/closing###########################
#------------------connection/closing--------------------------#
################################################################
    def connect(self):
        self.bd = mysql.connector.connect(
            host = self.hote,
            user = self.nom,
            database = self.bdd
        )
        self.cursor = self.bd.cursor()

    def close(self):
        self.cursor.close()
        self.bd.close()
###################CRUD###########################
#-----------------create-------------------------#
##################################################
    def ajout(self, nom):
        self.connect()
        ajout_req = f'insert into Textuel (nom) \
            \nvalues ("{nom}")'
       
        self.cursor.execute(ajout_req)
        self.bd.commit()
        self.close()
###################CRUD###########################
#------------------read--------------------------#
##################################################
    def lecture(self):
        self.connect()
        lecture_req = f"select * from textuel"
        self.cursor.execute(lecture_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat

    def lectureCondition(self, condition):
        self.connect()
        lecture_cond_req = f"select nom from textuel where {condition}"
        self.cursor.execute(lecture_cond_req)
        resultat = self.cursor.fetchall()
        self.close()
        return resultat
        
    def lectureCondition_id(self, condition):
        self.connect()
        lecture_cond_req = f'select id from textuel where nom = "{condition}"'
        self.cursor.execute(lecture_cond_req)
        resultat = self.cursor.fetchone()[0]
        print(resultat)
        self.close()
        return resultat
###################CRUD###########################
#-----------------up date------------------------#
##################################################
    def maj(self, champ, nouvelle_valeur, condition):
        self.connect()
        maj_req = f"update textuel set {champ} = {nouvelle_valeur} where {condition}"
        self.cursor.execute(maj_req)
        self.bd.commit()
        self.close()
###################CRUD###########################
#-----------------delete-------------------------#
##################################################
    def supr(self, condition):
        self.connect()
        supr_req = f"delete from textuel where {condition}"
        self.cursor.execute(supr_req)
        self.bd.commit()
        self.close()