from business_object.regle_generation.modality import Modality


class ModalityFactory():
    """
        classe ayant pour role de gérer la conversion
        de donnees brutes en Modality
    """
    @staticmethod
    def get_modality_from_sql_query(res):
        mod = Modality(
            nom_type = res['id_type'],
            proba_apparition = res['proba'],
            value= res['value'] )
        mod.id = int(res['id_modality'])
        return mod