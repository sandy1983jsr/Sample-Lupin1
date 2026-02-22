from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_dryer_baseline_model(df):
    """
    Learns expected dryer energy based on operating conditions
    """
    X = df[[
        "time_in_dryer_hr",
        "dryer_temp_c",
        "vacuum_mbar"
    ]]
    y = df["dryer_kwh"]

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=6,
        random_state=42
    )
    model.fit(X, y)

    return model


def detect_dryer_opportunities(df, model, power_cost, grid_ef):
    """
    Identifies over-drying and inefficient operation
    """
    X = df[[
        "time_in_dryer_hr",
        "dryer_temp_c",
        "vacuum_mbar"
    ]]
    df = df.copy()
    df["expected_kwh"] = model.predict(X)
    df["excess_kwh"] = df["dryer_kwh"] - df["expected_kwh"]

    opps = []

    for _, r in df[df["excess_kwh"] > 10].iterrows():
        opps.append({
            "molecule": r["molecule"],
            "issue": "Over-drying / conservative endpoint",
            "energy_saved_kwh_per_batch": r["excess_kwh"],
            "annual_cost_saving_rs": r["excess_kwh"] * power_cost * 300,
            "co2_reduction_tpy": r["excess_kwh"] * grid_ef * 300 / 1000,
            "confidence": "High (historically achieved)",
            "recommended_action": "Implement ML-based drying end-point"
        })

    return pd.DataFrame(opps)
