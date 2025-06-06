import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.proj1_data import Proj1Data


class DataIngestion:
    def __init__(self,data_ingestion_config=DataIngestionConfig()):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise MyException(e,sys)
        

    def export_data_into_feature_store(self)->pd.DataFrame:
        try:
            logging.info(f"exporting data from mongodb")
            my_data=Proj1Data
            dataframe=my_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)

            logging.info(f'shape of dataframe {dataframe.shape}')
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"saving exported data into feature store file:{feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False)
            return dataframe
        except Exception as e:
            raise MyException(e,sys)
        
    
    def split_data_as_train_test(self,dataframe:pd.DataFrame)->None:
        logging.info("entered split_data_as reain_ test")

        try:
            dataframe=self.export_data_into_feature_store()
            logging.info('got the dataset from mongodb')
            self.split_data_as_train_test(dataframe)
            logging.info('performed train test split on dataset')
            data_ingestion_artifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=
                                                          self.data_ingestion_config.testing_file_path)
            
        except Exception as e:
            raise MyException(e,sys)

            
