import json

json_file_path = "data.json"

with open(json_file_path, 'r') as file:
    data = json.load(file)

item_totals = {}

for item_data in data:
    item_name = item_data.get('item')
    price = item_data.get('price')

    if item_name in item_totals:
        item_totals[item_name] += price
    else:
        item_totals[item_name] = price

print("Individual totals for each item:")
for item, total in item_totals.items():
    print(f"{item}: {total}")

overall_total = sum(item_totals.values())

print(f"\nOverall total: {overall_total}")
