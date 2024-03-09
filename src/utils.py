import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import q_stat
from statsmodels.tsa.stattools import adfuller


def qstat_is_random(p_value, alpha=0.05):
    if p_value < alpha:
        return False  # Rejects null hypothesis, it's not random.
    else:
        return True   # Cannot reject null hypothesis, it's random.
    
