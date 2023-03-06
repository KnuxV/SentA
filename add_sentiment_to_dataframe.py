"""
Created by kevin-desktop, on the 18/02/2023
ADD sentiment columns to a sample Excel sheet.
"""
import numpy as np
import pandas as pd
import tqdm

from asba_model import run_models


path = "data/marco_sample.pkl"
df = pd.read_pickle(path)



dic = {}
max_nb_terms = 0
for row in tqdm.tqdm(df.itertuples(name=None)):
    ind = row[0]
    ti = row[1]
    ab = row[4]
    dtkey = row[13].split(", ")

    sentiments = run_models(ab, dtkey)
    if max_nb_terms < len(sentiments):
        max_nb_terms = len(sentiments)
    dic[ind] = sentiments


df_sent = pd.DataFrame.from_dict(dic, orient="index")
df_sent.rename(columns={i: f'Term{i + 1}' for i in range(0, max_nb_terms)}, inplace=True)

df = pd.concat([df, df_sent], axis=1)


lst_columns_w_term = [col for col in df.columns if 'Term' in col]
df.fillna('0', inplace=True)


df.to_excel("data/sample_marco.xlsx")
