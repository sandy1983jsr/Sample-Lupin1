def recommend_boiler_actions(df):
    recs = []

    if df["o2_pct"].mean() > 6:
        recs.append({
            "action": "Reduce excess air",
            "lever": "O₂ trim optimization",
            "expected_eff_gain_pct": 2.5,
            "confidence": "High"
        })

    if df["stack_temp_c"].mean() > 210:
        recs.append({
            "action": "Improve heat recovery",
            "lever": "Economizer cleaning / upgrade",
            "expected_eff_gain_pct": 1.8,
            "confidence": "Medium"
        })

    if (df["load_pct"] < 60).mean() > 0.3:
        recs.append({
            "action": "Avoid low-load cycling",
            "lever": "Load consolidation / scheduling",
            "expected_eff_gain_pct": 1.2,
            "confidence": "High"
        })

    return recs
