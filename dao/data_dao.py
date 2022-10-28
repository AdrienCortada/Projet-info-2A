from business_object.generation_donnee import Generation_donnee
from business_object.regle_generation.meta_type import Meta_type
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from factory.data_factory import DataFactory

class DataDao : 
    
    def find_all_data(self):
        data=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM Donnee"
                )
                res = cursor.fetchall()
                for row in res:
                    dat = DataFactory.get_data_from_sql_query(row)
                    data.append(dat)
        return data
    
    def save_data(self, data : Generation_donnee):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for key in data.jeu_donnee.keys() : 
                    for i,tip in enumerate(data.meta_type.list_type) :
                        cursor.execute(
                            "INSERT INTO Donnee(nom_meta, nom_type, order, value)"+ 
                            "VALUES ( %(nom_meta)s, %(nom_type)s, %(order)s, %(value)s)"
                        , {"nom_meta" : data.meta_type.nom,
                            "nom_type":tip,
                            "order" : i+1,
                            "value" : data.jeu_donnee[key][tip]})

    def find_data_by_id(self, id_donnee):
        data=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM Donnee WHERE id_donnee=%(id_donnee)s "
                    , {"id_donnee" : id_donnee})
                res = cursor.fetchall()
                for row in res:
                    dat = DataFactory.get_data_from_sql_query(row)
                    data.append(dat)
        return user

    def find_data_by_meta(self, nom_meta : str):
        data=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM Donnee WHERE nom_meta=%(nom_meta)s "
                    , {"nom_meta" : nom_meta})
                res = cursor.fetchall()
                for row in res:
                    dat = DataFactory.get_data_from_sql_query(row)
                    data.append(dat)
        return user

    