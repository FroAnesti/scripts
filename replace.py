# Filtering the generated data.                                                                                #
# At the grid of TUC, inside the cells_xxx.txt file an extra value (-1-1') is generated and has to be removed. #

import fileinput
import os


for NO in range(0, 1200, 1):
	cwd = os.getcwd()
	print(cwd)
	# This will change your current working directory
	os.chdir("/home/eanesti/PhysiBoSS/examples/Mine/example_spheroid_TNF_pulse100-300_dur_conc_oxy/run%s/output" %NO)
	for time in range(0, 1470, 30):
		with fileinput.FileInput('cells_%05d.txt' %time, inplace=True) as file:
			#print('cells_%05d.txt' %time)
			for line in file:
				print(line.replace('-1-1;','' ), end='')
