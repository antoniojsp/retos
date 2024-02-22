import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # products["quantity"] = products["quantity"].fillna(0)
    products["quantity"] = products["quantity"].replace({None: 0})
    return products