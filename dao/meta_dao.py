from business_object.generation_donnee import Generation_donnee
from business_object.regle_generation.meta_type import Meta_type
from business_object.regle_generation.typ import Type
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from factory.data_factory import DataFactory

class MetaDao : 
    
    def find_all_meta(self):
        metas=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM metatype"
                )
                res = cursor.fetchall()
                for row in res.keys:
                    metas.append(res[row])
        return metas
    
    def save_meta(self, meta : Meta_type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for tip in meta.list_type :
                    cursor.execute(
                        "INSERT INTO metatype(nom_meta_type, nom_type)"+ 
                        "VALUES ( %(nom_meta_type)s, %(nom_type)s)"
                    , {"nom_meta_type" : meta.nom,
                        "nom_type":tip})

    def find_meta_by_id(self, id_meta : int):
        meta_t=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM metatype WHERE id_meta=%(id_meta)s "
                    , {"id_meta" : id_meta})
                res = cursor.fetchall()
                for row in res.keys:
                    meta_t.append(res[row])
        return meta_t

    def find_meta_by_nom(self, nom_meta : str):
        data=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM metatype WHERE nom_meta_type=%(nom_meta)s "
                    , {"nom_meta" : nom_meta})
                res = cursor.fetchall()
                for row in res.keys:
                    meta_t.append(res[row])
        return data

    def update_meta_by_id(self, id : int, new_meta : list):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE metatype "+
                    "SET nom_meta_type = %(nom_meta)s, nom_type = %(nom_type)s " +
                    "WHERE id_meta_type = %(id_meta)s",
                    {"nom_meta" :new_meta[0],
                    "nom_type": new_meta[1]}
                )
    
    def update_meta(self, Meta0 : Meta_type, new_meta : Meta_type):  ### Il remplace les n premiers types du meta type avec n la longueur de list_type de new_meta
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for i,tip in enumerate(new_meta.list_type):
                    cursor.execute(
                        "UPDATE metatype "+
                        "SET nom_meta_type = %(nom_meta)s, nom_type = %(nom_type)s " +
                        "WHERE nom_meta_type = %(nom_m)s AND nom_type = %(type)s ", 
                        {"nom_meta" :new_meta.nom,
                        "nom_type": tip,     
                        "nom_m" : Meta0.nom,
                        "type" : Meta0.list_type[i]}
                    )
    
    def delete_meta(self, ligne : list):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM metatype "+
                    "WHERE id_meta_type IN ( "+
                    "SELECT id_meta_type FROM metatype "+
                    "WHERE nom_meta_type = %(nom_meta_type)s AND nom_type = %(nom_type)s" +
                    "LIMIT 1 )",
                    {"nom_meta_type" : ligne[0],
                    "nom_type": ligne[1]}
                )

    def delete_meta_by_id(self, id : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM metatype "+
                    "WHERE id_meta_type = %(id)s",
                    {"id" : id}
                )
    
    def find_id_meta(self, ligne:list):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_meta_type FROM metatype "+
                    "WHERE nom_meta_type = %(nom_meta_type)s AND nom_type = %(nom_type)s",
                    {"nom_meta_type" : ligne[0],
                    "nom_type": ligne[1]}                    
                )
                res = cursor.fetchall()
                return res.values()


    