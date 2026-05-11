import numpy
import scipy.signal

def compute_crosscorrelation(fmri_data, signal, data):
    data = fmri_data[p]
    cross = scipy.signal.correlate(
    # show cross correlation to not just eyeball it 
        normalise(data), normalise(signal),
        mode="same")
    lags = scipy.signal.correlation_lags(
    # lags = it takes e.g. 8 seconds until the brain reacts after an event
        len(data), len(signal),
        mode="same")
    pyplot.plot(lags, cross)
    c = numpy.max(cross) # maximal cross correlation
    print(c)