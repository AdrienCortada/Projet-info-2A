from business_object.regle_generation.typ import Type
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from factory.typ_factory import TypeFactory

class TypeDao:
    """
        classe ayant pour role de gérer les comportements
        relatifs à la récupération de données en bdd
    """    
    def find_all_type(self):
        typs=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * from Type"
                )
                res = cursor.fetchall()
                for row in res: 
                    typ = TypeFactory.get_type_from_sql_query(row)
                    typs.append(typ)
        return typs
    
    def find_type_by_id(self, id : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                   "SELECT * FROM modality WHERE id_modality = %(id)s LIMIT 1"
                   , { "id" : id}
                )
                res = cursor.fetchone()
                typ = ModalityFactory.get_type_from_sql_query(res)
                return typ

    def save_type(self,type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO Type(id_type, tx_remplissage, nom) VALUES "+
                    "(%(tx_remplissage)s, %(nom)s)"
                    , {"tx_remplissage" : type.tx_remplissage, 
                       "nom" : type.nom}
                )

    def find_type(self, type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM Type WHERE nom = %(nom_type)s AND tx_remplissage = %(tx_remplissage)s"
                    , {"nom_type" : type.nom,
                        "tx_remplissage": type.tx_remplissage}
                        )
                res = cursor.fetchone()
                typ = TypeFactory.get_type_from_sql_query(res)
                return typ
    
    def update_type_by_id(self, id : int, new_type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE Type "+
                    "SET tx_remplissage = %(tx_remplissage)s, nom = %(nom)s " +
                    " where id_type = %(id_type)s",
                    {"id_type" : id,"tx_remplissage": new_type.tx_remplissage, "nom" : new_type.nom}
                )
                
    def delete_type(self,type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM Type "+
                    " WHERE id_type IN ("+
                    "SELECT id_type FROM Type "+
                    "WHERE nom = %(nom)s AND tx_remplissage = %(tx_remplissage)s" +
                    "LIMIT 1 )",
                    {"nom":type.nom, 
                    "tx_remplissage" : type.tx_remplissage}
                )

    def delete_type_by_id(self,id_type:int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM Type "+
                    " where id_type = %(id)s",
                    {"id":id_type}
                )
