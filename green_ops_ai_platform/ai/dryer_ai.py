from sklearn.ensemble import RandomForestRegressor

def detect_dryer_opportunities(df, power_cost, grid_ef):
    X = df[["time_in_dryer_hr","dryer_temp_c","vacuum_mbar"]]
    y = df["dryer_kwh"]

    model = RandomForestRegressor()
    model.fit(X, y)

    df["pred"] = model.predict(X)
    df["excess"] = df["dryer_kwh"] - df["pred"]

    opps = []
    for _, r in df[df["excess"] > 10].iterrows():
        opps.append({
            "site": r["site"],
            "unit": "Dryer",
            "opportunity": "Over-drying reduction",
            "annual_savings_rs": r["excess"] * power_cost * 300,
            "co2_reduction_tpy": r["excess"] * grid_ef * 300 / 1000,
            "confidence": "High",
            "status": "Identified"
        })
    return opps
