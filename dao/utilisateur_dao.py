from tp3.business_object.utilisateur import Utilisateur
from tp3.dao.db_connection import DBConnection
from tp3.factory.utilisateur_factory import UtilisateurFactory

class UtilisateurDao:
    """
        classe ayant pour role de gérer les comportements
        relatifs a la récupération de données en bdd
    """

    def find_all_users(self):
        users=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * from utilisateur"
                )
                res = cursor.fetchall()
                for row in res:
                    user = UtilisateurFactory.get_utilisateur_from_sql_query(row)
                    users.append(user)
        return users

    def save_user(self,user:Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "insert into utilisateur(nom,prenom) VALUES (%(nom)s,%(prenom)s)"
                , {"nom" : user.nom,"prenom":user.prenom})

    def find_user(self,user:Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "select * from utilisateur where nom=%(nom)s and prenom=%(prenom)s limit 1"
                    , {"nom" : user.nom,"prenom":user.prenom})
                res = cursor.fetchone()
                user = UtilisateurFactory.get_utilisateur_from_sql_query(res)
                return user
    def update_user(self,user:Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE utilisateur "+
                    "SET nom = %(nom)s , prenom = %(prenom)s " +
                    " where id = %(id)s",
                    {"nom" : user.nom,"prenom":user.prenom,"id":user.id}
                )
                
    def delete_user(self,user:Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM utilisateur "+
                    " where id = %(id)s",
                    {"id":user.id}
                )
