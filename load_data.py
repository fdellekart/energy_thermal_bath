import pandas as pd

with open("load_curve_thermal_bath.csv", 'r') as f:
    data = pd.read_csv(f)

print(data)