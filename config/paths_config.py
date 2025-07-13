import os

### DATA INGESTION ###

RAW_DIR = "artifacts/raw" ## storing the data in artifacts, in artifacts there should be a folder raw
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw.csv") ## it will get stored under raw directory with the file name "raw.csv"
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

#### WE ALSO NEED TO READ DATA FROM THE config.yaml, like bucket_name, bucket_file_name and so on, SO SPECIFYING CONFIG PATH ####

CONFIG_PATH = "config/config.yaml"


################ DATA PROCESSING ##############

PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_train.csv")
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_test.csv")


################ MODEL TRAINING ##############
MODEL_OUTPUT_PATH = "artifacts/model/lgbm_model.pkl"  # Path to save the trained model
