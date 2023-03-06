"""
Created by kevin-desktop, on the 25/02/2023
Annotate database with DT keywords and then explode the DB (one row for each PUB+single dt keyword)
"""
import pandas as pd


def annotate_in_dt_explode(dataframe_path, excel_dt_keyword_path):
    digi_keywords = pd.read_csv(excel_dt_keyword_path, sep=',')
    dic_digi = {}
    all_keywords = []
    for keyword in digi_keywords.columns:
        lst = [keyword for keyword in digi_keywords[keyword].to_list() if not isinstance(keyword, float)]
        dic_digi[keyword] = lst
        all_keywords += lst

    inter = pd.read_pickle(dataframe_path)

    t_sb = [r"\b" + word.lower().replace("*", r"\w*") + r"\b" for word in all_keywords]
    pattern = '|'.join(t_sb)
    inter["TXT"] = inter.TXT.str.lower().str.findall(pattern).apply(set)

    inter = inter.explode("TXT")
    inter.TXT.fillna('', inplace=True)

    return inter
