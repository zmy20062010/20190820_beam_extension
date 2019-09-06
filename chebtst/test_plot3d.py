import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib.colors import LogNorm

def get_demo_image():
    import numpy as np
    from matplotlib.cbook import get_sample_data
    f = get_sample_data("axes_grid/bivariate_normal.npy", asfileobj=False)
    z = np.load(f)
    # z is a numpy array of 15x15
    return z, (-3, 4, -4, 3)

def demo_grid_with_single_cbar(fig):
    """
    A grid of 2x2 images with a single colorbar
    """
    grid = AxesGrid(fig, 111,  # modified to be only subplot
                    nrows_ncols=(2, 2),
                    axes_pad=0.0,
                    share_all=True,
                    label_mode="L",
                    cbar_location="top",
                    cbar_mode="single",
                    )

    Z, extent = get_demo_image()
    for i in range(4):
        im = grid[i].imshow(Z, extent=extent, interpolation="nearest")
    #plt.colorbar(im, cax = grid.cbar_axes[0])
    grid.cbar_axes[0].colorbar(im)

    for cax in grid.cbar_axes:
        cax.toggle_label(False)

    # This affects all axes as share_all = True.
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])
    plt.show()

def demo_grid_with_single_cbar_log(fig):
    """
    A grid of 2x2 images with a single colorbar and log scaling
    """
    grid = AxesGrid(fig, 111,  # modified to be only subplot
                    nrows_ncols=(2, 2),
                    axes_pad=0.0,
                    share_all=True,
                    label_mode="L",
                    cbar_location="top",
                    cbar_mode="single",
                    )

    Z, extent = get_demo_image()
    Z -= np.min(Z)  # modified to make data positive
    for i in range(4):
        im = grid[i].imshow(Z, extent=extent, interpolation="nearest", norm=LogNorm())  # modified to log-scale display
    #plt.colorbar(im, cax = grid.cbar_axes[0])
    grid.cbar_axes[0].colorbar(im)

    for cax in grid.cbar_axes:
        cax.toggle_label(False)

    # This affects all axes as share_all = True.
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])
    plt.show()


fig = plt.figure()
demo_grid_with_single_cbar(fig)

fig = plt.figure()
demo_grid_with_single_cbar_log(fig)
