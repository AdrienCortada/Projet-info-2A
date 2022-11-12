from utils.singleton import Singleton
from dao.db_connection import DBConnection

#remplacer Objet par un objet métier
class ObjetDao(metaclass = Singleton):

    def fonction_type(self): #remplacer fonction par le nom de la méthode
        request = "" #requête SQL

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    request
                )
                res = cursor.fetchall() #ou fetchone ou...?
    #Les données sont stockées dans res, après il faut du code pour construire l'objet python correspondant
