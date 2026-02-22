import pandas as pd

def build_register(*lists):
    df = pd.DataFrame([x for lst in lists for x in lst])
    return df.sort_values("annual_savings_rs", ascending=False)
