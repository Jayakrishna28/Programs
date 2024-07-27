original_dict = {'Ravi': 19, 'Sasi': 22, 'Vamsi': 21, 'Venu': 20}
min_key = min(original_dict, key=original_dict.get)
max_key = max(original_dict, key=original_dict.get)
print(f"Key with minimum value: {min_key}")
print(f"Key with maximum value: {max_key}")