# level1

import pandas as pd
import numpy as np

def solution(id_list, report, k):

    df = pd.DataFrame(np.zeros((len(id_list), len(id_list))), index = id_list, columns = id_list).astype('int')
    
    for rep in report:
        df.loc[rep.split(' ')[0], rep.split(' ')[1]] = 1

    stop_list=[id for id in id_list if df[id].sum() >= k]
    
    return list(df[stop_list].sum(axis=1))

