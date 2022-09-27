
import numpy as np

def block_data(data):
    """
    A function that reblocks correlated data (e.g. time series). This function starts reblocking the data from
    block size 1 until the optimal block size is reached, at this point the statistics for the optimal block
    are returned. 
    
    Parameters
    ----------
    data : 2D numpy array
        numpy array containing the data to be reblocked, this can be obtained using get_data functions
        
    Output
    ----------
    opt_block : 2D numpy array
        numpy array containing the statisitics for the optimal block of the reblocked data
        
    """

    opt_block = np.empty(shape=0)
    first_std_err  = np.std(data)/np.sqrt(int(len(data)))
    for i in range(1, (int(len(data)/4) - 1), 1):
        stats_temp = np.empty(shape=0)
        b_points = int(len(data)/i)
        obs = np.zeros(b_points)
        for j in range(1, b_points+1):
            b_start = (j - 1) * i
            b_end = b_start + i
            obs[j-1] = np.mean(data[b_start:b_end])
        stats_temp = np.array([i+1, b_points, np.mean(obs), np.std(obs)/np.sqrt(i+1)])
        cond = 2**(stats_temp[0])
        if cond > 2*stats_temp[1]*(stats_temp[3]/first_std_err)**4:  #block_stats[0, 3])**4:
            opt_block = stats_temp
            break
            
    return(opt_block) 