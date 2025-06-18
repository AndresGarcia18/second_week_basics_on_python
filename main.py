#!/usr/bin/env python3

import functions

# Challenge 1
words = [
    "apple", "banana", "apple", "orange", "banana",
    "apple", "kiwi", "banana", "banana", "grape", "kiwi"
]

# Challenge 2
matrix = [
    [1,2,3,4],
    [5,6,7,8]
]

#Challenge 3
dictionaries = [
    {"name": "Carlos", "age": 25},
    {"name": "Ana", "age": 30},
    {"name": "Felipe", "age": 22},
    {"name": "Matias", "age": 25},
    {"name": "Carlos", "age": 31},
    {"name": "Sofia", "age": 22}
]

# Challenge 5
numbers = [2, 3, 4, 5, 6]

# Challenge 6
filepath = "textfile.txt"

# Challenge 7
dir_path = "Challenge 7"

# Challenge 8
date1 = "2025-01-01"
date2 = "2025-06-18"

def menu():
    while True:
        print("\nSelect an option:")
        print(" 1. Challenge 1: Collections")
        print(" 2. Challenge 2: List Comprehensions")
        print(" 3. Challenge 3: Lambda Expressions")
        print(" 4. Challenge 4: Generators")
        print(" 5. Challenge 5: Itertools")
        print(" 6. Challenge 6: File Handling")
        print(" 7. Challenge 7: OS Library")
        print(" 8. Challenge 8: Datetime")
        print(" 9. Exit")

        option = input("Enter the option number: ")

        if option == '1':
            print(f"List of words: {words}")
            print(f"Most common word in list: {functions.most_common_word(words)}")
            break

        elif option == '2':
            print(f"Base Matrix: {matrix}")
            print(f"Transpose Matrix: {functions.transpose(matrix)}")
            break

        elif option == '3':
            print(f"Base dictionaries: {dictionaries}")
            print(f"Sort dictionaries: {functions.sort_by_key(dictionaries, 'name', 'age')}")
            break

        elif option == '4':
            print("Press any key to generate a prime number...\nPress Ctrl + C to exit.")
            try:
                gen = functions.prime_generator()
                while True:
                    input()
                    print(next(gen))
            except KeyboardInterrupt:
                print("\n Exiting...")
            break

        elif option == '5':
            print(f"Base numbers: {numbers}")
            print(f"All unique combinations of size 3: {functions.find_combinations(numbers)}")
            break

        elif option == '6':
            print(filepath)
            print(f"Lines: {functions.file_stats(filepath)['lines']}, Words: {functions.file_stats(filepath)['words']}, Characters: {functions.file_stats(filepath)['characters']}")
            break

        elif option == '7':
            print(functions.create_and_list_dir(dir_path))
            break

        elif option == '8':
            print(f"Date 1: {date1}")
            print(f"Date 2: {date2}")
            print(f"Difference in days: {functions.date_difference(date1, date2)}")
            break

        elif option == '9':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
