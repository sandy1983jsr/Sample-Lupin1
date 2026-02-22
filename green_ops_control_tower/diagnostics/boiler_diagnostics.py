import pandas as pd

def compute_boiler_losses(df):
    losses = {}

    # Excess air proxy
    losses["excess_air_loss_pct"] = (
        (df["o2_pct"] - 3).clip(lower=0) * 0.25
    )

    # Stack temperature loss
    losses["stack_loss_pct"] = (
        (df["stack_temp_c"] - 150).clip(lower=0) * 0.015
    )

    # Low load cycling loss
    losses["low_load_loss_pct"] = (
        (50 - df["load_pct"]).clip(lower=0) * 0.1
    )

    return pd.DataFrame(losses)
