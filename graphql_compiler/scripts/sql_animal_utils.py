import random

from .sql_species_utils import SPECIES_LIST
from .sql_utils import (create_edge_statement, create_name, create_vertex_statement, get_uuid,
                        strip_index_from_name)


random.seed(0)

NUM_INITIAL_ANIMALS = 5
NUM_GENERATIONS = 10
NUM_PARENTS = 3


def create_animal_statement(animal_name):
    fields_dict = {'name': animal_name, 'uuid': get_uuid()}
    return create_vertex_statement('Animal', fields_dict)


def create_animal_parent_of_statement(from_name, to_name):
    return create_edge_statement('Animal_ParentOf', 'Animal', from_name, 'Animal', to_name)


def create_animal_of_species_statement(from_name, to_name):
    return create_edge_statement('Animal_OfSpecies', 'Animal', from_name, 'Species', to_name)


def get_initial_animal_generators(species_name, current_animal_names):
    generator_list = []
    for index in range(NUM_INITIAL_ANIMALS):
        animal_name = create_name(species_name, str(index))
        current_animal_names.append(animal_name)
        generator_list.append(create_animal_statement(animal_name))
    return generator_list


def get_animal_generators():
    generator_list = []
    species_to_names = {}

    for species_name in SPECIES_LIST:
        current_animal_names = []
        species_to_names[species_name] = current_animal_names
        generator_list.extend(get_initial_animal_generators(species_name, current_animal_names))

        for _ in range(NUM_GENERATIONS):
            parent_names = random.sample(current_animal_names, NUM_PARENTS)
            parent_indices = [index for _, index in
                                 [strip_index_from_name(parent_name)
                                     for parent_name in parent_names]]
            new_label = '(' + ''.join(parent_indices) + ')'
            new_animal_name = create_name(species_name, new_label)
            current_animal_names.append(new_animal_name)
            generator_list.append(create_animal_statement(new_animal_name))
            for parent_name in parent_names:
                generator_list.append(create_animal_parent_of_statement(new_animal_name, parent_name))

        for animal_name in current_animal_names:
            generator_list.append(create_animal_of_species_statement(animal_name, species_name))

    return generator_list
