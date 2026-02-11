# data = {
#     "Ram": 85,
#     "Shyam": 92,
#     "Hari": 78,
#     "Sita": 95
#     }

# key = max(data, key=data.get)

# print("Highest value key:", key)
# print("Highest value:", data[key])

data = {
    "Ram": 85,
    "Shyam": 92,
    "Hari": 78,
    "Sita": 95
}

max_key = None
max_value = -1

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Highest value key:", max_key)
print("Highest value:", max_value)
