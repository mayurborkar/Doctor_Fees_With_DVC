from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from src.utils.common import read_yaml, create_directories
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import argparse
import logging
import json
import joblib
import os

STAGE = "Train & Evaluate" ## <<< change stage name 

logging.basicConfig(
                    filename=os.path.join("logs", 'running_logs.log'), 
                    level=logging.INFO, 
                    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
                    filemode="a"
                    )

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train_and_evaluate(config_path):
    ## read config files
    config = read_yaml(config_path)

    logging.info(f'Loading The Train & Test')
    train_data = config['split_data']['train_data']
    test_data = config['split_data']['test_data']

    logging.info(f'Logging The Random State Parameter')
    random_state = config['split_data']['random_state']

    model_dir = config["model_dir"]

    logging.info(f'Logging The Random Forest Parameter')
    min_samples_split = config["estimators"]["RandomForestRegressor"]["params"]["min_samples_split"]
    min_samples_leaf = config["estimators"]["RandomForestRegressor"]["params"]["min_samples_leaf"]
    n_estimators = config["estimators"]["RandomForestRegressor"]["params"]["n_estimators"]
    max_depth = config["estimators"]["RandomForestRegressor"]["params"]["max_depth"]
   
    logging.info(f'Defining The Target Column In Config')
    target_col = [config["base"]["target_col"]]

    logging.info(f'Loading The Train & Test')
    train = pd.read_csv(train_data, sep=",")
    test = pd.read_csv(test_data, sep=",")

    logging.info(f'Defining The Target Column In Train & Test')
    train_y = train[target_col]
    test_y = test[target_col]

    logging.info(f'Drop The Target Column From Train & Test')
    train_x = train.drop(target_col, axis=1)
    test_x = test.drop(target_col, axis=1)

    # print(test_x.columns)
    logging.info(f'Create The Model')
    rfr = RandomForestRegressor(min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, 
                                max_features='sqrt', n_estimators= n_estimators, bootstrap=True)

    rfr.fit(train_x, train_y)

    predicted_qualities = rfr.predict(test_x)

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("RMSE For Heating Load: %s" % rmse)
    print("MAE For Heating Load: %s" % mae)
    print("R2 Score For Heating Load: %s" % r2)

    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    logging.info(f'Store The Score & Parameter Value In The Json Format In Report Folder')
    with open(scores_file, "w") as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2,
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        scores = {
            "max_depth": max_depth,
            "min_samples_split": min_samples_split,
            "min_samples_leaf":min_samples_leaf,
            "n_estimators": n_estimators
        }
        json.dump(scores, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "model.joblib")

    logging.info(f'Save The Model In model_dir')
    joblib.dump(rfr, model_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        train_and_evaluate(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e