# import json

# file_path = "data.json"
# item_name = "Laptop"

# with open(file_path, 'r') as file:
#     data = json.load(file)

# for item in data:
#     print(item ["item"])

# total_price = 0
# for item_data in data:
#     total_price += item_data.get('price', 0)

# print(total_price)

# prices = []
# for item_data in data:
#     if item_data.get('item') == item_name:
#         prices.append(item_data.get('price'))

# print(prices)

# print(data[0] ["item"])


import json

# Provide the path to your JSON file
json_file_path = 'data.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

item_totals = {}  # Dictionary to store item totals

# Iterate through the list of items
for item_data in data:
    item_name = item_data.get('item')
    price = item_data.get('price')
    
    # Check if the item is already in the dictionary
    if item_name in item_totals:
        item_totals[item_name] += price
    else:
        item_totals[item_name] = price

# Print the individual totals for each item
print("Individual totals for each item:")
for item, total in item_totals.items():
    print(f"{item}: {total}")

# Calculate the overall total
overall_total = sum(item_totals.values())

# Print the overall total
print(f"\nOverall total: {overall_total}")

