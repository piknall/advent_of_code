def get_games(file_path: str) -> tuple[tuple[tuple[int, ...], tuple[str, ...]], ...]:
    with open(file_path, "r") as file:
        game_strings = file.read().splitlines()

    games = tuple(
        (
            tuple(map(int, (game_parts := game_string.split())[2::2])),
            tuple(part.rstrip(",;") for part in game_parts[3::2])
        ) for game_string in game_strings
    )

    return games


def get_possible_games_id_sum(games: tuple[tuple[tuple[int, ...], tuple[str, ...]], ...]):
    number_of_cubes = {"red": 12, "green": 13, "blue": 14}

    id_sum = 0

    for game_id, game in enumerate(games):
        for cube_number, colour in zip(*game):
            if cube_number > number_of_cubes[colour]:
                break
        else:
            id_sum += game_id + 1

    return id_sum


def get_minimal_cubes_sum(games: tuple[tuple[tuple[int, ...], tuple[str, ...]], ...]):
    pow_sum = 0

    for game_id, game in enumerate(games):
        red_min = 0
        green_min = 0
        blue_min = 0

        for cube_number, colour in zip(*game):
            if colour == "red" and cube_number > red_min:
                red_min = cube_number
            elif colour == "green" and cube_number > green_min:
                green_min = cube_number
            elif colour == "blue" and cube_number > blue_min:
                blue_min = cube_number

        pow_sum += red_min * green_min * blue_min

    return pow_sum


if __name__ == "__main__":
    print(get_possible_games_id_sum(get_games(r"resources\day_2_input.txt")))
    print(get_minimal_cubes_sum(get_games(r"resources\day_2_input.txt")))
