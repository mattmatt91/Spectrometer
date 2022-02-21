
import seabreeze.spectrometers as sb
from seabreeze.spectrometers import Spectrometer
import pandas as pd
from matplotlib import pyplot as plt
from time import time_ns

start_time = time_ns()

def get_time():
    return (time_ns() - start_time)/1000000



ammount_spectras = 100
spec = Spectrometer.from_first_available()

spec.integration_time_micros(20000)
counts = []
timestamps = []
for i in range(ammount_spectras):
    counts.append(spec.intensities())
    timestamps.append(get_time())

df = pd.DataFrame({'wavelength': spec.wavelengths()})
for spectra, timestamp in zip(counts, timestamps):
    df[timestamp] = spectra.tolist()
    
print(df.head())

for i in range(len(timestamps)-1):
    print(timestamps[i+1]- timestamps[i])
df.set_index('wavelength', inplace=True)
df.plot()
plt.show()
