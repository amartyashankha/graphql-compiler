# Copyright 2017 Kensho Technologies, LLC.
from snapshottest import TestCase

from graphql import GraphQLID, GraphQLString
import six
import pytest

from .. import test_input_data
from ... import graphql_to_match
from ..test_helpers import get_schema


def execute_graphql(schema, test_data, client):
    """Assert that the GraphQL input generates all expected MATCH and Gremlin data."""
    if test_data.type_equivalence_hints:
        # For test convenience, we accept the type equivalence hints in string form.
        # Here, we convert them to the required GraphQL types.
        schema_based_type_equivalence_hints = {
            schema.get_type(key): schema.get_type(value)
            for key, value in six.iteritems(test_data.type_equivalence_hints)
        }
    else:
        schema_based_type_equivalence_hints = None

    parameters = {}
    result = graphql_to_match(schema, test_data.graphql_input, parameters,
                              type_equivalence_hints=schema_based_type_equivalence_hints)

    rows = [row.oRecordData for row in client.command(result.query)]
    return rows


class OrientdbMatchQueryTests(TestCase):

    def setUp(self):
        """Initialize the test schema once for all tests, and disable max diff limits."""
        self.maxDiff = None
        self.schema = get_schema()

    @pytest.mark.usefixtures('test_db')
    def test_immediate_output(self):
        test_data = test_input_data.immediate_output()

        rows = execute_graphql(self.schema, test_data, self.client)

        self.assertMatchSnapshot(rows)
