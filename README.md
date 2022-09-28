# VASP_block

### Introduction to VASP_block

VASP_block is a terminal program written in python, which allows users to extract data from VASP output files (OUTCAR/OSZICAR) and reblock the data to gain meaningful statistical insights. Currently VASP_block can extract:

-	Pressure (GPa)
-	Temperature (K)
-	Volume (A3)
-	Total Energy (eV)

This allows processing of the fundamental state properties and covers most types of VASP calculation (NPT, NVE, etc.). Other properties (e.g. magnetism) can easily be added to the current framework. 

### Why this program was written

Most VASP calculations returns data in time series (where time is equivalent to ionic steps). However, this data is generally correlated, meaning the current data point is influenced by the previous data. If mean averages and errors are obtained from the raw data, these would not be statistically meaningful. Currently, block averaging has become the standard tool to deal with this in the computational chemistry field. The mathematics for this come from papers such as Flyvbjerg and Petersen (1998) and python modules, such as pyblock (https://pypi.org/project/pyblock/), implement this. The rational for writing this program are as follows:

-	Currently users find themselves running data through many code snippets, and using many different modules to process the data, a more direct approach is beneficial.
-	VASP_block uses only NumPy (https://numpy.org/) and matplotlib (https://matplotlib.org/stable/index.html) as external modules, which most users already have installed.
-	Most VASP jobs are ran on external servers (such as supercomputing facilities), if the user wants to process the data on the server, installing additional modules can be difficult due to admin rights (given VASP_block requires 2 common modules users can now process data on servers without needing to download and upload data) 
-	Although blocking modules exists (and users are encouraged to check out pyblock) these programs are general, the blocking used in VASP_block has been written for VASP data and therefore is more stable when handling VASP data

The program has been written as a terminal program, this decision was taken as most VASP work is carried out in a terminal environment (running jobs on servers). Therefore, all VASP users are familiar with a terminal environment and many wish to process all their data in one place (something that has been hard to do previously). 
For users wishing to write their own python scripts, or use the program to build a data pipeline, the main aspect of the program are written in functions (data extraction, blocking, plotting) and therefore python users will find it easy to integrate the code into python scripts of their own. 

## How the program works

In a terminal environment run the program `VASP_block.py`. This will then ask for inputs from the user, these are:
-	`Enter the file path:` Give the program the location of the folder where the data is data (OUTCAR/OSZICAR files), e.g. C:/Users/bob/work/data/VASP/run_1/
-	`Enter the amount of steps to remove from the beginning of the data:` It is common for VASP calculations to include steps at the beginning that need to be removed (e.g. due to a change in cell volume). If no steps are needed to be removed, simply enter `0`
-	`Save CSV?` The optimal blocks for the state properties will be printed, but can also be saved as a separate CSV file. Answer `yes`/`no`
-	`Enter CSV file name` If a CSV is being save, enter the file name to save is as, this will be a `.CSV` file and will be saved in the same directory as the program is being ran from
-	Like wise the plot can be saved (again `yes`/`no`) and a file name is needed if this is being saved too

After the inputs the program will extract the data for the state properties. It will then reblock the data, starting from a block size of 1 until the optimal block is found. At which point a table will be printed giving the user the values for the optimal block for each state variable:

`--------------------------------Optimal Blocking Statistics-------------------------------` <br />
`                | Block Size      | Data per Block  | Mean            | Standard Error    ` <br />
`------------------------------------------------------------------------------------------` <br />
`Pressure        | 26.0            | 360.0           | -0.062          | 0.204             ` <br />
`Temperature     | 25.0            | 375.0           | 3000.322        | 25.273            ` <br />
`Volume          | 3.0             | 4500.0          | 2299.97         | 0.0               ` <br />
`Total Energy    | 27.0            | 346.0           | -482.867        | 0.017             ` <br />

Once the table is printed in the terminal, a plot is produced showing the data, mean and 1 standard deviation:

![output](https://user-images.githubusercontent.com/95185273/192791559-87fe378b-388e-4c49-95b7-9320424bd091.png)

Plotting has been optimized for the subplot shown above, however can be easily changed using the matplotlib (https://matplotlib.org/stable/index.html) documentation to suit the users needs. 

### Final comments 
I hope you find some use for this program and it helps tackle some issues I was facing which made me write it in the first place. Please get in touch with any comments (my email is on my profile). 
