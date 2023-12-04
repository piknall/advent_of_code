import functools


def get_pile_sum(file_path: str) -> int:
    with open(file_path, "r") as file:
        cards = file.read().splitlines()

    pile_sum = 0

    for str_card in cards:
        winning_numbers, card_numbers = str_card.split(" | ")
        winning_numbers = {int(number) for number in winning_numbers.split()[2:]}
        card_numbers = {int(number) for number in card_numbers.split()}

        number_of_winning_numbers = len(winning_numbers & card_numbers)

        if number_of_winning_numbers:
            pile_sum += 2**(number_of_winning_numbers - 1)

    return pile_sum


def get_number_of_won_cards(file_path: str) -> int:
    with open(file_path, "r") as file:
        cards = file.read().splitlines()

    @functools.cache
    def get_card_count(card_index: int):
        winning_numbers, card_numbers = cards[card_index].split(" | ")
        winning_numbers = {int(number) for number in winning_numbers.split()[2:]}
        game_numbers = {int(number) for number in card_numbers.split()}

        won_copies = winning_numbers & game_numbers

        if not won_copies:
            return 1

        return sum(get_card_count(card_index + copy_index + 1) for copy_index in range(len(won_copies))) + 1

    return sum(map(get_card_count, range(len(cards))))


if __name__ == "__main__":
    print(get_pile_sum(r"resources\day_4_input.txt"))
    print(get_number_of_won_cards(r"resources\day_4_input.txt"))
