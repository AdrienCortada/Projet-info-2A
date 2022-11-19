from business_object.generation_donnee import Generation_donnee
from business_object.regle_generation.meta_type import Meta_type
from business_object.regle_generation.typ import Type
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from factory.meta_factory import MetaFactory

class MetaDao : 
    
    def find_all_meta(self):
        metas=[]
        liste_metas = []
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM meta_type"
                )
                res = cursor.fetchall()
                print('sortie python avec le cursor.fetchall() : ', res)
                for row in res:
                    if row['nom_meta_type'] not in metas:
                        metas.append(row['nom_meta_type'])
        print('liste des nom_métatypes : ', metas)
        for nom_meta in metas:
            meta = MetaFactory().get_meta_type_from_sql_query(res, nom_meta)
            print(meta.nom, meta.list_type)
            liste_metas.append(meta)
        print('liste des objets métier :', liste_metas)
        return liste_metas
    
    def save_meta(self, meta : Meta_type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for tip in meta.list_type :
                    cursor.execute(
                        "INSERT INTO meta_type(nom_meta_type, nom_type) "+ 
                        "VALUES ( %(nom_meta_type)s, %(nom_type)s) "
                    , {"nom_meta_type" : meta.nom,
                        "nom_type":tip})

    def find_ids_meta(self, nom_meta : str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                ids =[]
                cursor.execute(
                    "SELECT * FROM meta_type "+
                    "WHERE nom_meta_type = %(nom_meta_type)s ",
                    {"nom_meta_type" : nom_meta}                    
                )
                res = cursor.fetchall()
                for row in res:
                    ids.append(row['id_meta_type'])
        return ids

    def add_type_to_meta(self, 
                         nom_meta_type : str,
                         nom_type : str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO meta_type(nom_meta_type, nom_type) VALUES "+
                    "(%(nom_meta_type)s, %(nom_type)s)",
                    {"nom_meta_type" : nom_meta_type,
                     "nom_type" : nom_type}
                )    

    def delete_meta_by_name(self, nom_meta_type : str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM meta_type "+
                    "WHERE nom_meta_type = %(nom_meta_type)s",
                    {"nom_meta_type" : nom_meta_type}
                )    

    #QUE VEUT-ON POUVOIR FAIRE EXACTEMENT ???
        
    #def find_meta_by_id(self, id_meta : int):
    #    meta_t=[]
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            cursor.execute(
    #                "SELECT * FROM meta_type WHERE id_meta=%(id_meta)s "
    #                , {"id_meta" : id_meta})
    #            res = cursor.fetchall()
    #            for row in res:
    #                mt = MetaFactory.get_meta_from_sql_query(row)
    #                meta_t.append(mt)
    #    return meta_t

    #def find_meta_by_name(self, nom_meta : str):
    #    meta_t=[]
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            cursor.execute(
    #                "SELECT * FROM meta_type "+
    #                "WHERE nom_meta_type=%(nom_meta)s "
    #                , {"nom_meta" : nom_meta})
    #            res = cursor.fetchall()
    #            for row in res:
    #                mt = MetaFactory.get_meta_from_sql_query(row)
    #                meta_t.append(mt)
    #    return meta_t
#
    #def update_meta_by_id(self, id : int, new_meta : list):
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            cursor.execute(
    #                "UPDATE meta_type "+
    #                "SET nom_meta_type = %(nom_meta)s, nom_type = %(nom_type)s " +
    #                "WHERE id_meta_type = %(id_meta)s",
    #                {"nom_meta" :new_meta[0],
    #                "nom_type": new_meta[1]}
    #            )
    #
    #def update_meta(self, Meta0 : Meta_type, new_meta : Meta_type):  ### Il remplace les n premiers types du meta type avec n la longueur de list_type de new_meta
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            for i,tip in enumerate(new_meta.list_type):
    #                cursor.execute(
    #                    "UPDATE meta_type "+
    #                    "SET nom_meta_type = %(nom_meta)s, nom_type = %(nom_type)s " +
    #                    "WHERE nom_meta_type = %(nom_m)s AND nom_type = %(type)s ", 
    #                    {"nom_meta" :new_meta.nom,
    #                    "nom_type": tip,     
    #                    "nom_m" : Meta0.nom,
    #                    "type" : Meta0.list_type[i]}
    #                )
    #
    #def delete_meta(self, ligne : list):
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            cursor.execute(
    #                "DELETE FROM meta_type "+
    #                "WHERE id_meta_type IN ( "+
    #                "SELECT id_meta_type FROM meta_type "+
    #                "WHERE nom_meta_type = %(nom_meta_type)s AND nom_type = %(nom_type)s" +
    #                "LIMIT 1 )",
    #                {"nom_meta_type" : ligne[0],
    #                "nom_type": ligne[1]}
    #            )
#
    #def delete_meta_by_id(self, id : int):
    #    with DBConnection().connection as connection:
    #        with connection.cursor() as cursor :
    #            cursor.execute(
    #                "DELETE FROM meta_type "+
    #                "WHERE id_meta_type = %(id)s",
    #                {"id" : id}
    #            )
    #
#



if __name__ == '__main__':
    print('Tests de la classe MetaDao')
    #metas = MetaDao().find_all_meta()
    #print(len(metas) == 2)

    #Test de "save_meta"
    #meta1 = Meta_type(
    #    nom = 'meta_test',
    #    list_type = ['prénom', 'code postal'])
    #MetaDao().save_meta(meta1)

    #Test de find_ids_meta
    #ids = MetaDao().find_ids_meta(nom_meta = 'meta_test')
    #print(ids)

    #Test de add_type_to_meta
    #MetaDao().add_type_to_meta(nom_meta_type = 'meta_test',
    #                           nom_type = 'nom commune')

    #Test de delete_meta_by_name
    MetaDao().delete_meta_by_name('meta_test')
    
