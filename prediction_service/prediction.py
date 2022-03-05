from src.utils.common import read_yaml
import numpy as np
import joblib
import json
import yaml
import os

params_path = "params.yaml"

def load_model(params_path):
    config = read_yaml(params_path)

    model_dir_path = config["webapp_model_dir"]["model"]

    model = joblib.load(model_dir_path)
    
    return model
   