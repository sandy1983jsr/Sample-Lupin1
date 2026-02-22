import pandas as pd
import numpy as np

class MockOTConnector:
    def fetch(self, start, end):
        ts = pd.date_range(start, end, freq="H")
        data = []
        for t in ts:
            data.append({"timestamp": t,"site":"Site_A","tag":"Boiler_O2","value":np.random.uniform(5,8)})
            data.append({"timestamp": t,"site":"Site_A","tag":"Fuel","value":np.random.uniform(1500,2000)})
        return pd.DataFrame(data)
