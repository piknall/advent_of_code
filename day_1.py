def get_sum_of_integer_calibration_values(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    numbers = {str(i) for i in range(10)}

    calibration_sum = 0

    for line in lines:
        for letter in line:
            if letter in numbers:
                first_number = letter
                break

        for letter in line[::-1]:
            if letter in numbers:
                last_number = letter
                break

        calibration_sum += int(first_number + last_number)

    return calibration_sum


def get_sum_of_all_calibration_values(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    integer_numbers = {str(i) for i in range(10)}
    letter_numbers = {"one", "six", "zero", "four", "five", "eight", "nine", "three", "seven", "two"}
    letter_number_values = {"one": "1", "six": "6", "zero": "0", "four": "4", "five": "5",
                            "eight": "8", "nine": "9", "three": "3", "seven": "7", "two": "2"}

    calibration_sum = 0

    for index, line in enumerate(lines):
        line_length = len(line)
        for letter_index, letter in enumerate(line):
            if letter in integer_numbers:
                first_number = letter
                break

            first_number_found = False
            for word_length in range(3, 6):
                if line_length - letter_index < word_length:
                    break
                str_number = line[letter_index:letter_index+word_length]
                if str_number in letter_numbers:
                    first_number = letter_number_values[str_number]
                    first_number_found = True
                    break

            if first_number_found:
                break

        for letter_index in range(len(line) - 1, -1, -1):
            letter = line[letter_index]
            if letter in integer_numbers:
                last_number = letter
                break

            last_number_found = False
            for word_length in range(3, 6):
                if line_length - letter_index < word_length:
                    break
                str_number = line[letter_index:letter_index + word_length]
                if str_number in letter_numbers:
                    last_number = letter_number_values[str_number]
                    last_number_found = True
                    break

            if last_number_found:
                break

        calibration_sum += int(first_number + last_number)

    return calibration_sum


if __name__ == "__main__":
    print(get_sum_of_integer_calibration_values(r"resources/day_1_1_input.txt"))
    print(get_sum_of_all_calibration_values(r"resources/day_1_1_input.txt"))
