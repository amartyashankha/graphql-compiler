import random

from .species import SPECIES_LIST
from .utils import (create_edge_statement, create_name, create_vertex_statement, get_uuid,
                    strip_index_from_name)


NUM_INITIAL_ANIMALS = 5
NUM_GENERATIONS = 10
NUM_PARENTS = 3


def _create_animal_statement(animal_name):
    """Return a SQL statement to create an animal vertex."""
    fields_dict = {'name': animal_name, 'uuid': get_uuid()}
    return create_vertex_statement('Animal', fields_dict)


def _create_animal_parent_of_statement(from_name, to_name):
    """Return a SQL statement to create an Animal_ParentOf edge."""
    return create_edge_statement('Animal_ParentOf', 'Animal', from_name, 'Animal', to_name)


def _create_entity_related_statements(from_name, to_name):
    """Return list of two SQL statements to create a bidirectional Entity_Related edge."""
    forward_edge = create_edge_statement('Entity_Related', 'Animal', from_name, 'Animal', to_name)
    reverse_edge = create_edge_statement('Entity_Related', 'Animal', to_name, 'Animal', from_name)
    return [forward_edge, reverse_edge]


def _create_animal_of_species_statement(from_name, to_name):
    """Return a SQL statement to create an Animal_OfSpecies edge."""
    return create_edge_statement('Animal_OfSpecies', 'Animal', from_name, 'Species', to_name)


def _get_initial_animal_generators(species_name, current_animal_names):
    """Return a list of SQL statements to create initial animals for a given species."""
    generator_list = []
    for index in range(NUM_INITIAL_ANIMALS):
        animal_name = create_name(species_name, str(index))
        current_animal_names.append(animal_name)
        generator_list.append(_create_animal_statement(animal_name))
    return generator_list


def _get_new_parents(current_animal_names, previous_parent_sets, num_parents):
    """Return a list of `num_parents` parent names that is not present in `previous_parent_sets`."""
    while True:
        new_parent_names = frozenset(random.sample(current_animal_names, num_parents))
        # Duplicating a set of parents could result in Animals with the same names.
        # This would invalidate unique selection of Animals by name.
        if new_parent_names not in previous_parent_sets:
            return new_parent_names


def _create_animal_from_parent(parent_names, species_name):
    """Return a list of statements to create an animal (and its edges) from a list of parents."""
    generator_list = []
    new_animal_names = []
    parent_indices = [
        index for _, index in [
            strip_index_from_name(parent_name)
                       for parent_name in parent_names
        ]
    ]

    new_label = '(' + ''.join(parent_indices) + ')'
    new_animal_name = create_name(species_name, new_label)
    new_animal_names.append(new_animal_name)
    generator_list.append(_create_animal_statement(new_animal_name))

    # Create Animal_ParentOf edges
    for parent_name in parent_names:
        new_edge = _create_animal_parent_of_statement(new_animal_name, parent_name)
        generator_list.append(new_edge)

    # Create Entity_Related edges
    for parent_name in parent_names:
        new_edges = _create_entity_related_statements(new_animal_name, parent_name)
        generator_list.extend(new_edges)

    return generator_list, new_animal_names


def get_animal_generators():
    """Return a list of SQL statements to create animal vertices and their corresponding edges."""
    generator_list = []
    species_to_names = {}
    previous_parent_sets = set()

    for species_name in SPECIES_LIST:
        current_animal_names = []
        species_to_names[species_name] = current_animal_names
        generator_list.extend(_get_initial_animal_generators(species_name, current_animal_names))

        for _ in range(NUM_GENERATIONS):
            new_parent_names = _get_new_parents(current_animal_names, previous_parent_sets)
            previous_parent_sets.add(parent_names)

            new_animal_generator_list, new_animal_names = _create_animal_from_parent(
                parent_names, species_name)
            generator_list.extend(new_animal_generator_list)
            current_animal_names.extend(new_animal_names)

        for animal_name in current_animal_names:
            generator_list.append(_create_animal_of_species_statement(animal_name, species_name))

    return generator_list
