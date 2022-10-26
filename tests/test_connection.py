from dao.db_connection import DBConnection
from unittest.case import TestCase

class TestConnection(TestCase):

    def test_connection(self):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 as test")
                res = cursor.fetchone()
        self.assertEqual(1,res["test"])