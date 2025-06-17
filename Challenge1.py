#!/usr/bin/env python3

from collections import Counter

words = [
    "apple", "banana", "apple", "orange", "banana",
    "apple", "kiwi", "banana", "banana", "grape", "kiwi"
]

def most_common_word(words: list[str]) -> tuple[str, int]:

    count = Counter(words)

    return count.most_common(1)[0]

print(most_common_word(words))
