import seaborn as sns
from thermal_bath import LoadCurve
import matplotlib.pyplot as plt

TIME_KEY = "times"
SRC_PATH = "load_curve_thermal_bath.csv"

sns.set()

load_curve = LoadCurve(SRC_PATH, "W", TIME_KEY)

load_curve.moving_average("lüftung", 5)

sns.pairplot(load_curve.data)

plt.show()