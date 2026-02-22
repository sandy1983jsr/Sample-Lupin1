def boiler_efficiency(row, gcv=3800):
    useful = row["steam_tph"] * 1000 * (660 - 105)
    input_energy = row["fuel_kgph"] * gcv
    return useful / input_energy * 100
