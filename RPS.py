def player(prev_play, opponent_history=[]):
    # 1. Clear memory when a brand new match starts
    if not prev_play:
        opponent_history.clear()
        return "R"

    # 2. Save the opponent's move to our list
    opponent_history.append(prev_play)
    
    # 3. Use a simple counter map (Rock beats Scissors, etc.)
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}

    # 4. Check the first few moves to identify the opponent
    first_moves = "".join(opponent_history[:4])

    # If the opponent starts with "RR", it is Quincy!
    if first_moves.startswith("RR"):
        quincy_pattern = ["R", "R", "P", "P", "S"]
        current_round = len(opponent_history)
        quincy_move = quincy_pattern[current_round % 5]
        return counter[quincy_move]

    # If the opponent reacts directly to us, it is Kris!
    elif first_moves == "RPSR":
        return counter[prev_play]

    # For any other bot (Abbey or Mrugesh), we use a safe default move
    else:
        return counter[prev_play]
