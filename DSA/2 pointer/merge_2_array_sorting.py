a = [1, 4, 7]
b = [2, 5, 6]

i = 0
j = 0
merged = []

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

# Add remaining elements
while i < len(a):
    merged.append(a[i])
    i += 1

while j < len(b):
    merged.append(b[j])
    j += 1

print(merged)