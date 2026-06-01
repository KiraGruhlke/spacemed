import matplotlib
matplotlib.use('Agg') 
from matplotlib import pyplot
import os
import sys
import nibabel

def main():
    # 1. Grab the slice index from Slurm environment. 
    # Fallback to 96 if you run it locally for testing.
    slice_idx_str = os.environ.get('SLURM_ARRAY_TASK_ID')
    if slice_idx_str is None:
        print("Not running as a Slurm array job. Defaulting to slice 96.")
        slice_idx = 96
    else:
        slice_idx = int(slice_idx_str)

    # 2. Load the data
    data_path = "/home/kigr11/Spacemed-2026/kigr11/data"
    img_file = os.path.join(data_path, "mri-data/2_Anatomy_1mm_5min.nii")
    
    anatomy = nibabel.load(img_file)
    data_anatomy = anatomy.get_fdata()

    # 3. Guard against out-of-bounds indices
    max_slices = data_anatomy.shape[0]
    if slice_idx >= max_slices:
        print(f"Error: Requested slice {slice_idx}, but max index is {max_slices - 1}")
        sys.exit(1)

    # 4. Create output directory if it doesn't exist
    output_dir = os.path.join(data_path, "f
    mri-data/slices")
    os.makedirs(output_dir, exist_ok=True)

    # 5. Plot and Save the slice
    fig, axes = pyplot.subplots(1)
    axes.imshow(data_anatomy[slice_idx, :, :].T, origin="lower", cmap="gray")
    axes.set_title(f"Slice {slice_idx}")
    axes.axis('off')  # Optional: hides axis ticks for a cleaner image

    # Save with zero-padded formatting (e.g., slice_005.png) so they sort correctly
    output_file = os.path.join(output_dir, f"slice_{slice_idx:03d}.png")
    pyplot.savefig(output_file, bbox_inches='tight')
    pyplot.close(fig)
    
    print(f"Successfully saved slice {slice_idx} to {output_file}")

if __name__ == "__main__":
    main()