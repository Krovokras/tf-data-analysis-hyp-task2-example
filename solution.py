import pandas as pd
import numpy as np
from scipy.stats import kstest


chat_id = 1134491798

def solution(x: np.array, y: np.array) -> bool:
   
    ks_statistic, p_value = kstest(x, y)
    
   
    if p_value < 0.03:
        return True
    else:
        return False
