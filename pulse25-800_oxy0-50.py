from subprocess import call
from parameters import xml_str, xml_str_sim, xml_str_cell, xml_str_network, xml_str_conf
import xml.dom.minidom as md
import os
import numpy

def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print("Error creating directory.")

i = 0
# elements' steps
#time_step_step = 0.01
#oxygen_necrotic_step = 0.001
#duration_add_tnf_step = 5
#time_add_tnf_step = 50

# Number of parameter files will be generated
#for number in range(1000):
# oxygen_necrotic range: [0,1), with step 0.01
for oxy in numpy.arange(0, 51, 1):
	# time_add_tnf_pulse range: [100, 350), with step 50
	for tnf_pulse in range(25, 825, 25):
		#current_path = os.getcwd()
		#print("The current working directory is: %s" % current_path)
		
		# Create folder where to put the xml file
		run_folder = createFolder('./example_spheroid_TNF_pulse25-800_oxy0-50/run%s/' %i)

		# Each run folder should contain 2 output subfolders: output, microutput
		output_folder = createFolder('./example_spheroid_TNF_pulse25-800_oxy0-50/run%s/output' %i)		
		microutput_folder = createFolder('./example_spheroid_TNF_pulse25-800_oxy0-50/run%s/microutput' %i)			

		# Call the file that creates the desirable xml file
		call(["python", "parameters.py"])

		# The name of the document
		xml_filename = ("./example_spheroid_TNF_pulse25-800_oxy0-50/run%s/parameters.xml" %i)
		
		# Write the generated xml file
		with open(xml_filename, "w") as f:
			f.write(xml_str)				#xml_str: the xml file as a string

		f.close()	

		# The XML file has been generated	


		# ------------------------- Change values for parameters ------------------------- #	

		# Import data by reading the file that just created

		# For simulation root
		sim_root = md.parseString(xml_str_sim)
		# Updated XML file as string
		tmp_updated_xml_str_sim = sim_root.toxml() + "\n"
		updated_xml_str_sim = tmp_updated_xml_str_sim[0:22] + "\n" + tmp_updated_xml_str_sim[22:116] + "\n" + tmp_updated_xml_str_sim[116:]

		# For cell_properties root
		cell_root = md.parseString(xml_str_cell)
		# Update the desirable values
		oxygen_necrotic_element = cell_root.getElementsByTagName('oxygen_necrotic')
		# update the text - value
		oxygen_necrotic_element[0].firstChild.nodeValue = oxy
		tmp_updated_xml_str_cell = cell_root.toxml() + "\n"
		updated_xml_str_cell = "\n" + tmp_updated_xml_str_cell[22:98] + "\n" + tmp_updated_xml_str_cell[98:]

		# For initial configuration root
		initial_conf_root = md.parseString(xml_str_conf)
		# Update the desirable values
		time_add_tnf_element = initial_conf_root.getElementsByTagName('time_add_tnf')
		#time_add_tnf_element[0].firstChild.nodeValue = str(150)		#desirable tnf pulse
		time_add_tnf_element[0].firstChild.nodeValue = tnf_pulse

		# Updated XML file as string
		tmp_updated_xml_str_initial_conf = initial_conf_root.toprettyxml() + "\n"
		updated_xml_str_initial_conf = tmp_updated_xml_str_initial_conf[22:]


		updated_xml_str = updated_xml_str_sim + updated_xml_str_cell + xml_str_network + updated_xml_str_initial_conf


		with open(xml_filename, "w") as f:
			f.write(updated_xml_str)

		f.close()		


		i += 1	
	