import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as jr:
        data = json.loads(jr.read())

    json_dict = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    data['orders'].append(json_dict)

    with open('orders.json', 'w') as jw:
        json.dump(data, jw, indent=4)

write_order_to_json(1,1,1,1,1)
