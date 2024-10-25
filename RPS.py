# The basic idea is to emulate Abbey's strategy which is itself based on a markov
# chain. To beat abbey, we need a longer MEMORY, which can be set in the constants
# in the beginning of this script. Instead of defining all possible combinations
# beforehand, the player keeps an evolving record, stored in the global 
# KNOWN_COMBINATIONS dict.
# Increasing MEMORY to 7 consistently beats Abbey more than 60 percent of the 
# time and also all other opponents.

import random

# Define constants and global variables

MOVES = ["R", "P", "S"]
RESPONSES = {"R": "P", "P": "S", "S": "R"}
MEMORY = 7
KNOWN_COMBINATIONS = {}

# player function to be used in RPS_game

def player(prev_play, opponent_history=[]):
    def update_known_combinations(last_moves):
        """Function to update the record dict with new combinations or 
        counter of known combinations."""
        if last_moves in KNOWN_COMBINATIONS:
            KNOWN_COMBINATIONS[last_moves] += 1
        else:
            KNOWN_COMBINATIONS[last_moves] = 1

    def return_most_likely(possible_combinations):
        """Based upon the record dict, return the most likely combination from 
        all possible combinations and in turn the most likely next move."""
        most_likely_combination = max(possible_combinations,
                                      key=lambda x: KNOWN_COMBINATIONS[x] 
                                      if x in KNOWN_COMBINATIONS else 0)
        # as possible combinations are a concatenation of the last moves and 
        # all possible next moves, the last move in the most_likely_combination 
        # is the most likely next move of the opponent.
        most_likely_move = most_likely_combination[-1]
        return RESPONSES[most_likely_move]
    
    def return_possible(last_moves):
        """Based upon last moves return all combinations with possible next 
        move."""
        return [last_moves[1:] + next_play for next_play in MOVES]

    opponent_history.append(prev_play)

    # guess = random.choice(MOVES)

    guess = "P"  # Somehow, starting with "S" increases chances against Abbey.
                 # Hint taken from the freecodecamp forum.
    
    # play a few games till length of opponent_history allows for use of markov
    # chain, then use that to guess next moves
    if len(opponent_history) > MEMORY:
        last_moves = "".join(opponent_history[-MEMORY:])
        update_known_combinations(last_moves)
        guess = return_most_likely(return_possible(last_moves))

    return guess
    