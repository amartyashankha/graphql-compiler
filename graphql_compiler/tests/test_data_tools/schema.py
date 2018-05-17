from glob import glob
from os import path


def apply_sql_update(client, filepath):
    """Apply the specified SQL update file to the client."""
    with open(filepath, 'r') as update_file:
        for line in update_file:
            sanitized = line.strip()
            if not sanitized or sanitized[0] == '#':
                sanitized = None

            if sanitized is None:
                # comment or empty line, ignore
                continue

            client.command(sanitized)


def load_schema(client):
    project_root = path.dirname(path.dirname(path.abspath(__file__)))
    sql_files = glob(path.join(project_root, 'test_data_tools/schema.sql'))
    for filepath in sql_files:
        apply_sql_update(client, filepath)
