import numpy


def normalise(data):
    norm = (data - numpy.mean(data))
    norm = norm / numpy.std(data)
    return norm
