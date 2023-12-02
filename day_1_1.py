def get_sum_of_calibration_values(file_path: str) -> int:
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


if __name__ == "__main__":
    print(get_sum_of_calibration_values(r"resorces/day_1_1_input.txt"))
