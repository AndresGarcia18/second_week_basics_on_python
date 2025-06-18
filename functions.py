from collections import Counter
from typing import Generator
from itertools import combinations
import os
from datetime import datetime

def most_common_word(words: list[str]) -> tuple[str, int]:
    
    count = Counter(words)

    return count.most_common(1)[0]

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    
    columns = int(len(matrix))
    rows = int(len(matrix[0]))
    transposed = []

    # print (columns,rows)

    for i in range(rows):
        column = [row[i] for row in matrix]
        transposed.append(column)

    return transposed

def sort_by_key(data: list[dict], key: str, secondary_key = '') -> list[dict]:

    if secondary_key:
        data = sorted(data, key=lambda x: (x[key], x[secondary_key]))
    else:
        data = sorted(data, key=lambda x: (x[key]))

    return data

def prime_generator() -> Generator[int, None, None]:

    generated = 2

    while True:

        for i in range(2, int(generated**0.5) + 1):
            if generated % i == 0:
                break
        else:
            yield generated

        generated += 1

def find_combinations(nums: list[int]) -> list[tuple[int, int, int]]:
    
    return list(combinations(nums, 3))

def file_stats(filepath: str) -> dict[str, int]:
    
    dict = {"lines": 0, "words": 0, "characters": 0}
    
    with open(filepath, 'r', encoding='utf-8') as f:

        for line in f:
            dict["lines"] += 1
            dict["words"] += len(line.split())
            dict["characters"] += len(line)

    return dict

def create_and_list_dir(dir_path: str) -> str:
    
    os.makedirs(dir_path, exist_ok=True)
    
    file_list = []
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), dir_path)
            file_list.append(rel_path)
            
    if file_list:
        files_str = "\n".join(file_list)
    else:
        files_str = "Folder empty"

    return f"\nDirectory created: {dir_path}\n{files_str}"

def date_difference(date1: str, date2: str) -> int:

    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    return abs((date2 - date1).days)