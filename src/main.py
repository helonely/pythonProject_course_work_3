from src.utils import (open_json,
                       operations_filtered,
                       operations_sorted,
                       format_date,
                       build_description,
                       mask_operations_from,
                       mask_operations_to
                       )


# Наш чистый json
data_list = open_json()

# Наш отфильтрованный список(словарей)
operations = operations_filtered(data_list)

# Берем первые 5 транзакции т.к. мы использовали reverse=True
operation_sort = operations_sorted(operations)[:5]

# основная логика
for i in operation_sort:
    date_output = format_date(i)
    description_output = build_description(i)
    print(f"{date_output} {description_output}")

    amount_ = i['operationAmount']['amount']
    currency_ = i['operationAmount']['currency']['name']
    musk_from = mask_operations_from(i)
    musk_to = mask_operations_to(i)
    print(f'{musk_from} -> {musk_to}')
    print(f"{amount_} {currency_} ")
    print()
