# utils/threats.py

import pandas as pd
import random
from datetime import datetime

def generate_fake_threats():
    """Generate a DataFrame with fake threat data."""
    threats = {
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(5)],
        "Threat Type": random.choices(["Firewall Breach", "Phishing Attempt", "Device Anomaly"], k=5),
        "Severity": random.choices(["Critical", "High", "Medium", "Low"], k=5),
        "Source IP": [f"192.168.1.{random.randint(1, 255)}" for _ in range(5)],
    }
    return pd.DataFrame(threats)