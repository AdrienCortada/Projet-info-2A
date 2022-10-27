from business_object.regle_generation.modality import Modality
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from factory.modality_factory import ModalityFactory

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
                modality = ModalityFactory().get_modality_from_sql_query(res)
                return modality

    def save_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO modality(id_modality, id_type, value, proba) VALUES "+
                    "(%(id_modality)s, %(id_type)s, %(value)s, %(proba)s)"
                    , {"id_modality" : modality.id_modality, "id_type" : modality.id_type,
                       "value" : modality.value, "proba" : modality.proba }
                )

    def find_modality(self, modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "select * from modality where id_modality = %(id)s "
                    , {"id" : modality.id_modality})
                res = cursor.fetchone()
                modality = ModalityFactory().get_modality_from_sql_query(res)
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
    #modality_dao = ModalityDao()
    #mods = modality_dao.find_all_modality()
    #print(5 == len(mods))