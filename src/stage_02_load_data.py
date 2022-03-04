from src.utils.common import read_yaml
from src.stage_01_get_data import get_data
import argparse
import logging
import os

STAGE = "Load The Actual Data" ## <<< change stage name 

logging.basicConfig(
                    filename=os.path.join("logs", 'running_logs.log'), 
                    level=logging.INFO, 
                    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
                    filemode="a"
                    )

def load_and_save(config_path):
    config = read_yaml(config_path)
    data = get_data(config_path)

    data.drop(['Miscellaneous_Info'], axis=1, inplace=True)

    raw_data = config['load_data']['raw_data']

    data.to_csv(raw_data, sep=',', index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        load_and_save(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e