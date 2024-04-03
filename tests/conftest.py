import pytest
import json
from pathlib import Path


@pytest.fixture
def operations_json():
    # Use pathlib to construct the path
    file_path = Path('../data/operations.json')
    with open(file_path, encoding='utf-8') as f:
        json_data = json.load(f)
        return json_data


list_dict = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'PENDING'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'FAILED'}
    ]


@pytest.fixture
def json_list():
    return list_dict.copy()
