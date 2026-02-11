# data = {
#     "Ram": 85,
#     "Shyam": 92,
#     "Hari": 78,
#     "Sita": 95
#     }

# key = max(data, key=data.get)

# print("Highest value key:", key)
# print("Highest value:", data[key])

# data = {
#     "Ram": 85,
#     "Shyam": 92,
#     "Hari": 78,
#     "Sita": 95
# }

# max_key = None
# max_value = -1

# for key in data:
#     if data[key] > max_value:
#         max_value = data[key]
#         max_key = key

# print("Highest value key:", max_key)
# print("Highest value:", max_value)

# students = {
#     "S1": {"name": "Ram", "marks": 85},
#     "S2": {"name": "Shyam", "marks": 92},
#     "S3": {"name": "Hari", "marks": 78},
#     "S4": {"name": "Sita", "marks": 95}
# }

# max_student = None
# max_marks = -1

# for sid, info in students.items():
#     if info["marks"] > max_marks:
#         max_marks = info["marks"]
#         max_student = sid

# print("Topper ID:", max_student)
# print("Name:", students[max_student]["name"])
# print("Marks:", max_marks)
