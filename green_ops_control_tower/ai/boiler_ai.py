from sklearn.ensemble import GradientBoostingRegressor

def boiler_ai(df, fuel_cost=6.5, ef=1.8):
    X = df[["load_pct","o2_pct","stack_temp_c"]]
    y = df["boiler_eff"]

    model = GradientBoostingRegressor(loss="quantile", alpha=0.8)
    model.fit(X, y)

    best = model.predict(X)
    gap = best - y

    savings = (gap.clip(lower=0) / y) * df["fuel_kgph"]
    return savings.sum() * fuel_cost * 365, savings.sum() * ef * 365 / 1000
