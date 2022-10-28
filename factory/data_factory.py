from business_object.regle_generation.generation_donnee import Generation_donnee


class DataFactory():
    """
        classe ayant pour role de gérer la conversion
        de donnees brutes en Type
    """
    @staticmethod
    def get_data_from_sql_query(res):
        dat = {'id_donnee' : res['id_donnee'], 
                'nom_meta' : res['nom_meta'], 
                'nom_type' : res['nom_type'], 
                'order' : res['order'], 
                'value' : res['value']}
        return dat