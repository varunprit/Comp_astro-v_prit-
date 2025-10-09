import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Getting the fourier transformation of TESS data",
        usage="\nTo run this code type:\n  python %(prog)s --plot, you can pick if you want to see the original plot or the fourier transformed \n\nExample:\n  python %(prog)s --plot_og True"
    )
    parser.add_argument("--plot", default=True, action='store_true', help="Shows the fourier transformed data")
    parser.add_argument("--plot_og", default=False, action='store_true', help="Shows the original data")
    args = parser.parse_args()

    hdul = fits.open('TESS.fits')
    times = hdul[1].data['times']
    fluxes = hdul[1].data['fluxes']
    ferrs = hdul[1].data['ferrs']

    datemask=(times>2990) & (times<3000) #setting limit so it ignores gaps
    times_cut = times[datemask]
    fluxes_cut =fluxes[datemask]

    fluxes_diff = fluxes_cut - np.median(fluxes_cut)
#plt.scatter(times_cut,fluxes_diff)

    c = np.fft.rfft(fluxes_diff)
    k = np.arange(len(c))
    c_sqr=abs(c)**2

    maxc_sqr=np.max(c_sqr[1:])
    freqmask=c_sqr>(0.1*maxc_sqr)
    freqmask.sum()

    Cfilt=np.where(freqmask, c, 0)
    inverted=np.fft.irfft(Cfilt,n=times_cut.size)

    if args.plot:
        plt.scatter(times_cut, inverted, color='red')

    if args.plot_og:
        plt.scatter(times_cut, fluxes_diff, color='blue')

    plt.show()
    plt.xlabel('Time (days)')
    plt.ylabel('Flux (e-/s)')
    plt.title('TESS Data Fourier Transform')
    plt.grid()
    plt.legend(['Fourier Transformed Data', 'Original Data'])


if __name__ == "__main__": # This thing means the code will run in the command line
    result = main()