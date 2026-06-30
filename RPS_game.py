import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    p1_history = []
    p2_history = []
    p1_won = 0
    p2_won = 0
    tie = 0

    for _ in range(num_games):
        p1 = player1(p2_prev_play, p1_history)
        p2 = player2(p1_prev_play, p2_history)
        p1_history.append(p1)
        p2_history.append(p2)
        p1_prev_play = p1
        p2_prev_play = p2

        if p1 == p2:
            tie += 1
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_won += 1
        else:
            p2_won += 1

    if verbose:
        print("Games played:", num_games)
        print("Player 1 wins:", p1_won, f"({p1_won/num_games*100:.1f}%)")
        print("Player 2 wins:", p2_won, f"({p2_won/num_games*100:.1f}%)")
        print("Ties:", tie)

    return p1_won / num_games * 100

def quincy(prev_play, opponent_history=[]):
    pattern = ["R", "R", "P", "P", "S"]
    return pattern[len(opponent_history) % 5]

def kris(prev_play, opponent_history=[]):
    if not prev_play: return "R"
    return prev_play

def mrugesh(prev_play, opponent_history=[]):
    return "P"

def abbey(prev_play, opponent_history=[]):
    return "R"
