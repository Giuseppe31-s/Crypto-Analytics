import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import q_stat
from statsmodels.tsa.stattools import adfuller
from scipy import stats


def qstat_is_random(p_value, alpha=0.05):
    if p_value < alpha:
        return False  # Rejects null hypothesis, it's not random.
    else:
        return True   # Cannot reject null hypothesis, it's random.
    

def monte_carlo_simulation(y, days_ahead, simulations):
  df_retorn_tax =  np.log(1 + y.pct_change())
  df_retorn_tax.dropna(inplace = True)    
  u = df_retorn_tax.mean()
  var = df_retorn_tax.var()
  drift = u - (0.5 * var)
  std = df_retorn_tax.std()
  Z = stats.norm.ppf(np.random.rand(days_ahead, simulations))
  diary_return = np.exp(drift + std * Z)
  predict = np.zeros_like(diary_return)
  predict[0] = y.iloc[-days_ahead]
  for day in range(1, days_ahead):
    predict[day] = predict[day - 1] * diary_return[day]
  return predict
    
