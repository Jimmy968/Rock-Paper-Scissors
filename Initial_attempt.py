import random

def player(prev_play, opponent_history=[]):

    # First play, go with random move
    if prev_play == "":
        return random.choice(['R','P','S'])

    opponent_history.append(prev_play)

    # Calculate percentage of opponent's plays that have been 'R', 'P', and 'S'
    # and append these to dictionary opp_play_probs
    opp_play_probs = {}
    if len(opponent_history) > 5:
        opp_play_probs['R'] = opponent_history.count('R')/len(opponent_history)
        opp_play_probs['P'] = opponent_history.count('P')/len(opponent_history)
        opp_play_probs['S'] = opponent_history.count('S')/len(opponent_history)
        
        # Predict opponent's next play by selecting from 'R', 'P', or 'S'
        # weighted by their respective probabilities of occurring historically
        possible_opp_plays = list(opp_play_probs.keys())
        possible_opp_play_probs = list(opp_play_probs.values())
        opp_play_prediction = random.choices(possible_opp_plays, weights=possible_opp_play_probs, k=1)[0]

        ideal_response = {'R':'P', 'P':'S', 'S':'R'}
        return ideal_response[opp_play_prediction]

    # If it's not the first go and we haven't got enough
    # previous plays to calculate probabilities from, play random
    return random.choice(['R','P','S'])