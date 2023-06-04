import json

"""Прятчет циферки карт, заменяя их на звездочки. """
def hide_ciferki(card_info):
    if card_info.startswith('Visa Classic') or card_info.startswith('Maestro'):
        card_info = card_info.split()
        number = card_info[-1]
        hide_number = number[:6] + '*'*2 + number[-4:]

        return ' '.join(card_info[:-1]+[hide_number])
    elif card_info.startswith('Счет'):
        card_info = card_info.split()
        number = card_info[-1]
        hide_number = '*' * 2 + number[-4:]


        return ' '.join(card_info[:-1] + [hide_number])

"""изменяет дату на читабельную"""
def change_data(date):

    return '.'.join(date[:10].split('-')[::-1])
"""выводит данные в читабельном виде"""
def show_trans(operation):

    output = f"""{change_data(operation['date'])} Перевод организации 
    \n Visa Platinum {hide_ciferki(operation['from'])} -> {hide_ciferki(operation['to'])} 
    {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}. """

    print(output)

"""Основная функция. Загружает данные, читает и выводит последние 5."""
def main():
    with open("data/operations.json", encoding='utf-8') as file:
        data = json.load(file)

    data = filter(lambda x: x.get('state') == 'EXECUTED' and x.get('from'), data)
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)

    for operation in data[:5]:
        show_trans(operation)

if __name__ == "__main__":
    main()
