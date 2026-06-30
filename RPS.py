def player(prev_play, opponent_history=[], play_order={}):
    # 1. Reset memory at the start of a brand new match
    if not prev_play:
        opponent_history.clear()
        play_order.clear()
        return "R"

    # 2. Add the opponent's last move to our running history list
    opponent_history.append(prev_play)
    guess = "R"  # Default safe guess

    # 3. Pattern Matching Logic
    n = 3  # Look back at sequences of 3 moves to predict the 4th
    if len(opponent_history) >= n:
        last_three = "".join(opponent_history[-n:])

        # Record the 4-move combination that just happened into our dictionary
        if len(opponent_history) > n:
            past_pattern = "".join(opponent_history[-(n+1):])
            play_order[past_pattern] = play_order.get(past_pattern, 0) + 1

        # Check history to see what they usually play after this specific sequence
        potential_next = [last_three + "R", last_three + "P", last_three + "S"]
        sub_counts = {move[-1]: play_order.get(move, 0) for move in potential_next}
        
        # Predict their next move based on the highest count
        prediction = max(sub_counts, key=sub_counts.get)
        
        # Counter their predicted move to win the round
        ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
        guess = ideal_response[prediction]

    return guess
