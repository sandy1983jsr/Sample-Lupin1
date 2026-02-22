from sklearn.ensemble import GradientBoostingRegressor

def detect_boiler_opportunities(df, fuel_cost, fuel_ef):
    X = df[["load_pct","o2_pct","stack_temp_c"]]
    y = df["boiler_efficiency_pct"]

    model = GradientBoostingRegressor(loss="quantile", alpha=0.8)
    model.fit(X, y)

    df["best_eff"] = model.predict(X)
    df["gap"] = df["best_eff"] - df["boiler_efficiency_pct"]

    opps = []
    for _, r in df[df["gap"] > 1].iterrows():
        fuel_saved = r["fuel_kgph"] * r["gap"] / r["boiler_efficiency_pct"]
        opps.append({
            "site": r["site"],
            "unit": "Boiler",
            "opportunity": "Combustion optimization",
            "annual_savings_rs": fuel_saved * fuel_cost * 365,
            "co2_reduction_tpy": fuel_saved * fuel_ef * 365 / 1000,
            "confidence": "High",
            "status": "Identified"
        })
    return opps
