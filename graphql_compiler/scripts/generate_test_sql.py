import random

random.seed(0)

SPECIES_LIST = [
    'Nazgul',
    'Pteranodon',
    'Dragon',
    'Hippogriff',
]
CREATE_VERTEX = 'create vertex '
CREATE_EDGE = 'create edge '
NUM_INITIAL_ANIMALS = 5
NUM_GENERATIONS = 10
NUM_PARENTS = 3
SEPARATOR = '__'

def get_uuid():
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(32)])
    uuid_substrings = [
        random_digits[:8],
        random_digits[8:12],
        random_digits[12:16],
        random_digits[16:20],
        random_digits[20:]
    ]
    return '-'.join(uuid_substrings)


def select_vertex_statement(vertex_type, name):
    template = '(select from {vertex_type} where name = \'{name}\')'
    args = {'vertex_type': vertex_type, 'name': name}
    return template.format(**args)


def set_statement(field_name, field_value):
    if not isinstance(field_name, basestring):
        raise AssertionError(u'Expected string field_name. Received {}'.format(arg))
    if not isinstance(field_value, basestring):
        raise AssertionError(u'Expected string field_value. Received {}'.format(arg))
    template = '{} = \'{}\''
    return template.format(field_name, field_value)


def get_vertex_statement(vertex_type, fields_dict):
    statement = CREATE_VERTEX + vertex_type
    set_field_clauses = [set_statement(field_name, field_value)
                            for field_name, field_value in fields_dict.iteritems()]
    statement += ' set ' + ', '.join(set_field_clauses)
    return statement


def get_animal_statement(animal_name):
    fields_dict = {'name': animal_name, 'uuid': get_uuid()}
    return get_vertex_statement('Animal', fields_dict)


def get_edge_statement(edge_name, from_class, from_name, to_class, to_name):
    statement = CREATE_EDGE + edge_name + ' from {} to {}'
    from_select = select_vertex_statement(from_class, from_name)
    to_select = select_vertex_statement(to_class, to_name)
    return statement.format(from_select, to_select)

def get_animal_parent_of_statement(from_name, to_name):
    return get_edge_statement('Animal_ParentOf', 'Animal', from_name, 'Animal', to_name)


def get_animal_of_species_statement(from_name, to_name):
    return get_edge_statement('Animal_OfSpecies', 'Animal', from_name, 'Species', to_name)


def strip_index_from_name(name):
    if not isinstance(name, basestring):
        raise AssertionError(u'Expected string name. Received {}'.format(arg))
    split_name =  name.split(SEPARATOR)
    if len(split_name) != 2:
        raise AssertionError(u'Expected a sting with a single occurrence of {}. Got {}'
                             .format(SEPARATOR, name))
    return split_name


def get_species_generators():
    generator_list = []
    for species_name in SPECIES_LIST:
        statement = CREATE_VERTEX + 'Species set '
        statement += set_statement('name', species_name) + ','
        statement += set_statement('uuid', get_uuid())
        generator_list.append(statement)

    return generator_list


def get_initial_animal_generators(species_name, current_animal_names):
    generator_list = []
    for index in range(NUM_INITIAL_ANIMALS):
        animal_name = species_name + SEPARATOR + str(index)
        current_animal_names.append(animal_name)
        generator_list.append(get_animal_statement(animal_name))
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
            new_animal_name = species_name + SEPARATOR + '(' + ''.join(parent_indices) + ')'
            current_animal_names.append(new_animal_name)
            generator_list.append(get_animal_statement(new_animal_name))
            for parent_name in parent_names:
                generator_list.append(get_animal_parent_of_statement(new_animal_name, parent_name))

        for animal_name in current_animal_names:
            generator_list.append(get_animal_of_species_statement(animal_name, species_name))

    return generator_list


def main():
    sql_generators = [
        get_species_generators,
        get_animal_generators,
    ]
    sql_generator_strings = []
    for generator in sql_generators:
        sql_generator_strings.extend(generator())

    return '\n'.join(sql_generator_strings)


if __name__ == '__main__':
    print main()
