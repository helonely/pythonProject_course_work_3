import json
from datetime import datetime as dt
from pathlib import Path


def open_json():
    """
    Открываем json на чтение
    """
    file_path = Path(__file__).parent / "../data/operations.json"
    with open(file_path, encoding='utf-8') as f:
        json_list = json.load(f)
    return json_list


def operations_filtered(json_list: list[dict]) -> list[dict]:
    """
    filter by completed operations
    :param json_list:
    :return:filtered list
    """
    list_filtered = []
    for i in json_list:
        if i.get('state') == 'EXECUTED':
            list_filtered.append(i)
    return list_filtered


def operations_sorted(list_filtered: list[dict]) -> list[dict]:
    """
    sort by completed operations and reverse list[dict]
    :param list_filtered:
    :return:sorted list
    """
    list_filtered_revert = sorted(list_filtered, key=lambda x: x['date'], reverse=True)
    return list_filtered_revert


def mask_operations_from(operation):
    """
    masking sender operations
    :param operation:
    :return: mask operation from
    """
    operation_from = operation.get('from')
    if operation_from:
        parts_split = operation_from.split(' ')
        card_numbers = parts_split[-1]
        if len(card_numbers) == 16:
            mask_card_numbers = f'{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}'
            return f'{" ".join(parts_split[:-1])} {mask_card_numbers}'
        else:
            return f'Счет **{card_numbers[-4:]}'


def mask_operations_to(operation):
    """
    masking receiver operations
    :param operation:
    :return: musk operation to
    """
    operation_to = operation.get('to')
    if operation_to:
        parts_split = operation_to.split(' ')
        card_numbers = parts_split[-1]
        if len(card_numbers) == 16:
            mask_card_numbers = f'{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}'
            return f'{" ".join(parts_split[:-1])} {mask_card_numbers}'
        else:
            return f'Счет **{card_numbers[-4:]}'


def format_date(operation):
    """
    change date format
    :param operation:
    :return: date d,m,y formatted
    """
    build_date = operation['date']
    format_build_date = dt.strptime(build_date, '%Y-%m-%dT%H:%M:%S.%f')
    return format_build_date.strftime('%d.%m.%Y')


def build_description(operation):
    """
    build description
    :param operation:
    :return: description string
    """
    description = operation.get('description')
    return description
