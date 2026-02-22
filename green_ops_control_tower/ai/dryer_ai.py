from sklearn.ensemble import RandomForestRegressor

def dryer_ai(df, power_cost=8, ef=0.82):
    X = df[["time_in_dryer_hr","dryer_temp_c","vacuum_mbar"]]
    y = df["dryer_kwh"]

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X, y)

    excess = (y - model.predict(X)).clip(lower=0)
    return excess.sum() * power_cost * 300, excess.sum() * ef * 300 / 1000
