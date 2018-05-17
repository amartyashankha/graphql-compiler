import random


random.seed(0)

CREATE_VERTEX = 'create vertex '
CREATE_EDGE = 'create edge '
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


def create_vertex_statement(vertex_type, fields_dict):
    statement = CREATE_VERTEX + vertex_type
    set_field_clauses = [set_statement(field_name, field_value)
                            for field_name, field_value in fields_dict.iteritems()]
    statement += ' set ' + ', '.join(set_field_clauses)
    return statement


def create_edge_statement(edge_name, from_class, from_name, to_class, to_name):
    statement = CREATE_EDGE + edge_name + ' from {} to {}'
    from_select = select_vertex_statement(from_class, from_name)
    to_select = select_vertex_statement(to_class, to_name)
    return statement.format(from_select, to_select)


def strip_index_from_name(name):
    if not isinstance(name, basestring):
        raise AssertionError(u'Expected string name. Received {}'.format(arg))
    split_name =  name.split(SEPARATOR)
    if len(split_name) != 2:
        raise AssertionError(u'Expected a sting with a single occurrence of {}. Got {}'
                             .format(SEPARATOR, name))
    return split_name


def create_name(base_name, label):
    return base_name + SEPARATOR + label
