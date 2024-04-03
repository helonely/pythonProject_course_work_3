import pytest
from datetime import datetime as dt
from src.utils import (open_json,
                       operations_filtered,
                       operations_sorted,
                       format_date,
                       build_description,
                       mask_operations_from,
                       mask_operations_to
                       )


def test_operations_filtered(json_list):

    expected_result = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    assert operations_filtered(json_list) == expected_result


def test_operations_sorted():
    list_dict = [
        {'id': 1, 'date': '12.11.10'},
        {'id': 2, 'date': '12.10.10'},
        {'id': 3, 'date': '12.09.10'},
        {'id': 4, 'date': '12.08.10'}
    ]

    expected_result = [
        {'id': 1, 'date': '12.11.10'},
        {'id': 2, 'date': '12.10.10'},
        {'id': 3, 'date': '12.09.10'},
        {'id': 4, 'date': '12.08.10'}
    ]
    assert operations_sorted(list_dict) == expected_result


def test_format_date():
    operation = {"date": "2018-03-09T23:57:37.537412"}
    expected_result = "09.03.2018"
    assert format_date(operation) == expected_result

    operation = {"date": "2018-12-24T20:16:18.819037"}
    expected_result = "24.12.2018"
    assert format_date(operation) == expected_result

    operation = {"date": "2022-04-03T15:30:00.123456"}
    expected_result = "03.04.2022"
    assert format_date(operation) == expected_result


def test_mask_operations_from():
    operation = {"from": "МИР 1234 5678 9012 3456"}
    expected_result = "Счет **3456"
    assert mask_operations_from(operation) == expected_result

    # Случай с отсутствующим ключом 'from'
    operation = {}
    expected_result = None
    assert mask_operations_from(operation) == expected_result


def test_mask_operations_to():
    # Тестовый случай с полным номером карты
    operation = {"to": "John Doe 1234 5678 9012 3456"}
    expected_result = 'Счет **3456'
    assert mask_operations_to(operation) == expected_result

    # Тестовый случай с пустым значением 'to'
    operation = {"to": ""}
    expected_result = None
    assert mask_operations_to(operation) == expected_result

    # Тестовый случай с отсутствующим ключом 'to'
    operation = {}
    expected_result = None
    assert mask_operations_to(operation) == expected_result


def test_build_description():

    operation = {"description": "Перевод организации"}
    expected_result = "Перевод организации"
    assert build_description(operation) == expected_result

    # с пустым описанием
    operation = {"description": ""}
    expected_result = ""
    assert build_description(operation) == expected_result

    # с отсутствующим ключом 'description'
    operation = {}
    expected_result = None
    assert build_description(operation) == expected_result


def test_open_json(operations_json):
    # Проверяем, что функция open_json возвращает ожидаемые данные
    assert open_json() == operations_json
