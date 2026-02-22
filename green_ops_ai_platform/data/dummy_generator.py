import pandas as pd
import numpy as np

def generate_dummy_data(hours=168, site="Site_A"):
    df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=hours, freq="H"),
        "site": site,
        "load_pct": np.random.uniform(50, 90, hours),
        "steam_tph": np.random.uniform(8, 18, hours),
        "fuel_kgph": np.random.uniform(1300, 2000, hours),
        "o2_pct": np.random.uniform(5, 8, hours),
        "stack_temp_c": np.random.uniform(180, 240, hours),
        "dryer_kwh": np.random.uniform(250, 420, hours),
        "dryer_temp_c": np.random.uniform(60, 90, hours),
        "vacuum_mbar": np.random.uniform(80, 200, hours),
        "time_in_dryer_hr": np.random.uniform(4, 10, hours),
        "api_kg": np.random.uniform(300, 700, hours),
        "molecule": np.random.choice(["API_X", "API_Y"], hours)
    })
    return df
