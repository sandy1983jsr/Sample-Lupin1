import pandas as pd

REQUIRED_COLUMNS = {
    "timestamp","site","load_pct","steam_tph","fuel_kgph",
    "o2_pct","stack_temp_c","dryer_kwh","dryer_temp_c",
    "vacuum_mbar","time_in_dryer_hr","api_kg","molecule"
}

def load_csv(files):
    dfs = []
    for f in files:
        df = pd.read_csv(f)
        missing = REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"{f.name} missing columns {missing}")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
