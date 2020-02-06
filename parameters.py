from xml.dom import minidom
import os
import random

# root: simulation
simulation = minidom.Document()
comment = simulation.createComment(' Global parameters of the simulation (time parameters are in min, distance in microns) ')
simulation.appendChild(comment)
xml = simulation.createElement('simulation')
simulation.appendChild(xml)

# simulation's children (with comments above each attribute)
simulationChild = simulation.createElement('time_step')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 0.02 '))
# If you want to randomly generate this value, comment the above line and comment out the two following ones.
#randomGenValue = round(random.uniform(0.001,1), 3)
#simulationChild.appendChild(simulation.createTextNode(str(randomGenValue)))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('mechanics_time_step')
comment = simulation.createComment(' Time scale of motion, cell volume changes ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 0.1 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('cell_cycle_time_step')
comment = simulation.createComment(' Cell cycle time scale, change of cell phase ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 2 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('maximal_time')
comment = simulation.createComment(' Time to simulate, 24 h ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 1440 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('output_interval')
comment = simulation.createComment(' Write output file of cells positions every 30 min ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 30 '))
xml.appendChild(simulationChild)

# Depends on the PC's architecture (16 for their PC, 4 for my PC)
simulationChild = simulation.createElement('number_of_threads')
comment = simulation.createComment(' parallelization with openmp ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 2 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('mode_cell_cycle')
comment = simulation.createComment(' parallelization with openmp ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 1 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('output_densities')
comment = simulation.createComment(' To use with a boolean network implementation ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 450 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('write_passive_cells')
comment = simulation.createComment(' parallelization with openmp ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 0 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('minimum_voxel_size')
comment = simulation.createComment(' Discretization size of the microenvironment grid (BioFVM) ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 15 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('bounding_box_xmin')
comment = simulation.createComment(' Dimensions of the simulated space ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' -500 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('bounding_box_xmax')
simulationChild.appendChild(simulation.createTextNode(' 500 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('bounding_box_ymin')
simulationChild.appendChild(simulation.createTextNode(' -500 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('bounding_box_ymax')
simulationChild.appendChild(simulation.createTextNode(' 500 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('bounding_box_zmin')
simulationChild.appendChild(simulation.createTextNode(' -500 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('bounding_box_zmax')
simulationChild.appendChild(simulation.createTextNode(' 500 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('number_of_densities')
comment = simulation.createComment(' Densities to simulate in the microenvironment ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 2 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('density_0')
simulationChild.appendChild(simulation.createTextNode(' oxygen '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('density_1')
simulationChild.appendChild(simulation.createTextNode(' tnf '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('dirichlet_boundary')
comment = simulation.createComment(' Constant injection of densities on the external boundaries ')
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 0 '))
xml.appendChild(simulationChild)

simulationChild = simulation.createElement('write_ratio_voxels')
comment = simulation.createComment(" When output densities files, don't write all the voxels values, but randomly selected ones ")
xml.appendChild(comment)
simulationChild.appendChild(simulation.createTextNode(' 0.4 '))
xml.appendChild(simulationChild)

# Return a pretty-printed version of the document. By default the encoding is UTF-8.
# Return the XML as a string 
xml_str_sim = simulation.toprettyxml(indent = "\t")


# root: cell_properties
cell_properties = minidom.Document()
decl = cell_properties.toxml()
comment = cell_properties.createComment(' Properties of the first cell line, common to all cells in this type ')
cell_properties.appendChild(comment)
xml = cell_properties.createElement('cell_properties')
cell_properties.appendChild(xml)

# cell_properties' children (with comments above each attribute)
cell_propertiesChild = cell_properties.createElement('polarity_coefficient')
comment = simulation.createComment(' How much polarized by default ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0.1 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('motility_amplitude_min')
comment = simulation.createComment(' Motility parameters ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0.01 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('motility_amplitude_max')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0.01 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('mode_motility')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 1 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('homotypic_adhesion_min')
comment = simulation.createComment(' Cell-cell adhesion and repulsion coefficients ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 2 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('homotypic_adhesion_max')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 2 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('heterotypic_adhesion_min')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 2 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('heterotypic_adhesion_max')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 2 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('max_interaction_factor')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 1.2 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('cell_cell_repulsion')
comment = simulation.createComment(' Cell default minimal volumes (after division) ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 10 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('cell_radius')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 8.413 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('nucleus_radius')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 5.052 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('fluid_fraction')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0.75 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('solid_nuclear')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 135 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('solid_cytoplasmic')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 486 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('cytoplasmic_nuclear_fraction')
comment = simulation.createComment(' diffusion time scale ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 3.6 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('phenotype_number')
comment = simulation.createComment(' Use default preset phenotype parameters for cell phases ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 3 '))
xml.appendChild(cell_propertiesChild)

# Variable value
cell_propertiesChild = cell_properties.createElement('oxygen_necrotic')
comment = simulation.createComment(' Cell parameters dependant on ECM densities interaction ')
xml.appendChild(comment)
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('oxygen_critical')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('oxygen_no_proliferation')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('oxygen_hypoxic')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 40 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('oxygen_reference')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 40 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('oxygen_saturation')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 40 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('initial_uptake_rate')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0.0025 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('protein_threshold')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 2.8e-05 '))
xml.appendChild(cell_propertiesChild)

cell_propertiesChild = cell_properties.createElement('secretion_rate')
cell_propertiesChild.appendChild(cell_properties.createTextNode(' 0.1 '))
xml.appendChild(cell_propertiesChild)

# Return a pretty-printed version of the document. By default the encoding is UTF-8.
# Return the XML as a string
xml_str_cell = cell_properties.toprettyxml()[len(decl):]	# use [len(decl):] to avoid version's revision


# root: network
network = minidom.Document()
decl = network.toxml()
comment = network.createComment(' Parameters related to boolean network computation ')
network.appendChild(comment)
xml = network.createElement('network')
network.appendChild(xml)

# network's children (with comments above each attribute)
networkChild = network.createElement('network_update_step')
networkChild.appendChild(network.createTextNode(' 10 '))
xml.appendChild(networkChild)

# Return a pretty-printed version of the document. By default the encoding is UTF-8.
# Return the XML as a string
xml_str_network = network.toprettyxml()[len(decl):]	# use [len(decl):] to avoid version's revision


# root: initial_configuration
initial_configuration = minidom.Document()
decl = initial_configuration.toxml()
comment = initial_configuration.createComment(' Initial configuration of the simulation and injection management ')
initial_configuration.appendChild(comment)
xml = initial_configuration.createElement('initial_configuration')
initial_configuration.appendChild(xml)

# initial_configuration's children (with comments above each attribute)
initial_configurationChild = initial_configuration.createElement('load_cells_from_file')
initial_configurationChild.appendChild(initial_configuration.createTextNode(' init.txt '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('membrane_shape')
initial_configurationChild.appendChild(initial_configuration.createTextNode(' sphere '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('membrane_length')
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 470 '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('time_passive_cells')
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 1500 '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('oxygen_concentration')
comment = initial_configuration.createComment(' concentration of available oxygen ')
xml.appendChild(comment)
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 40 '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('tnf_concentration')
comment = initial_configuration.createComment(' concentration of injected TNF ')
xml.appendChild(comment)
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 0.5 '))
xml.appendChild(initial_configurationChild)

# tnf window
initial_configurationChild = initial_configuration.createElement('duration_add_tnf')
comment = initial_configuration.createComment(' Duration of the injection > maximal time then continuous ')
xml.appendChild(comment)
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 10 '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('time_remove_tnf')
comment = initial_configuration.createComment(' If wash-off TNF at some time or not ')
xml.appendChild(comment)
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 80000 '))
xml.appendChild(initial_configurationChild)

# Variable value
# Interval time between 2 tnf pulses
initial_configurationChild = initial_configuration.createElement('time_add_tnf')
comment = initial_configuration.createComment(" If doesn't add TNF from the begining, at what time ")
xml.appendChild(comment)
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 80000 '))
xml.appendChild(initial_configurationChild)

initial_configurationChild = initial_configuration.createElement('mode_injection')
comment = initial_configuration.createComment(' Modes of injection: 0 microfluidic-like (everywhere), 1 spheroid-like (at the boundaries) ')
xml.appendChild(comment)
initial_configurationChild.appendChild(initial_configuration.createTextNode(' 1 '))
xml.appendChild(initial_configurationChild)

# Return a pretty-printed version of the document. By default the encoding is UTF-8.
# Return the XML as a string
xml_str_conf = initial_configuration.toxml()[len(decl):]	# use [len(decl):] to avoid version's revision

# Concatenate strings to a single XML
xml_str = xml_str_sim + xml_str_cell + xml_str_network + xml_str_conf
