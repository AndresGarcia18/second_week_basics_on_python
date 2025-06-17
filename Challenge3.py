#!/usr/bin/env python3

dictionaries = [
    {"name": "Carlos", "age": 25},
    {"name": "Ana", "age": 30},
    {"name": "Felipe", "age": 22},
    {"name": "Matias", "age": 25},
    {"name": "Carlos", "age": 31},
    {"name": "Sofia", "age": 22}
]

def sort_by_key(data: list[dict], key: str, secondary_key = '') -> list[dict]:
    
    if secondary_key:
        data = sorted(data, key=lambda x: (x[key], x[secondary_key]))
    else:
        data = sorted(data, key=lambda x: (x[key]))

    return data

print (sort_by_key(dictionaries, "name", "age"))
