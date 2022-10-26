from tp3.business_object.utilisateur import Utilisateur


class UtilisateurFactory():
    """
        classe ayant pour role de gérer la conversion
        de donnees brutes en Utilisateur
    """
    @staticmethod
    def get_utilisateur_from_sql_query(res):
        user= Utilisateur(
                nom=res['nom']
                , prenom = res["prenom"]
        )
        user.id = int(res['id'])
        return user