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
                    "INSERT INTO modality(id_modality, id_type, value, proba) VALUES "+
                    "(%(id_modality)s, %(id_type)s, %(value)s, %(proba)s)"
                    , {"id_modality" : modality.id_modality, "id_type" : modality.id_type,
                       "value" : modality.value, "proba" : modality.proba_apparition }
                )

    def find_modality(self, modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "select * from modality where id_modality = %(id)s "
                    , {"id" : modality.id_modality})
                res = cursor.fetchone()
                modality = ModalityFactory.get_modality_from_sql_query(res)
                return modality
    
    def update_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE modality "+
                    "SET type = %(type)s , value = %(value)s, proba = %(proba) " +
                    " where id = %(id)s",
                    {"type" : modality.id_type,"value": modality.value,"id":modality.id_modality}
                )
                
    def delete_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM modality "+
                    " where id = %(id)s",
                    {"id":modality.id_modality}
                )

if __name__ == "__main__":
    #Test find_all_modality
    #modality = ModalityDao().find_all_modality()
    #print(len(modality) == 5)
    #Test find_modality_by_id
    #mod1 = ModalityDao().find_modality_by_id(1)
    #print(mod1.nom_type, mod1.proba_apparition, mod1.value)
    #Test save_modality
    mod2 = Modality(nom_type = 2,
                    proba_apparition="NULL",
                    value = "Nathan")
    mod2.add_modality()
    print(mod2.id_modality)
    #ModalityDao().save_modality(mod2)
    