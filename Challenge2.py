#!/usr/bin/env python3

matrix = [
    [1,2,3,4],
    [5,6,7,8]
]

print(matrix)

transposed = []

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    columns = int(len(matrix))
    rows = int(len(matrix[0]))
    # print (columns,rows)

    for i in range(rows):
        column = [row[i] for row in matrix]
        transposed.append(column)
    return transposed

print (transpose(matrix))
