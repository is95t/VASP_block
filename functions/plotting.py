
import matplotlib.pyplot as plt
import numpy as np

def plot_data(data, stats, d_type=None, legend=False):
    """
    A function to plot data from a VASP run (e.g. pressure, temperature data in a time series) with the mean and 1
    standard deviation plotted.

    Parameters
    ----------
    data : 2D numpy array
        numpy array containing the data to be reblocked, this can be obtained using get_data functions
    stats : 2D numpy array
        numpy array containing the statisitics for the optimal block of the reblocked data using block_data functions
    d_type : string
        the type of data being plotted:
            'pressure' - pressure data (GPa)
            'temperature' - temperature data (K)
            'volume' - volume data (A^3)
            'energy' - total energy data (eV)
    legend : boolean (default False)
        if True a legend is also shown
        
    Output
    ----------
    fig : pyplot figure
        the plot is retunred as a pyplot figure
        
    """

    fig = plt.figure()
    std_dev = stats[3] * np.sqrt(stats[0])
    plt.xlabel('Ionic Steps')
    if d_type == 'pressure':
        plt.ylabel('Pressure (GPa)')
        plt.title('Pressure')
    elif d_type == 'temperature':
        plt.ylabel('Temperature (K)')
        plt.title('Temperature')
    elif d_type == 'volume':
        plt.ylabel('Volume (A$^3$)')
        plt.title('Volume')
    elif d_type == 'energy':
        plt.ylabel('Total Energy (eV)')
        plt.title('Total Energy')
    else:
        plt.ylabel('Output Data')
        plt.title('Output Data')
    plt.plot(np.linspace(0, len(data), len(data)), data, c='darkgrey', label='Data')
    plt.plot((0, len(data)), (stats[2], stats[2]), c='red', label='Mean')
    plt.plot((0, len(data)), ((stats[2] + std_dev), (stats[2] + std_dev)), c='red', linestyle='--', label='1 Standard Deviation')
    plt.plot((0, len(data)), ((stats[2] - std_dev), (stats[2] - std_dev)), c='red', linestyle='--')
    #plt.plot((0, len(data)), ((stats[2] + std_dev*1.96), (stats[2] + std_dev*1.96)), c='red', linestyle='-.', label='95% Confidence Interval')
    #plt.plot((0, len(data)), ((stats[2] - std_dev*1.96), (stats[2] - std_dev*1.96)), c='red', linestyle='-.')
    if legend == True:
        plt.legend(loc='upper right')
    return fig



def plot_data_sub(data, stats, ax, d_type=None):
    """
    A function to plot data from a VASP run (e.g. pressure, temperature data in a time series) with the mean and 1
    standard deviation plotted, adapted for plotting the subplot in the VASP_block program

    Parameters
    ----------
    data : 2D numpy array
        numpy array containing the data to be reblocked, this can be obtained using get_data functions
    stats : 2D numpy array
        numpy array containing the statisitics for the optimal block of the reblocked data using block_data functions
    ax : typically axs[col, row]
        location of plot within subplot
    d_type : string
        the type of data being plotted:
            'pressure' - pressure data (GPa)
            'temperature' - temperature data (K)
            'volume' - volume data (A^3)
            'energy' - total energy data (eV)

    """

    std_dev = stats[3] * np.sqrt(stats[0])
    ax.set_xlabel('Ionic Steps')
    if d_type == 'pressure':
        ax.set_ylabel('Pressure (GPa)')
        ax.set_title('Pressure')
    elif d_type == 'temperature':
        ax.set_ylabel('Temperature (K)')
        ax.set_title('Temperature')
    elif d_type == 'volume':
        ax.set_ylabel('Volume (A$^3$)')
        ax.set_title('Volume')
    elif d_type == 'energy':
        ax.set_ylabel('Total Energy (eV)')
        ax.set_title('Total Energy')
    else:
        ax.set_ylabel('Output Data')
        ax.set_title('Output Data')
    ax.plot(np.linspace(0, len(data), len(data)), data, c='darkgrey', label='Data')
    ax.plot((0, len(data)), (stats[2], stats[2]), c='red', label='Mean')
    ax.plot((0, len(data)), ((stats[2] + std_dev), (stats[2] + std_dev)), c='red', linestyle='--', label='1 Standard Deviation')
    ax.plot((0, len(data)), ((stats[2] - std_dev), (stats[2] - std_dev)), c='red', linestyle='--')
    #ax.plot((0, len(data)), ((stats[2] + std_dev*1.96), (stats[2] + std_dev*1.96)), c='red', linestyle='-.', label='95% Confidence Interval')
    #ax.plot((0, len(data)), ((stats[2] - std_dev*1.96), (stats[2] - std_dev*1.96)), c='red', linestyle='-.')
