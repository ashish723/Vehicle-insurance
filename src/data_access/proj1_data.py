import os
import sys
import pandas as pd
import numpy as np
import typing as  Optional


from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException


class Proj1Data:

    def __init__(self)->None:
        try:
            self.mongo_client=MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)
        
    def export_collection_as_dataframe(self,collection_name:str,database_name :Optional[str]=None)->pd.DataFrame:
        try:
            if database_name is None:
                collection=self.mongo_client.database[collection_name]
            else :
                collection=self.mongo_client[database_name][collection_name]

            print('fetching data from mongodb client')

            df=pd.DataFrame(list(collection.find()))
            print('data fetched from database')


            if 'id' in df.columns.to_list():
                df.drop('id',axis=1,inplace=True)
            df.replace({'na':np.nan},inplace=True)

            return df
        
        except Exception as e:
            raise MyException(e,sys)