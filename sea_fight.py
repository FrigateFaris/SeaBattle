playing_field_first = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] for i in range(10)]  # playing field 10
playing_field_second = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] for j in range(10)]  # playing field 10
shot_field_first = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] for y in range(10)]  # playing field 10
shot_field_second = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] for d in range(10)]  # playing field 10
playing_field_test_1 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] for u in range(10)]  # playing field 10
playing_field_test_2 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] for p in range(10)]
column_numbers = [{'A': '0'}, {'B': '1'}, {'C': '2'}, {'D': '3'}, {'E': '4'}, {'F': '5'}, {'G': '6'},
                  {'H': '7'}, {'I': '8'}, {'J': '9'}]  # for output column by letter
alphabet_numbers = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8', 'J': '9'}


def header_string():
    res_string = "- "
    for i in range(len(column_numbers)):
        res_string += list(column_numbers[i].keys())[0] + ' '
    return res_string


def concat_string(prefix, range_of_elements, postfix, elements):
    res_string = prefix
    for i in range(range_of_elements):
        res_string += f'{elements[i]}{postfix}'
    return res_string


def draw_field(elements):
    print(header_string())
    for i in range(10):
        print(concat_string(str(i) + '|', len(elements[i]), ' ', elements[i]))


data_ships_first = [['v'], ['v'], ['<', '<', '<'], ['>', '>', '>', '>']]
data_ships_second = [['v'], ['v'], ['<', '<', '<'], ['>', '>', '>', '>']]


def remaining_ships(ships):
    for i in ships:
        for j in i:
            print(j, end=' ')
        print()


def square(board, start_pos):
    field_mark = '*'
    field_square = [(0, 0), (0, 1), (1, 0), (0, -1), (0, -1), (-1, 0), (-1, 0), (0, 1), (0, 1)]
    board[start_pos[0]][start_pos[1]] = field_mark
    for i in field_square:
        i0 = i[0]
        i1 = i[1]
        start_pos[0] += i0
        start_pos[1] += i1
        if 0 <= start_pos[0] <= 9 and 0 <= start_pos[1] <= 9:
            board[start_pos[0]][start_pos[1]] = field_mark
        else:
            continue


removal_ship_status = True
column_letter_1, row_num_1 = 0, 0
column_letter_2, row_num_2 = 0, 0
ship_pos = None


def print_ship(ship, field, playing_field_test):
    print('Enter coordinates(order of range) of your ship')
    print('A3 for single section')
    print('A3 A4 for two section ship and etc:')
    try:
        coordinates = input().upper().split()
        global removal_ship_status
        if len(ship) == 1 and len(coordinates) == 1:
            column, row = coordinates[0][0], coordinates[0][1]
            if playing_field_test[int(row)][int(alphabet_numbers[column])] == "#":
                field[int(row)][int(alphabet_numbers[column])] = ship[0]
            else:
                print('You cannot place a ship next to an already standing ship')
                removal_ship_status = False
                return removal_ship_status
            square(playing_field_test, [int(row), int(alphabet_numbers[column])])
        elif len(coordinates) == 2:
            global column_letter_1, row_num_1, column_letter_2, row_num_2
            column_letter_1, row_num_1 = coordinates[0][0], coordinates[0][1]
            column_letter_2, row_num_2 = coordinates[1][0], coordinates[1][1]
            if column_letter_1 == column_letter_2:
                if abs(int(row_num_1) - int(row_num_2)) + 1 != len(ship):
                    print('You are out of range')
                    removal_ship_status = False
                    return removal_ship_status
                start = int(row_num_1)
                global ship_pos
                ship_pos = []

                for i in range(start, start + len(ship)):
                    if playing_field_test[int(i)][int(alphabet_numbers[column_letter_1])] == "#":
                        ship_pos.append(list([int(i), int(alphabet_numbers[column_letter_1])]))
                    else:
                        print('You cannot place a ship next to an already standing ship')
                        removal_ship_status = False
                        return removal_ship_status

                for i in ship_pos:
                    field[i[0]][i[1]] = ship[0]
                square(playing_field_test, [start, int(alphabet_numbers[column_letter_1])])
                square(playing_field_test, [start + len(ship) - 1, int(alphabet_numbers[column_letter_1])])
            elif column_letter_1 != column_letter_2:
                if abs(int(alphabet_numbers[column_letter_1]) - int(alphabet_numbers[column_letter_2])) + 1 != len(ship) \
                        and row_num_1 == row_num_2:
                    print('You are out of range')
                    removal_ship_status = False
                    return removal_ship_status
                elif row_num_1 != row_num_2:
                    removal_ship_status = False
                    return removal_ship_status
                start = int(alphabet_numbers[column_letter_1])
                ship_pos = []

                for i in range(start, start + len(ship)):
                    if playing_field_test[int(row_num_1)][i] == "#":
                        ship_pos.append(list([int(row_num_1), i]))
                    else:
                        print('You cannot place a ship next to an already standing ship')
                        removal_ship_status = False
                        return removal_ship_status

                for i in ship_pos:
                    field[i[0]][i[1]] = ship[0]
                square(playing_field_test, [int(row_num_1), start])
                square(playing_field_test, [int(row_num_1), start + len(ship) - 1])
            removal_ship_status = True
    except Exception:
        print('Something went wrong\nTry again')
        removal_ship_status = False


take_ships = None


def disposition_ships(ships, field, test_field):
    player_status = True
    while player_status:
        draw_field(field)
        print('your remaining ships:')
        remaining_ships(ships)
        global take_ships
        take_ships = input('enter the ship, which do you want to take: ').split()
        if take_ships not in ships:
            print('there is no such option or the ship has already been selected')
            continue
        print_ship(take_ships, field, test_field)
        if take_ships in ships and removal_ship_status is True:
            ships.remove(take_ships)
        if not ships:
            draw_field(field)
            player_status = False


two_deck_pos = []
three_deck_pos = []
four_deck_pos = []


def game_check(field_of_attack, player_field, two_deck, three_deck, four_deck):
    coordinates_attack = input('Enter coordinates: ').upper().split()
    column = coordinates_attack[0][0]
    row = coordinates_attack[0][1]
    global two_deck_pos, three_deck_pos, four_deck_pos, ship_pos
    if player_field[int(row)][int(alphabet_numbers[column])] == 'v' and field_of_attack[int(row)][int(alphabet_numbers[column])] != 'X':
        square(field_of_attack, [int(row), int(alphabet_numbers[column])])
        field_of_attack[int(row)][int(alphabet_numbers[column])] = 'X'
        draw_field(field_of_attack)
        print('ship killed')
        return 'hit one deck'
    elif player_field[int(row)][int(alphabet_numbers[column])] == '^' and field_of_attack[int(row)][int(alphabet_numbers[column])] != 'X':
        two_deck.append(coordinates_attack)
        if len(two_deck) == 2:
            square(field_of_attack, [int(two_deck[0][0][1]), int(alphabet_numbers[two_deck[0][0][0]])])
            square(field_of_attack, [int(two_deck[1][0][1]), int(alphabet_numbers[two_deck[1][0][0]])])
            field_of_attack[int(two_deck[0][0][1])][int(alphabet_numbers[two_deck[0][0][0]])] = 'X'
        field_of_attack[int(row)][int(alphabet_numbers[column])] = 'X'
        draw_field(field_of_attack)
        print('Great shot!')
        return 'hit two deck'
    elif player_field[int(row)][int(alphabet_numbers[column])] == '<' and field_of_attack[int(row)][int(alphabet_numbers[column])] != 'X':
        three_deck.append(coordinates_attack)
        if len(three_deck) == 3:
            square(field_of_attack, [int(three_deck[0][0][1]), int(alphabet_numbers[three_deck[0][0][0]])])
            square(field_of_attack, [int(three_deck[-1][0][1]), int(alphabet_numbers[three_deck[-1][0][0]])])
            field_of_attack[int(three_deck[0][0][1])][int(alphabet_numbers[three_deck[0][0][0]])] = 'X'
            field_of_attack[int(three_deck[1][0][1])][int(alphabet_numbers[three_deck[1][0][0]])] = 'X'
        field_of_attack[int(row)][int(alphabet_numbers[column])] = 'X'
        draw_field(field_of_attack)
        print('Great shot!')
        return 'hit three deck'
    elif player_field[int(row)][int(alphabet_numbers[column])] == '>' and field_of_attack[int(row)][int(alphabet_numbers[column])] != 'X':
        four_deck.append(coordinates_attack)
        if len(four_deck) == 4:
            square(field_of_attack, [int(four_deck[0][0][1]), int(alphabet_numbers[four_deck[0][0][0]])])
            square(field_of_attack, [int(four_deck[-1][0][1]), int(alphabet_numbers[four_deck[-1][0][0]])])
            field_of_attack[int(four_deck[0][0][1])][int(alphabet_numbers[four_deck[0][0][0]])] = 'X'
            field_of_attack[int(four_deck[1][0][1])][int(alphabet_numbers[four_deck[1][0][0]])] = 'X'
            field_of_attack[int(four_deck[2][0][1])][int(alphabet_numbers[four_deck[2][0][0]])] = 'X'
        field_of_attack[int(row)][int(alphabet_numbers[column])] = 'X'
        draw_field(field_of_attack)
        print('Great shot!')
        return 'hit four deck'
    elif player_field[int(row)][int(alphabet_numbers[column])] == '#':
        field_of_attack[int(row)][int(alphabet_numbers[column])] = '*'
        draw_field(field_of_attack)
        print('Unfortunately you missed')
        return 'missed'
    elif field_of_attack[int(row)][int(alphabet_numbers[column])] == 'X' or field_of_attack[int(row)][int(alphabet_numbers[column])] == '*':
        print('You can not attack an opponent already in the attacked place\nTry again!')
        return 'Fall'


def first_player():
    print(f'\nFirst player, arrange ships')
    disposition_ships(data_ships_first, playing_field_first, playing_field_test_1)


first_player()


def second_player():
    print(f'\nSecond player, arrange ships')
    disposition_ships(data_ships_second, playing_field_second, playing_field_test_2)


second_player()


def sea_battle_players():
    print('\n\n\nGreat, now attack your opponent! Good luck!')
    print('First player, start first')
    count_ship_first = 0
    count_ship_second = 0
    hits_two_deck = 0
    hits_three_deck = 0
    hits_four_deck = 0
    global two_deck_pos, three_deck_pos, four_deck_pos
    game_status = True
    while game_status:
        while count_ship_first != 9:
            print('First player, your turn!')
            check_point = game_check(shot_field_first, playing_field_second, two_deck_pos, three_deck_pos, four_deck_pos)
            if check_point == 'hit one deck':
                count_ship_first += 1
            if check_point == 'hit two deck':
                hits_two_deck += 1
                count_ship_first += 1
                if hits_two_deck == 2:
                    print('ship killed')
                    hits_two_deck = 0
                    two_deck_pos = []
                continue
            if check_point == 'hit three deck':
                hits_three_deck += 1
                count_ship_first += 1
                if hits_three_deck == 3:
                    print('ship killed')
                    hits_three_deck = 0
                    three_deck_pos = []
                continue
            if check_point == 'hit four deck':
                hits_four_deck += 1
                count_ship_first += 1
                if hits_four_deck == 4:
                    print('ship killed')
                    hits_four_deck = 0
                    four_deck_pos = []
                continue
            elif check_point == 'missed':
                break
            elif check_point == 'Fall':
                continue
        if count_ship_first == 9:
            print('First Player, you are WON!')
            print('Congratulations!')
            game_status = False
            continue
        while count_ship_second != 9:
            print('Second player, your turn!')
            check_point = game_check(shot_field_second, playing_field_first, two_deck_pos, three_deck_pos, four_deck_pos)
            if check_point == 'hit one deck':
                count_ship_second += 1
            if check_point == 'hit two deck':
                hits_two_deck += 1
                count_ship_second += 1
                if hits_two_deck == 2:
                    print('ship killed')
                    hits_two_deck = 0
                    two_deck_pos = []
                continue
            if check_point == 'hit three deck':
                hits_three_deck += 1
                count_ship_second += 1
                if hits_three_deck == 3:
                    print('ship killed')
                    hits_three_deck = 0
                    three_deck_pos = []
                continue
            if check_point == 'hit four deck':
                hits_four_deck += 1
                count_ship_second += 1
                if hits_four_deck == 4:
                    print('ship killed')
                    hits_four_deck = 0
                    four_deck_pos = []
                continue
            elif check_point == 'missed':
                break
            elif check_point == 'Fall':
                continue
        if count_ship_second == 9:
            print('Second Player, you are WON!')
            print('Congratulations!')
            game_status = False
            continue


sea_battle_players()
