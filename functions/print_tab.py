
import numpy as np

def print_data(data):
    """
    A function to print the output of the blocking function (optimal block statistics) in a table style.

    Parameters
    ----------
    data : 2D numpy array
        numpy array containing the statisitics for the optimal block of the reblocked data using block_data functions,
        in the VASP_block program labels (headers) are added 
    
    Output
    ----------
    the function prints out a table in the terminal 
        
    """
    print('-'*32 + 'Optimal Blocking Statistics' + '-'*31)
    colwidth = 15
    for i , row in enumerate(data):
        outrow = ''
        for j, item in enumerate(row):
            if j == 0:
                outrow += data[i, j].ljust(colwidth)
            else:
                outrow += ' | ' + data[i, j].ljust(colwidth)
        if i == 0:
            print(outrow)
            print('-'*((data.shape[1]+1)*colwidth))
        else:
            print(outrow)
