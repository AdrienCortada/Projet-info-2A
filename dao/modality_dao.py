from business_object.regle_generation.modality import Modality
from dao.db_connection import DBConnection
from factory.modality_factory import ModalityFactory

class ModalityDao:
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
                    mod = ModalityFactory.get_modality_from_sql_query(row)
                    mods.append(mod)
        return mods

    def save_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO modality(id_modality, id_type, value, proba) VALUES "+
                    "(%(id_modality)s, %(id_type)s, %(value)s, %(proba))"
                    , {"id_modality" : modality.id_modality, "id_type" : modality.id_type,
                       "value" : modality.value}
                )


    def find_modality(self,modality:Modality):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "select * from modality where value = %(nom)s "
                    , {"nom" : modality.value})
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
