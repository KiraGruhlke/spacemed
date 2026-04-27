from pathlib import Path
import argparse
import numpy
import spacemed
spacemed.__version__
from matplotlib import pyplot
from . import read_pulse
from . import find_peaks
from . import calc_heart_rate

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
      "data", type=Path,
      help="the name of the input file")
    parser.add_argument(
      "-o", "--output", type=Path,
      help="write output to file")
    parser.add_argument(
      "--version", action="version",
      version=f'%(prog)s {__version__}')
    return parser

def main():
    indata = Path("data/pulse_data.csv")
    outname = Path("heart_rate.pdf")

    time, absorption =read_pulse ("data/pulse_data.csv")
    absorption = numpy.array(absorption)
    time = numpy.array(time)

    peaks = find_peaks (absorption, w=50)
    #pyplot.plot(absorption)
    #pyplot.plot(peaks, absorption[peaks], "ro")
    print(peaks)

    peaks = numpy.array(peaks)
    time = numpy.array(time)
    heart_rate = calc_heart_rate (time, peaks)
    pyplot.plot(heart_rate)

    pyplot.savefig(outname)

if __name__ == '__main__':
    main()
