# Insert the init.txt file in each simulation's folder (run_i folder). # 
from shutil import copy2

for i in range(0, 1632, 1):
	copy2('./example_spheroid_TNF_pulse25-800_oxy0-50/init.txt', './example_spheroid_TNF_pulse25-800_oxy0-50/run%s' %i)
