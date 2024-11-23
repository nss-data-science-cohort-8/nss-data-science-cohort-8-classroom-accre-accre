import pandas as pd
import numpy as np
from datetime import datetime as dt


# optional milliseconds function
def optional_ms(series):
    # format with milliseconds
    parsed = pd.to_datetime(series, format="%Y-%m-%d %H:%M:%S.%f", errors="coerce")
    # Handle rows where the first attempt failed
    nats = parsed.isna()
    if nats.any():
        parsed[nats] = pd.to_datetime(
            series[nats], format="%Y-%m-%d %H:%M:%S", errors="coerce"
        )
    return parsed
