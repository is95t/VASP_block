

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from functions.get_data import get_data_all
from functions.blocking import block_data
from functions.plotting import plot_data_sub
from functions.print_tab import print_data

print('Enter the file path:')
file_path = input()
print()
print('Enter the amount of steps to remove from the beginning of the data:')
d_cut = input()
print()
print('Save CSV? (yes/no):')
csv_save = input()
print()
if csv_save == 'yes':
    print('Enter csv file name:')
    csv_name = input()
    print()
print('Save plot? (yes/no):')
plot_save = input()
print()
if plot_save == 'yes':
    print('Enter plot file name:')
    plot_name = input()
    print()
print('Reblocking data - please wait...')
print()

out_data = get_data_all(file_path, d_cut=int(d_cut))
opt_blocks = np.empty(shape=0)
for i in range(0, out_data.shape[1]):
    data_temp = out_data[:, i]
    b_opt = block_data(data_temp)
    if i == 0:
        opt_blocks = np.append(opt_blocks, b_opt)
    else:
        opt_blocks = np.vstack([opt_blocks, b_opt])
print_blocks = np.round(opt_blocks, 3)
col_lab = np.array(['Block Size', 'Data per Block', 'Mean', 'Standard Error'])
row_lab = np.array([[''],
                    ['Pressure'],
                    ['Temperature'],
                    ['Volume'],
                    ['Total Energy']])
print_blocks = np.vstack([col_lab, print_blocks])
print_blocks = np.hstack([row_lab, print_blocks])
print_data(print_blocks)
print()
if csv_save == 'yes':
    np.savetxt(csv_name + '.csv', print_blocks, fmt='%s', delimiter=',')
    print('CSV saved as ' + csv_name + '.csv')
    print()
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 7))
plot_data_sub(out_data[:, 0], opt_blocks[0, :], ax=axs[0, 0], d_type='pressure')
plot_data_sub(out_data[:, 1], opt_blocks[1, :], ax=axs[0, 1], d_type='temperature')
plot_data_sub(out_data[:, 2], opt_blocks[2, :], ax=axs[1, 0], d_type='volume')
plot_data_sub(out_data[:, 3], opt_blocks[3, :], ax=axs[1, 1], d_type='energy')
legend_elements = [Line2D([0], [0], color='darkgrey', label='Data'),
                  Line2D([0], [0], color='red', label='Mean Average'),
                   Line2D([0], [0], linestyle='--', color='red', label='1 Standard Deviation'),
                   Line2D([0], [0], linestyle='-.', color='red', label='95% Confidence Interval'),]
fig.legend(handles=legend_elements, loc='upper right')
fig.suptitle('Time Evolution of State Variables', fontsize=20)
fig.tight_layout()
if plot_save == 'yes':
    fig.savefig(plot_name + '.png', dpi=500, bbox_inches='tight')
    print('Plot saved as ' + plot_name + '.png')
plt.show()
