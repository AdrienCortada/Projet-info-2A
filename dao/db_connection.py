import os

<<<<<<< Updated upstream
import dotenv #import dotenv_values #ou import dotenv (en entier)
=======
import dotenv #ou from dotenv import dotenv_values 
>>>>>>> Stashed changes
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Classe technique permettant d'assurer une connecion unique à la base de données.
    """
    def __init__(self):
<<<<<<< Updated upstream
        dotenv.load_dotenv(override=True) #à modifier pour avoir un accès local ?
        #dotenv_values(".env.local") #à vérifier ?
=======
        #dotenv.load_dotenv(override=True) #à modifier pour avoir un accès local ?
        #dotenv_values(".env.local") #à vérifier ?
        dotenv.load_dotenv(override=True)
>>>>>>> Stashed changes
        # Ouvre la connection
        self.__connection =psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection

if __name__ == "__main__":
    with DBConnection().connection as conn:
<<<<<<< Updated upstream
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 as test")
                res = cursor.fetchone()
    print(1 == res["test"])
=======
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 as test")
            res = cursor.fetchone()
        print(1 == res["test"])
>>>>>>> Stashed changes
