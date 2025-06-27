import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

### writing the common function for reading the yaml file
def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in the given path")
        ## but if it is in the given path, it will open that file
        with open(file_path, "r") as yaml_file: ## 'r' read mode
            config = yaml.safe_load(yaml_file) ## load the content of YAML file, gets stored under config variable
            logger.info("Successfully read the YAML file")
            return config
    except Exception as e:
        logger.error("Error while reading the YAML file")
        raise CustomException("Failed to read YAML file", e) ## and whatever the exception 'e' it will get shown
    
            
