
from housing.config.configuration import configuration
from housing.logger import logging
from housing.exception import housing_exception
from housing.component.data_ingestion import DataIngestion
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig

import os,sys

class Pipeline:

    def __init__(self,config:configuration=configuration()) -> None:
        try:
            self.config=config
        except Exception as e:
            raise housing_exception(e,sys) from e
    
    def start_data_ingestion(self) ->DataIngestionArtifact:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise housing_exception(e,sys) from e


    def run_pipeline(self):
        try:
            #data ingestion
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise housing_exception(e,sys) from e
    









