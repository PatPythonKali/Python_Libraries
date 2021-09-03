from collections import defaultdict

# Regular Dict
d = {'a':10}
# print(d['Wrong'])

# Defaultdict
x = defaultdict(lambda: 0)
x['correct'] = 100

# Initialized
print(x['correct'])

# Not Initialized and NO Value
print(x['wrong'])