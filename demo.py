from housing.exception import housing_exception
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import configuration
import os,sys
def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise housing_exception(e,sys) from e
    # data_transformation_info=configuration().get_data_transformation_config()
    # print(data_transformation_info)


if __name__=="__main__":
    main()   