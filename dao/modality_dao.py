from business_object.regle_generation.modality import Modality
from dao.db_connection import DBConnection
from factory.modality_factory import ModalityFactory
from utils.singleton import Singleton

class ModalityDao(metaclass=Singleton):
    """
        classe ayant pour role de gérer les comportements
        relatifs a la récupération de données en bdd
    """

    def find_all_modality(self):
        mods=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * from modality"
                )
                res = cursor.fetchall()
                for row in res: 
                    mod = ModalityFactory().get_modality_from_sql_query(row)
                    mods.append(mod)
        return mods
    
    def find_modality_by_id(self, id : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                   "SELECT * FROM modality WHERE id_modality = %(id)s"
                   , { "id" : id}
                )
                res = cursor.fetchone()
                modality = ModalityFactory.get_modality_from_sql_query(res)
                return modality

    def save_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO modality(nom_type, value, proba_apparition) VALUES "+
                    "(%(nom_type)s, %(value)s, %(proba)s)"
                    , {"nom_type" : modality.nom_type,
                       "value" : modality.value, 
                       "proba" : modality.proba_apparition }
                )

    def find_modality(self, modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "select * from modality where nom_type = %(nom)s AND value = %(value)s "
                    , {"nom" : modality.nom_type,
                       "value" : modality.value}
                    )
                res = cursor.fetchone()
                modality = ModalityFactory.get_modality_from_sql_query(res)
                return modality
    
    #à revoir : (qui modifie-t-on ? modalité dans la base de donnée ? )
    def update_modality_by_id(self, id : int, new_type : str, new_value : str, new_proba_apparition : float):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE modality " +
                    "SET nom_type = %(type)s, value = %(value)s, proba_apparition = %(proba)s " +
                    "WHERE id_modality = %(id)s",
                    {"type" : new_type,
                     "value" : new_value,
                     "proba" : new_proba_apparition,
                     "id" : id}
                )
    #def update_modality(self,modality:Modality):
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            cursor.execute(
    #                "UPDATE modality "+
    #                "SET nom_type = %(type)s , value = %(value)s, proba_apparition = %(proba)s " +
    #                " where id = %(id)s",
    #                {"type" : modality.nom_type,
    #                 "value": modality.value,
    #                 "id":modality.id_modality}
    #            )
            
    def delete_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM modality "+
                    "WHERE nom_type = %(nom)s AND value = %(value)s "
                    , {"nom" : modality.nom_type,
                       "value" : modality.value}
                )

if __name__ == "__main__":
    #Test find_all_modality
    #modality = ModalityDao().find_all_modality()
    #print(len(modality) == 5)

    #Test find_modality_by_id
    #mod1 = ModalityDao().find_modality_by_id(3)
    #print(mod1.nom_type, mod1.proba_apparition, mod1.value)

    #Test save_modality
    #mod2 = Modality(nom_type = 'prénom',
    #                proba_apparition=0,
    #                value = "Nathan")
    #ModalityDao().save_modality(mod2)

    #Test find_modality
    #mod3 = ModalityDao().find_modality(mod2)
    #print(mod3.nom_type, mod3.proba_apparition, mod3.value)

    #Test update_modality
    ModalityDao().update_modality_by_id(id=5, new_type = 'prénom', new_value = 'Nathan', new_proba_apparition = 0) 

    #Test delete_modality
    #ModalityDao().delete_modality(mod2)
    
    