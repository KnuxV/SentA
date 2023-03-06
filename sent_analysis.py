"""
Created by kevin-desktop, on the 24/02/2023
"""
import re
import time
from tqdm import tqdm
import pandas as pd
import numpy as np
from typing import List
import os

from asba_model import run_asba_model


def annotate_sent(dataframe):
    # df['sent'] = np.vectorize(run_asba_model)(df.AB, df.TXT)
    with tqdm(total=len(dataframe), position=0, leave=True) as pbar:
        dataframe['Neg'], dataframe['Neu'], dataframe['Pos'] = np.vectorize(run_asba_model)(dataframe.AB, dataframe.TXT,
                                                                                            pbar)
    return dataframe
    # df.to_pickle("results/small_test.pkl")
    # end = time.time()


def split_df(dataframe: pd.DataFrame, nb_partition: int) -> List[pd.DataFrame]:
    return np.array_split(dataframe, nb_partition)


def save_lst_df(lst_df: List[pd.DataFrame], directory: str):
    for ind, dataframe in enumerate(lst_df):
        df_path = os.path.join(directory, f'{ind + 1}.pkl')
        dataframe.to_pickle(df_path)


def join_df(folder: str) -> pd.DataFrame:
    lst_df = []
    for suf in os.listdir(folder):
        df_path = os.path.join(folder, suf)
        df = pd.read_pickle(df_path)
        lst_df.append(df)
    tot = pd.concat(lst_df)
    return tot


if __name__ == '__main__':
    # inter_path = "results/inter_digi_keywords_exploded.pkl"
    # df = pd.read_pickle(inter_path)
    # lst_inter = split_df(dataframe=df, nb_partition=50)
    # save_lst_df(lst_df=lst_inter, directory="results/split/")

    directory_input = "results/split"
    directory_output = "results/split_w_sent"

    tot_df = len(os.listdir(directory_input))
    for ind, suffix in enumerate(sorted(os.listdir(directory_input))):
        print(str(ind+1) + "/" + str(tot_df))
        df_path = os.path.join(directory_input, suffix)

        df = pd.read_pickle(df_path)

        df_annotated = annotate_sent(dataframe=df)
        df_annotated_path = os.path.join(directory_output, suffix)
        df_annotated.to_pickle(df_annotated_path)

        if os.path.isfile(df_path):
            os.remove(df_path)
        else:
            # If it fails, inform the user.
            print("Error: %s file not found" % df_path)

    tot = join_df(directory_output)
    tot.to_pickle("results/test.pkl")
