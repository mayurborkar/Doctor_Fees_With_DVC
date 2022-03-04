from sklearn.model_selection import train_test_split
from src.utils.common import read_yaml
import pandas as pd
import argparse
import logging
import os

STAGE = "Split Data" ## <<< change stage name 

logging.basicConfig(
                    filename=os.path.join("logs", 'running_logs.log'), 
                    level=logging.INFO, 
                    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
                    filemode="a"
                    )


def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    logging.info(f'Loading The Raw Data')

    logging.info(f'Setting All The Path For Loading The Data & Split Up Into train, test')

    processed_data = config['load_data']['processed_data']
    train_data = config['split_data']['train_data']
    test_data = config['split_data']['test_data']

    logging.info(f'Setting The Split Ratio & Random State')

    split_ratio = config['split_data']['split_ratio']
    random_state = config['split_data']['random_state']

    logging.info(f'Reading The Data Set & Split Up Into Train & Test')

    data = pd.read_csv(processed_data, sep=',')
    train, test = train_test_split(data, test_size=split_ratio, random_state=random_state)

    logging.info(f'Setting Up The Path of Train & Test Data')

    train.to_csv(train_data, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data, sep=",", index=False, encoding="utf-8")



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e