"""
Created by kevin-desktop, on the 19/02/2023
create a column annotator with values (Claudia, Giacomo, Stefano, Kevin)
"""

import pandas as pd
import numpy as np

df_sample = pd.read_excel('data/sample.xlsx', sheet_name="Sheet1", index_col=0)

# Split dataframe into SDG groups
gb = df_sample.groupby('SDG')
split = [gb.get_group(x) for x in gb.groups]

annotator = {0: 'Claudia', 1: 'Giacomo', 2: 'Stefano', 3: 'Kevin'}
lst_df = []
# For each SDG groups, split into 4 dataframe for each annotator and then add a new column Annotator according to dic
for sdg in split:
    lst_df_sdg = np.array_split(sdg, len(annotator))
    for ind, df_sdg in enumerate(lst_df_sdg):
        df_sdg['Annotator'] = annotator[ind]
        lst_df.append(df_sdg)

finish = pd.concat(lst_df)

finish.to_excel('data/sample.xlsx')
