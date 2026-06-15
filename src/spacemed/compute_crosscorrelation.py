import numpy
import scipy.signal
from .normalise_data import normalise


def compute_crosscorrelation(fmri_data, signal, p):
    data = fmri_data[p]
    # show cross correlation to not just eyeball it
    cross = scipy.signal.correlate(
        normalise(data), normalise(signal), mode="same"
    )
    c = numpy.max(cross)  # maximal cross correlation
    print(c)
