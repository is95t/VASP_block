
import numpy as np

def get_data(f_path, d_type, d_cut=0):
    """
    A function to collect a cetain type of data from VASP output files.
    
    Parameters
    ----------
    f_path : string
        the path to the folder containing the VASP output files (OUTCAR/OSZICAR)
    d_type : string
        the type of data to collect:
            'pressure' - pressure data (GPa)
            'temperature' - temperature data (K)
            'volume' - volume data (A^3)
            'pressure' - pressure data (eV)
    d_cut : int (optional)
        amount of data to remove from the start of the run
        
    Output
    ----------
    raw_data : 2D numpy array
        numpy array containing output data
        
    """
    
    raw_data = np.empty(shape=0)
    if d_type == 'temperature':
        output_file = open(f_path + '/OSZICAR')
        output_data = output_file.read()
        for line in output_data.splitlines():
            if "T=" in line:
                float_num = 0
                for i in line.split():
                    try:
                        data_temp = float(i)
                        float_num = float_num + 1
                        if float_num == 2:
                            break
                    except:
                        continue
                raw_data = np.append(raw_data, data_temp)
    else:
        if d_type == 'pressure':
            type_str = "total pressure"
        elif d_type == 'volume':
            type_str = "volume of cell"
        elif d_type == 'energy':
            type_str = "ETOTAL"
        output_file = open(f_path + '/OUTCAR')
        output_data = output_file.read()
        for line in output_data.splitlines():
            if type_str in line:
                for i in line.split():
                    try:
                        data_temp = float(i)
                        break
                    except:
                        continue
                if d_type == 'pressure':
                    data_temp = data_temp * 0.1
                raw_data = np.append(raw_data, data_temp)
    raw_data = raw_data.reshape(-1, 1)
    if d_type == 'volume':
        raw_data = np.delete(raw_data, 0, axis=0)
    else:
        pass
    if d_type == 0:
        pass
    else:
        raw_data = np.delete(raw_data, slice(d_cut), axis=0)
        
    return raw_data
    
def get_data_all(f_path, d_cut=0):
    """
    A function to collect a cetain type of data from VASP output files.
    
    Parameters
    ----------
    f_path : string
        the path to the folder containing the VASP output files (OUTCAR/OSZICAR)
    d_cut : int (optional)
        amount of data to remove from the start of the run
        
    Output
    ----------
    all_data : 2D numpy array
        numpy array containing output data, column order is: P, T, V, E
        
    """
    for i in ['pressure', 'temperature', 'volume', 'energy']:
        temp_data = get_data(f_path=f_path, d_type=i, d_cut=d_cut)
        if i == 'pressure':
            all_data = np.array(temp_data)
        else:
            all_data = np.concatenate((all_data, temp_data), axis=1)
            
    return all_data