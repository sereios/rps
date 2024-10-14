# The example function below keeps track of the opponent's history and plays 
# whatever the opponent played two plays ago. It is not a very good player so 
# you will need to change the code to pass the challenge.

MOVES = ["R", "P", "S"]
RESPONSES = {"R": "P", "P": "S", "S": "R"}
MEMORY = 6
KNOWN_COMBINATIONS = {}

def player(prev_play, opponent_history=[]):
    def update_known_combinations(last_moves):
        if last_moves in KNOWN_COMBINATIONS:
            KNOWN_COMBINATIONS[last_moves] += 1
        else:
            KNOWN_COMBINATIONS[last_moves] = 1

    def return_most_likely(possible_combinations):
        most_likely_combination = max(possible_combinations,
                                      key=lambda x: KNOWN_COMBINATIONS[x] 
                                      if x in KNOWN_COMBINATIONS else 0)
        most_likely_move = most_likely_combination[-1]
        return RESPONSES[most_likely_move]

    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > MEMORY:
        last_moves = "".join(opponent_history[-MEMORY:])
        possible_combinations = [last_moves[1:] + next_play
                            for next_play in MOVES]
        update_known_combinations(last_moves)
        guess = return_most_likely(possible_combinations)

    return guess
    