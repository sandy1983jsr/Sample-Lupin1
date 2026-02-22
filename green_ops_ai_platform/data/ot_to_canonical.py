def pivot(df):
    df["variable"] = df["tag"].map(TAG_MAP)
    return df.pivot_table(
        index=["timestamp","site"],
        columns="variable",
        values="value",
        aggfunc="mean"
    ).reset_index()
