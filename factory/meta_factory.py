from business_object.regle_generation.meta_type import Meta_type


class MetaFactory():
    """
        classe ayant pour role de gérer la conversion
        de donnees brutes en Meta_type
    """
    @staticmethod
    def get_meta_from_sql_query(res):
        mt = Meta_type(
            nom= res['nom_meta_type'],
            list_type= [res['nom_type']])
        return mt