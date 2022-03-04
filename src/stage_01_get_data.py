from src.utils.common import read_yaml
import pandas as pd
import argparse
import logging
import yaml
import os

STAGE = "Get Actual Data" ## <<< change stage name 

logging.basicConfig(
                    filename=os.path.join("logs", 'running_logs.log'), 
                    level=logging.INFO, 
                    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
                    filemode="a"
                    )


def get_data(config_path):
    config = read_yaml(config_path)
    data = config['data_source']['source']
    data = pd.read_excel(data)
    #print(data.head())
    return data
    


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        get_data(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e