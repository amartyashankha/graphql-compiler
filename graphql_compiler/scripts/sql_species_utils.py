import random

from .sql_utils import create_edge_statement, create_vertex_statement, get_uuid


random.seed(0)

SPECIES_LIST = [
    'Nazgul',
    'Pteranodon',
    'Dragon',
    'Hippogriff',
]


def create_species_statement(species_name):
    fields_dict = {'name': species_name, 'uuid': get_uuid()}
    return create_vertex_statement('Species', fields_dict)


def get_species_generators():
    generator_list = []
    for species_name in SPECIES_LIST:
        generator_list.append(create_species_statement(species_name))

    return generator_list
