from business_object.regle_generation.typ import Type
from dao.db_connection import DBConnection
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
                    "(%(id_type)s, %(tx_remplissage)s, %(nom)s)"
                    , {"id_type" : type.id_type,
                       "tx_remplissage" : type.value, "nom" : type.proba}
                )

    def find_type(self, type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM Type WHERE id_type = %(id)s LIMIT 1"
                    , {"id" : type.id_type})
                res = cursor.fetchone()
                typ = TypeFactory.get_type_from_sql_query(res)
                return typ
    
    def update_type(self, type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE Type "+
                    "SET id_type = %(id_type)s , tx_remplissage = %(tx_remplissage)s, nom = %(nom) " +
                    " where id = %(id)s",
                    {"id_type" : type.id_type,"tx_remplissage": type.tx_remplissage, "nom" : type.nom, "id":type.id}
                )
                
    def delete_type(self,type:Type):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM modality "+
                    " where id = %(id)s",
                    {"id":modality.id_modality}
                )

    def delete_type_by_id(self,id_type:int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM modality "+
                    " where id = %(id)s",
                    {"id":modality.id_type}
                )
