import json
a='{ "a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print(a)
b=json.loads(a)
print(b)