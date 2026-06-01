import argparse
from matplotlib import pyplot
import nibabel
import numpy
import scipy.signal


def normalise(data):
    std_val = numpy.std(data)
    # Protection against dividing by zero for empty background voxels
    if std_val == 0:
        return numpy.zeros_like(data)
    norm = (data - numpy.mean(data))
    norm = norm / std_val
    return norm


def main():
    # 1. Set up command line arguments
    parser = argparse.ArgumentParser(description="Compute cross-correlation for one fMRI slice.")
    parser.add_argument("fmri_file", help="name of fMRI file")
    parser.add_argument("slice_num", type=int, help="the slice to process (an integer)")
    parser.add_argument("output_image", help="the name of the output image file")
    args = parser.parse_args()

    # 2. Load the fMRI data
    print(f"Loading {args.fmri_file}...")
    fmri = nibabel.load(args.fmri_file)
    fmri_data = fmri.get_fdata()

    # Get the number of timepoints (the last dimension of the shape)
    nt = fmri_data.shape[-1]

    # 3. Create the block-design signal
    s_one = numpy.array([1]*5 + [0]*5)
    signal = numpy.tile(s_one, int(numpy.ceil(nt/10)))
    signal = signal[:nt]
    norm_signal = normalise(signal)

    # 4. Extract dimensions and prepare the output array
    z_slice = args.slice_num
    x_dim = fmri_data.shape[0]
    y_dim = fmri_data.shape[1]

    # Verify the requested slice is within bounds
    if z_slice < 0 or z_slice >= fmri_data.shape[2]:
        print(f"Error: Slice {z_slice} is out of bounds. Must be between 0 and {fmri_data.shape[2]-1}")
        return

    print(f"Processing cross-correlation for slice {z_slice}. This may take a moment...")
    cross_corr_map = numpy.zeros((x_dim, y_dim))

    # 5. Compute cross-correlation for every voxel in the slice
    for x in range(x_dim):
        for y in range(y_dim):
            # Extract time series for the specific voxel
            voxel_data = fmri_data[x, y, z_slice, :]
            
            # Skip empty background voxels to save processing time
            if numpy.std(voxel_data) > 0:
                cross = scipy.signal.correlate(
                    normalise(voxel_data), norm_signal,
                    mode="same")
                # Store the max cross-correlation value as done in the original snippet
                c = numpy.max(cross)
                cross_corr_map[x, y] = c

    # 6. Display and save the data
    print(f"Saving output to {args.output_image}...")
    fig, axes = pyplot.subplots(1)

    # Plotted transposed (.T) and with origin="lower" to match your anatomy plot style
    # Used 'hot' colormap as it is standard for fMRI activation maps
    im = axes.imshow(cross_corr_map.T, origin="lower", cmap="hot")
    fig.colorbar(im, ax=axes, label="Max Cross-Correlation")
    axes.set_title(f"fMRI Cross-Correlation (Slice {z_slice})")

    # Save the figure instead of just showing it
    pyplot.savefig(args.output_image)
    print("Complete!")


if __name__ == "__main__":
    main()
