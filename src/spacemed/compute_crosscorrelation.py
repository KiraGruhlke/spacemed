import numpy
import scipy.signal

def compute_crosscorrelation(fmri_data, signal, data):
    voxel_time_series = fmri_data[data] 
    def normalise(ts):
        return (ts - numpy.mean(ts)) / (numpy.std(ts) * len(ts))
    cross = scipy.signal.correlate(
        normalise(voxel_time_series), 
        normalise(signal), 
        mode="same")
    max_correlation = numpy.max(cross)
    lags = scipy.signal.correlation_lags(
        len(voxel_time_series), 
        len(signal), 
        mode="same")
    max_lag = lags[numpy.argmax(cross)]
    return max_correlation, max_lag