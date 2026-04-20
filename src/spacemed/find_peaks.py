def find_peaks (data, w):
    peaks = []
    for i in range (len(data)): # the window moves along the dataset
        start = max(i-w, 0) # the point before is lower (i-w), 0 to include start of data
        end = min(i+w, len(data)) # len(subset) to include the end of data
        window = data[start:end]
        max_pos = numpy.argmax(window) + start # gives us the position inside the window, where the maximum is
        if i == max_pos:
            peaks.append(i)
    return peaks
