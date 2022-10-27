from dao.db_connection import DBConnection
from unittest.case import TestCase
from dao.modality_dao import ModalityDao

class TestModalityDao(TestCase):

    def test_find_all_modality(self):
        #GIVEN
        modality_dao = ModalityDao()
        #WHEN
        mods = modality_dao.find_all_modality()
        #THEN
        self.assertEqual(first, second)
