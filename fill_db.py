import os
import re
import string
import time
import pandas as pd
from create_db import *


def read_seed():
    dataframe = pd.read_csv("./data/wendland.csv", encoding ='latin1')

    for index, row in dataframe.iterrows():
        historian_id = row['historian_id']
        name = row['name']
        date_born = row['date_born']
        place_born = row['place_born']
        date_died = row['date_died']
        place_died = row['place_died']
        overview = row['overview']
        home_country = row['home_country']
        sources = row['sources']
        bibliography = row['bibliography']
        other_names = row['other_names']
        contributor = row['contributor']
        notes = row['notes']
        gender = row['gender']
        subject_area = row['subject_area']
        path = row['path']


        historian= Historian(historian_id=historian_id, name=name, date_born=date_born, place_born=place_born, date_died=date_died, 
                    overview=overview, home_country=home_country, sources=sources, bibliography=bibliography, other_names=other_names,
                    contributor=contributor, notes=notes, gender=gender, subject_area=subject_area, path=path)
        session.add(historian)
        session.commit()
        print("added historian")
	

read_seed()