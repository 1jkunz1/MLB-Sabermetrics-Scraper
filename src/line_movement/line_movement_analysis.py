from line_movement import NCAA, NFL, MLB

'''

We're looking for:
- Reverse line movement
- Public money on one

'''


def measure_line_movement():

    ncaa = NCAA()

    games = ncaa.create_game_object()

    movements = []

    for i in games:
        opening = i[2].split(' ')
        current = i[3].split(' ')
        opening_num = float(opening[0])
        current_num = float(current[0])
        movement = opening_num - current_num
        movements.append(movement)

    return movements


