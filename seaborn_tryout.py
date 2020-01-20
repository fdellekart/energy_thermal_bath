import seaborn as sns
from thermal_bath import LoadCurve
import matplotlib.pyplot as plt

TIME_KEY = "times"
SRC_PATH = "load_curve_thermal_bath.csv"

sns.set()

load_curve = LoadCurve()
load_curve.load_data(SRC_PATH, "W")
load_curve.time_to_datetime(TIME_KEY)
load_curve.time_to_index(TIME_KEY)
load_curve.set_unit("kW")

load_curve.moving_average("lüftung", 5)

sns.pairplot(load_curve.get_data())

plt.show()