import random

from .sql_animal_utils import (create_animal_of_species_statement,
                               create_animal_parent_of_statement, create_animal_statement,
                               get_animal_generators)
from .sql_species_utils import create_species_statement, get_species_generators
from .sql_utils import (create_edge_statement, create_vertex_statement, get_uuid,
                        select_vertex_statement, set_statement, strip_index_from_name)


random.seed(0)


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
