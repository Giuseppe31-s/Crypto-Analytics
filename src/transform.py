import pandas as pd
from datetime import datetime


def transfrom_date(dataframe: pd.DataFrame, name_colum_date: str) -> pd.DataFrame:
    data = dataframe.copy()
    data[f"{name_colum_date}"] = data[f"{name_colum_date}"].apply(
        lambda x: datetime.utcfromtimestamp(x)
    )
    return data


def transform_to_float(dataframe: pd.DataFrame, name_colum: str) -> pd.DataFrame:
    data = dataframe.copy()
    data[f"{name_colum}"] = data[f"{name_colum}"].astype(float)
    return data
