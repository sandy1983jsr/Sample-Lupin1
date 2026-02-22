import pandas as pd
import numpy as np

def compute_dryer_kpis(df):
    """
    Core dryer KPIs
    """
    kpis = {}

    # Specific Energy Consumption
    kpis["SEC_kWh_per_kg"] = (
        df["dryer_kwh"].sum() / df["api_kg"].sum()
        if df["api_kg"].sum() > 0 else None
    )

    # Average drying time
    kpis["avg_drying_time_hr"] = df["time_in_dryer_hr"].mean()

    # Energy intensity per batch-hour
    kpis["kWh_per_hr"] = (
        df["dryer_kwh"] / df["time_in_dryer_hr"]
    ).mean()

    return kpis


def identify_dryer_losses(df):
    """
    Loss breakdown using data-driven + physics proxies
    """
    losses = pd.DataFrame(index=df.index)

    # 1. Over-drying loss (time-based proxy)
    losses["overdrying_loss_kwh"] = (
        (df["time_in_dryer_hr"] - df["time_in_dryer_hr"].quantile(0.5))
        .clip(lower=0)
        * (df["dryer_kwh"] / df["time_in_dryer_hr"])
    )

    # 2. High temperature loss
    losses["high_temp_loss_kwh"] = (
        (df["dryer_temp_c"] - 80)
        .clip(lower=0)
        * 0.03
        * df["dryer_kwh"]
    )

    # 3. Poor vacuum efficiency
    losses["vacuum_loss_kwh"] = (
        (df["vacuum_mbar"] - 120)
        .clip(lower=0)
        * 0.02
        * df["dryer_kwh"]
    )

    losses["total_loss_kwh"] = losses.sum(axis=1)

    return losses
