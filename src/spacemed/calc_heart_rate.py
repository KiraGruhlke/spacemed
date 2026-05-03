import numpy   # noqa F401
from matplotlib import pyplot   # noqa F401
import spacemed   # noqa F401


def calc_heart_rate(time, peaks):
    time_peaks = time[peaks]
    delta_t = time_peaks[1:] - time_peaks[:-1]
    hr = 60 / delta_t
    return hr
