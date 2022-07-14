from collections import namedtuple
from unicodedata import name


#DataIngestionConfig
DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir",
"ingested_train_dir","ingsted_test_dir"])


#DataValidationConfig
DataValidationConfig=namedtuple("DataValidationConfig",["schema_path"])


#DataTransformationConfig
DataTransformationConfig=namedtuple("DataTransformationConfig",
["add_bedroom_per_room","transformed_train_dir","transformed_test_dir",
"preprocessed_object_file_path"])


#ModelTrainerConfig
ModelTrainerConfig=namedtuple("ModelTrainerConfig",
["trained_model_file_path","base_accuracy"])

#ModelPusherConfig
ModelPusherConfig=namedtuple("ModelPusherConfig",["export_dir_path"])



