from src.utils.common import read_yaml
from src.stage_01_get_data import get_data
import pandas as pd
import numpy as np
import argparse
import logging
import random
import shutil
import os
import re

STAGE = "Preprocess Data" ## <<< change stage name 

logging.basicConfig(filename=os.path.join("logs", 'running_logs.log'), 
                    level=logging.INFO, 
                    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
                    filemode="a")


def main(config_path):
    ## read config files
    config = read_yaml(config_path)

    raw_data_path = config['load_data']['raw_data']
    data = pd.read_csv(raw_data_path)


    ############# Handle The Experience Column #############
    data['Experience'] = data['Experience'].str.split().str[0]
    data['Experience'] = data['Experience'].astype(int)
    # print(data['Experience'].head())


    ############# Handle The Rating Column #############
    data['Rating'].fillna(-1, inplace=True)
    data['Rating']=data['Rating'].apply(lambda x: str(x).replace('%','')).astype(int)
    
    bins = [-1,0,10,20,30,40,50,60,70,80,90,100]
    labels = [i for i in range (11)]
    data['Rating'] = pd.cut(data['Rating'], bins=bins, labels=labels, include_lowest=True)
    # print(data['Rating'].head())


    ############# Handle The Place Column #############
    data['Place'].fillna('Unknown,Unknown',inplace=True)

    data['Locality'] = data['Place'].str.split(",").str[0]
    data['City']    = data['Place'].str.split(",").str[1]
    data.drop(['Place', 'Locality'],axis=1,inplace=True)

    data['City'] = data['City'].apply (lambda x: re.sub(' +','',str(x)))


    ############# Handle The Qualification Column #############
    data['Qualification'] = data['Qualification'].str.split(",")
    Qualification = {}

    for x in data['Qualification'].values:
        for qual in x:
            qual = qual.strip()
            if qual in Qualification:
                Qualification[qual] += 1
            else:
                Qualification[qual] = 1
    #print(Qualification)

    most_qual = sorted(Qualification.items(), key=lambda x: x[1], reverse=True)[:10]
    final_qual = []
    for qual in most_qual:
        final_qual.append(qual[0])
    #print(final_qual)

    for qual in final_qual:
        data[qual] = 0
    for x,y in zip(data['Qualification'].values, np.array([i for i in range(len(data))])):
        for c in x:
            c = c.strip()
            if c in final_qual:
                data[c][y] = 1
    #print(data.head())
    data.drop(['Qualification'], axis=1, inplace=True)


    ############# Rename The Qualification Dummy Column #############
    data.rename(columns={
        'MD - Dermatology':'MD_Dermatology','MS - ENT':'MS_ENT','Venereology & Leprosy':'Venereology_Leprosy',
        'MD - General Medicine':'MD_General_Medicine','MD - Homeopathy':'MD_Homeopathy',
        'Diploma in Otorhinolaryngology (DLO)':'Diploma_in_Otorhinolaryngology',
        'Profile_ENT Specialist':'Profile_ENT_Specialist','Profile_General Medicine':'Profile_General_Medicine'},
         inplace=True)


    ############# Create The Dummy of Some Column #############
    data = pd.get_dummies(data, columns=['City','Profile'], prefix=['City','Profile'])


    ############# Saving The Processed Data #############
    processed_data = config['load_data']['processed_data']
    data.to_csv(processed_data, sep=',', index=False)


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