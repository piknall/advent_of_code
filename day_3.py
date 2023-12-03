import math


def restrict(number: int, low=-float("inf"), high=float("inf")):
    return sorted((low, number, high))[1]


def get_part_sum(file_path: str) -> int:
    with open(file_path, "r") as file:
        rows = file.read().splitlines()

    part_sum = 0

    for row_index, row in enumerate(rows):
        letter_index = 0
        while letter_index < len(row):
            for number_length in range(3, 0, -1):
                str_number = row[letter_index: letter_index + number_length]
                if not str_number.isnumeric():
                    continue

                symbol_nearby = False

                if row_index != 0:
                    testing_row = rows[row_index - 1]
                    for i in range(restrict(letter_index - 1, low=0),
                                   restrict(letter_index + number_length + 1, high=len(testing_row))):
                        test_letter = testing_row[i]
                        if not test_letter.isnumeric() and test_letter != ".":
                            symbol_nearby = True
                            break

                if not symbol_nearby:
                    testing_row = row
                    for i in range(restrict(letter_index - 1, low=0),
                                   restrict(letter_index + number_length + 1, high=len(testing_row))):
                        test_letter = testing_row[i]
                        if not test_letter.isnumeric() and test_letter != ".":
                            symbol_nearby = True
                            break

                if row_index < len(rows) - 1 and not symbol_nearby:
                    testing_row = rows[row_index + 1]
                    for i in range(restrict(letter_index - 1, low=0),
                                   restrict(letter_index + number_length + 1, high=len(testing_row))):
                        test_letter = testing_row[i]
                        if not test_letter.isnumeric() and test_letter != ".":
                            symbol_nearby = True
                            break

                if symbol_nearby:
                    part_sum += int(str_number)

                letter_index += number_length
                break

            else:
                letter_index += 1

    return part_sum


def get_gear_sum(file_path: str) -> int:
    with open(file_path, "r") as file:
        rows = file.read().splitlines()

    gear_sum = 0

    for row_index, row in enumerate(rows):
        for letter_index, letter in enumerate(row):
            if letter != "*":
                continue

            gear_numbers = []
            for test_row_index in range(restrict(row_index - 1, low=0), restrict(row_index + 2, high=len(rows))):
                test_row = rows[test_row_index]

                leading_letter_index = -3
                while leading_letter_index <= 1:
                    for number_length in range(3, 0, -1):
                        if (leading_letter_index + letter_index < 0 or
                                leading_letter_index + letter_index + number_length > len(row)):
                            continue
                        if leading_letter_index + number_length < 0:
                            continue

                        test_number = test_row[letter_index + leading_letter_index:
                                               letter_index + leading_letter_index + number_length]

                        if test_number.isnumeric():
                            gear_numbers.append(int(test_number))
                            leading_letter_index += len(test_number)
                            break
                    else:
                        leading_letter_index += 1

            if len(gear_numbers) == 2:
                gear_sum += math.prod(gear_numbers)

    return gear_sum


def get_symbols(file_path: str):
    with open(file_path, "r") as file:
        rows = file.read().splitlines()

    symbols = set()

    for row in rows:
        for letter in row:
            if not letter.isnumeric():
                symbols.add(letter)

    return symbols


if __name__ == "__main__":
    print(get_part_sum(r"resources\day_3_input.txt"))
    print(get_gear_sum(r"resources\day_3_input.txt"))
