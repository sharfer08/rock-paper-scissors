# The game engine that loops 1000 times
def play(player1, player2, num_games, verbose=False):
    p1_history = []
    p2_history = []
    p1_prev = ""
    p2_prev = ""
    p1_won = 0

    for _ in range(num_games):
        p1_move = player1(p2_prev, p1_history)
        p2_move = player2(p1_prev, p2_history)
        
        p1_history.append(p1_move)
        p2_history.append(p2_move)
        p1_prev = p1_move
        p2_prev = p2_move

        # Simple score keeping logic
        if p1_move == p2_move:
            pass
        elif (p1_move == "R" and p2_move == "S") or (p1_move == "P" and p2_move == "R") or (p1_move == "S" and p2_move == "P"):
            p1_won += 1

    if verbose:
        print("Player 1 wins:", f"({p1_won/num_games*100:.1f}%)")
    return p1_won / num_games * 100

# BOT 1: Quincy loops through 5 moves
def quincy(prev_play, opponent_history=[]):
    moves = ["R", "R", "P", "P", "S"]
    return moves[len(opponent_history) % 5]

# BOT 2: Kris copies your last move
def kris(prev_play, opponent_history=[]):
    if not prev_play: return "R"
    return prev_play

# BOT 3: Mrugesh defaults to Paper
def mrugesh(prev_play, opponent_history=[]):
    return "P"

# BOT 4: Abbey defaults to Rock
def abbey(prev_play, opponent_history=[]):
    return "R"
