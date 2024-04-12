def player(prev_play, opponent_history=[], sequences={}):
  # prev_play: opponent's previous play
  # opponent_history: list containing opponent's play history
  # sequences: dictionary containing sequences of plays made
  # by opponent (keys) and their frequency (values)

  # First play, go with 'R'
  if prev_play == "":
    return 'R'

  opponent_history.append(prev_play)

  # Define length of sequences stored in sequences dictionary
  seq_len = 5

  if len(opponent_history) >= seq_len:
    seq = "".join(opponent_history[-seq_len:])
    # If sequence does not exist, append it to dictionary and set frequency to 1
    # If sequence does exit, increase frequency by 1
    sequences[seq] = sequences.get(seq, 0) + 1
    
    # Create list of opponent's next possible sequences using 
    # opponent's last (seq_len-1) plays + 'R', 'P', or 'S'
    next_possible_seqs = [
      "".join([*opponent_history[-(seq_len-1):], play]) for play in ['R', 'P', 'S']
    ]

    # Create dictionary containing those next possible sequences which 
    # have been seen before (keys), and their frequency (values)
    seen_before = {}
    for next_possible_seq in next_possible_seqs:
      if next_possible_seq in sequences:
        seen_before[next_possible_seq] = sequences[next_possible_seq]

    if seen_before:
      # Predict opponent's next sequence to be whichever next possible one we've seen the most in the past
      # [-1:] gets the prediction of the opponent's next play from the prediction of the next sequence
      prediction = max(seen_before, key=seen_before.get)[-1:]
  
    else:
      # If we have not seen any of the next possible sequences, we go with 'R'
      return 'R'

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]