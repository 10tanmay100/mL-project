import yaml
import os,sys
from housing.exception import housing_exception


def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,'rb') as f:
            ans=yaml.safe_load(f)
            return ans
    except Exception as e:
        raise housing_exception(e,sys) from e