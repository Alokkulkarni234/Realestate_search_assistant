import pandas as pd

def search_properties(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    result = df.copy()

    if filters.get('city'):
        result = result[result['cityid'] == filters['city']]

    if filters.get('bhk'):
        result = result[result['bhk'].str.contains(filters['bhk'], case=False, na=False)]

    if filters.get('budget'):
        result = result[result['price'] <= filters['budget']]

    if filters.get('readiness'):
        result = result[result['status'] == filters['readiness']]

    if filters.get('locality'):
        result = result[result['fulladdress'].str.contains(filters['locality'], case=False, na=False)]

    return result.reset_index(drop=True)
