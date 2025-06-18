classBio.PDB.mmtf.DefaultParser.StructureDecoder
Bases: object

Class to pass the data from mmtf-python into a Biopython data structure.

__init__(self)
Initialize the class.

init_structure(self, total_num_bonds, total_num_atoms, total_num_groups, total_num_chains, total_num_models, structure_id)
Initialize the structure object.

Parameters
total_num_bonds – the number of bonds in the structure

total_num_atoms – the number of atoms in the structure

total_num_groups – the number of groups in the structure

total_num_chains – the number of chains in the structure

total_num_models – the number of models in the structure

structure_id – the id of the structure (e.g. PDB id)

set_atom_info(self, atom_name, serial_number, alternative_location_id, x, y, z, occupancy, temperature_factor, element, charge)
Create an atom object an set the information.

Parameters
atom_name – the atom name, e.g. CA for this atom

serial_number – the serial id of the atom (e.g. 1)

alternative_location_id – the alternative location id for the atom, if present

x – the x coordiante of the atom

y – the y coordinate of the atom

z – the z coordinate of the atom

occupancy – the occupancy of the atom

temperature_factor – the temperature factor of the atom

element – the element of the atom, e.g. C for carbon. According to IUPAC. Calcium is Ca

charge – the formal atomic charge of the atom

set_chain_info(self, chain_id, chain_name, num_groups)
Set the chain information.

Parameters
chain_id – the asym chain id from mmCIF

chain_name – the auth chain id from mmCIF

num_groups – the number of groups this chain has

set_entity_info(self, chain_indices, sequence, description, entity_type)
Set the entity level information for the structure.

Parameters
chain_indices – the indices of the chains for this entity

sequence – the one letter code sequence for this entity

description – the description for this entity

entity_type – the entity type (polymer,non-polymer,water)

set_group_info(self, group_name, group_number, insertion_code, group_type, atom_count, bond_count, single_letter_code, sequence_index, secondary_structure_type)
Set the information for a group.

Parameters
group_name – the name of this group, e.g. LYS

group_number – the residue number of this group

insertion_code – the insertion code for this group

group_type – a string indicating the type of group (as found in the chemcomp dictionary. Empty string if none available.

atom_count – the number of atoms in the group

bond_count – the number of unique bonds in the group

single_letter_code – the single letter code of the group

sequence_index – the index of this group in the sequence defined by the entity

secondary_structure_type – the type of secondary structure used (types are according to DSSP and number to type mappings are defined in the specification)

set_model_info(self, model_id, chain_count)
Set the information for a model.

Parameters
model_id – the index for the model

chain_count – the number of chains in the model

set_xtal_info(self, space_group, unit_cell)
Set the crystallographic information for the structure.

Parameters
space_group – the space group name, e.g. “P 21 21 21”

unit_cell – an array of length 6 with the unit cell parameters in order: a, b, c, alpha, beta, gamma

set_header_info(self, r_free, r_work, resolution, title, deposition_date, release_date, experimnetal_methods)
Set the header information.

Parameters
r_free – the measured R-Free for the structure

r_work – the measure R-Work for the structure

resolution – the resolution of the structure

title – the title of the structure

deposition_date – the deposition date of the structure

release_date – the release date of the structure

experimnetal_methods – the list of experimental methods in the structure

set_bio_assembly_trans(self, bio_assembly_index, input_chain_indices, input_transform)
Set the Bioassembly transformation information. A single bioassembly can have multiple transforms.

Parameters
bio_assembly_index – the integer index of the bioassembly

input_chain_indices – the list of integer indices for the chains of this bioassembly

input_transform – the list of doubles for the transform of this bioassmbly transform.

finalize_structure(self)
Any functions needed to cleanup the structure.

set_group_bond(self, atom_index_one, atom_index_two, bond_order)
Add bonds within a group.

Parameters
atom_index_one – the integer atom index (in the group) of the first partner in the bond

atom_index_two – the integer atom index (in the group) of the second partner in the bond

bond_order – the integer bond order

set_inter_group_bond(self, atom_index_one, atom_index_two, bond_order)
Add bonds between groups.

Parameters
atom_index_one – the integer atom index (in the structure) of the first partner in the bond

atom_index_two – the integer atom index (in the structure) of the second partner in the bond

bond_order – the bond order
