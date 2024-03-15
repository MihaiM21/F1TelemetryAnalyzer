import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import fastf1 as ff1
import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# Setup plotting
plotting.setup_mpl()
# Enable the cache
#ff1.Cache.enable_cache('cache')

driver1 = 'LEC'
driver2 = 'NOR'
year = 2023
round = 18
session = 'Q'

# Load the session data
race = ff1.get_session(year, round, session)

# Collect all race laps

race.load()
laps = race.laps
# Get laps of the drivers (BOT and HAM)

laps_driver1 = laps.pick_driver(driver1)
laps_driver2 = laps.pick_driver(driver2)
# Extract the fastest laps
fastest_driver1 = laps_driver1.pick_fastest()
fastest_driver2 = laps_driver2.pick_fastest()

# Get telemetry from fastest laps
telemetry_driver1 = fastest_driver1.get_car_data().add_distance()
telemetry_driver2 = fastest_driver2.get_car_data().add_distance()

fig, ax = plt.subplots(4)
fig.suptitle("Fastest Lap Telemetry Comparison")

ax[0].plot(telemetry_driver1['Distance'], telemetry_driver1['Speed'], label=driver1)
ax[0].plot(telemetry_driver2['Distance'], telemetry_driver2['Speed'], label=driver2)
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")
ax[1].plot(telemetry_driver1['Distance'], telemetry_driver1['Throttle'], label=driver1)
ax[1].plot(telemetry_driver2['Distance'], telemetry_driver2['Throttle'], label=driver2)
ax[1].set(ylabel='Throttle')
ax[2].plot(telemetry_driver1['Distance'], telemetry_driver1['Brake'], label=driver1)
ax[2].plot(telemetry_driver2['Distance'], telemetry_driver2['Brake'], label=driver2)
ax[2].set(ylabel='Brakes')
ax[3].plot(telemetry_driver1['Distance'], telemetry_driver1['Brake'], label=driver1)
ax[3].plot(telemetry_driver1['Distance'], telemetry_driver1['Throttle'], label=driver1)
ax[3].set(ylabel='Comparison')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for a in ax.flat:
    a.label_outer()
    
plt.show()