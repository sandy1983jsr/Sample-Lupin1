def validate(predicted, actual, cost, ef):
    saved = predicted - actual
    saved = saved[saved > 0].sum()
    return {
        "energy_saved": saved,
        "cost_saved_rs": saved * cost,
        "co2_saved_t": saved * ef / 1000,
        "method":"IPMVP Option C"
    }
