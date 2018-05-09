from test_data_tools.graph import get_test_graph

import pytest


@pytest.fixture(scope='session')
def init_graph():
    graph_name = 'animals'
    graph, client = get_test_graph(graph_name)
    return client


@pytest.fixture(scope='class')
def test_db(request, init_graph):
    """Get a connection pool for an initialized defacto db, with all test data imported."""
    request.cls.client = init_graph
