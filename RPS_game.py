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
    regex = ["R", "R", "P", "P", "S"]
    return regex[len(opponent_history) % len(regex)]

def mrugesh(prev_play, opponent_history=[]):
    if not prev_play: prev_play = 'R'
    opponent_history.append(prev_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_response[most_frequent]

def kris(prev_play, opponent_history=[]):
    if not prev_play: prev_play = 'R'
    opponent_history.append(prev_play)
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_response[opponent_history[-1]]

def abbey(prev_play, opponent_history=[], play_order=[{
          "RR": 0, "RP": 0, "RS": 0,
          "PR": 0, "PP": 0, "PS": 0,
          "SR": 0, "SP": 0, "SS": 0,
      }]):
    if not prev_play: prev_play = 'R'
    opponent_history.append(prev_play)
    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1
    potential_plays = [
        "".join([opponent_history[-1], "R"]),
        "".join([opponent_history[-1], "P"]),
        "".join([opponent_history[-1], "S"]),
    ]
    sub_order = {k: play_order[0][k] for k in potential_plays if k in play_order[0]}
    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1]
    else:
        prediction = "R"
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_response[prediction]
