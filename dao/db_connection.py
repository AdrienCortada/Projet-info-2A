import os

from dotenv import dotenv_values #ou import dotenv (en entier)
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton

config = dotenv_values(".env.local") #Je ne sais pas si ça se met ici

class DBConnection(metaclass=Singleton):
    """
    Classe technique permettant d'assurer une connecion unique à la base de données.
    """
    def __init__(self):
        dotenv.load_dotenv(override=True) #à modifier pour avoir un accès local ?
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