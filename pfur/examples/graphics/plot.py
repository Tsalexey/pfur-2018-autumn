import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from scipy.interpolate import spline
import math

def main():
    x = [-math.pi, -math.pi/2, 0, math.pi/2, math.pi];
    y = np.cos(x);

    plot(x, y, 'x', 'y', 'example.pdf');

def plot(x, y, x_name, y_name, filename):
    # create new pdf file
    with PdfPages(filename) as pdf:
        # make new figure
        fig = plt.figure()

        # configure output to all figure
        ax = fig.add_subplot(111)

        # cast x/y arrays to np_arrays
        x_sm = np.array(x).astype(np.float)
        y_sm = np.array(y).astype(np.float)

        # get interpolated
        x_smooth = np.linspace(x_sm.min(), x_sm.max(), 1000)
        y_smooth = spline(x, y_sm, x_smooth)

        # plot
        ax.plot(x_smooth, y_smooth)

        # configure labels
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name, rotation=0)

        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()

        # ratio of y to x
        ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))

        # configure grid
        ax.grid(b=True, which='major', axis='both', color='grey', linestyle=':')

        # save figure
        pdf.savefig()
        plt.close()

if __name__ == '__main__':
	main()

