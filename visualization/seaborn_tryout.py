import sys

import seaborn as sns
import matplotlib.pyplot as plt

sys.path.append(r"C:\Users\f.dellekart\OneDrive - MPD-Innovations\Dokumente\Programming\energy_thermal_bath")

from thermal_bath import LoadCurve


sns.set()

load_curve = LoadCurve(r"C:\Users\f.dellekart\OneDrive - MPD-Innovations\Dokumente\Programming\energy_thermal_bath\properties.yaml")

load_curve.moving_average("lüftung", 5)

sns.pairplot(load_curve.data)

plt.show()