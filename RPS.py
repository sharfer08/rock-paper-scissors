def player(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
        return "R"

    opponent_history.append(prev_play)
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    first_moves = "".join(opponent_history[:4])

    if first_moves.startswith("RR"):
        quincy_pattern = ["R", "R", "P", "P", "S"]
        current_round = len(opponent_history)
        quincy_move = quincy_pattern[current_round % 5]
        return counter[quincy_move]
    elif first_moves == "RPSR":
        return counter[prev_play]
    else:
        return counter[prev_play]
