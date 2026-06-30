# BOT 1: Quincy just loops through these 5 moves forever
def quincy(prev_play, opponent_history=[]):
    pattern = ["R", "R", "P", "P", "S"]
    return pattern[len(opponent_history) % 5]

# BOT 2: Kris just copies whatever move you played last round
def kris(prev_play, opponent_history=[]):
    if not prev_play: 
        return "R"
    return prev_play

# BOT 3: Mrugesh always plays Paper (simplified version)
def mrugesh(prev_play, opponent_history=[]):
    return "P"

# BOT 4: Abbey always plays Rock (simplified version)
def abbey(prev_play, opponent_history=[]):
    return "R"
