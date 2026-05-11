# This python script is to be able to compute the cross-correlation/
# brain activation based on fMRI data directly on command line


from pathlib import Path
from matplotlib import pyplot
import numpy
import nibabel
import argparse
from . import fmri_cross_corr
from . import __version__

# Define a function to create an interface on the command line that helps
# with package usage


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data", type=Path,
        help="the name of the input file")
    parser.add_argument(
        "slice", type=int,
        help="slice index to process")
    parser.add_argument(
        "-o", "--output", type=Path, default="cc_act.png",
        help="write output to file")  # Options are always added with a "-"
    parser.add_argument(
        "--version", action="version",
        version=f'%(prog)s {__version__}')
    return parser


# Define a function that can be executable to plot the cross-correlated
# activation

def main():
    parser = arg_parser()  # Call on the parser function from above
    args = parser.parse_args()

    # Load the data using nibabel: We need the path
    # stored in "args.data" above
    fmri = nibabel.load(args.data)

    # Get the desired data from the file
    fmri_data = fmri.get_fdata()

    # Get the number of samples
    nt = fmri.shape[-1]  # get the numer of samples

    # Create a numpy array for sampling sequence where the sampling
    # frequency is 2sec, on 10 seconds off 10 seconds
    s_one = numpy.array([1] * 5 + [0] * 5)
    signal = numpy.tile(s_one, int(numpy.ceil(nt / 10)))  # round up
    signal = signal[:nt]  # Clip the rounded up array to  accomodate nt

    # Get the slice that is to be examined
    index = args.slice

    # Check validity of the desired slice
    if index < 0 or index >= fmri_data.shape[2]:
        parser.error("invalid slice")

    # Compute the cross-correlation matrix using "fmri_act":
    # We need the data, the signal, and the slice
    cc_mat = fmri_cross_corr(signal, fmri_data, index)

    # Plot the cross-correlation matrix to show the brain activation
    pyplot.imshow(cc_mat.T, origin="lower", cmap="viridis")
    pyplot.colorbar(label="Activation")
    pyplot.title(f"fMRI Activation Map for Longitudinal Slice {index}")
    pyplot.xlabel("Voxel X")
    pyplot.ylabel("Voxel Y")

    # Save the output file with the filename specified above in "outname"
    pyplot.savefig(args.output)


# Check to make sure the script is being run directly as opposed to being
# imported
if __name__ == '__main__':
    # If the above is true, then when the script is executed the code will run
    main()
