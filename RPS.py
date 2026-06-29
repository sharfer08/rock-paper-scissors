def player(prev_play, opponent_history=[], play_order={}):
    # Reset history and patterns when starting a new match against a new bot
    if not prev_play:
        opponent_history.clear()
        play_order.clear()
        return "R"

    # Keep track of the opponent's play history
    opponent_history.append(prev_play)
    guess = "R"

    # Look back at sequences of 3 moves to predict the 4th move
    n = 3
    if len(opponent_history) >= n:
        last_three = "".join(opponent_history[-n:])
        
        # Record the sequence that just occurred
        if len(opponent_history) > n:
            past_pattern = "".join(opponent_history[-(n+1):])
            play_order[past_pattern] = play_order.get(past_pattern, 0) + 1
            
        # Predict the opponent's most likely next move (R, P, or S)
        potential_next = [last_three + "R", last_three + "P", last_three + "S"]
        sub_counts = {move[-1]: play_order.get(move, 0) for move in potential_next}
        
        # Choose the move they have played most often after this sequence
        prediction = max(sub_counts, key=sub_counts.get)
        
        # Counter their predicted move to win
        ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
        guess = ideal_response[prediction]

    return guess
