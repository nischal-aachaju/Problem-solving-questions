data = {
    "Ram": 85,
    "Shyam": 92,
    "Hari": 78,
    "Sita": 95
    }

key = max(data, key=data.get)

print("Highest value key:", key)
print("Highest value:", data[key])
