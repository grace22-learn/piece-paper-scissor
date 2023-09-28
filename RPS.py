# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess

import random

def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)
# Define the player's next move
  if len(opponent_history) <= 2:
    # For the first two plays, play randomly
    guess = random.choice(['R', 'P', 'S'])
  else:
    # Determine the opponent's most frequent move from history
    opponent_moves = opponent_history[-2:]
    rock_count = opponent_moves.count('R')
    paper_count = opponent_moves.count('P')
    scissors_count = opponent_moves.count('S')
# Play the move that beats the opponent's most frequent move
    if rock_count >= paper_count and rock_count >= scissors_count:
      guess = 'P'  # Beat the opponent's most frequent move ('R') with paper
    elif paper_count >= rock_count and paper_count >= scissors_count:
      guess = 'S'  # Beat the opponent's most frequent move ('P') with scissors
    else:
      guess = 'R'  # Beat the opponent's most frequent move ('S') with rock

  return guess


def play_match(player_func, opponent_func, num_games):
  player_wins = 0
  opponent_wins = 0
  prev_play = None
  
  for _ in range(num_games):
    player_move = player_func(prev_play,opponent_history=opponent_moves)
    opponent_move = opponent_func()
    
    if player_move == opponent_move:
      continue
    elif (player_move == 'R' and opponent_move == 'S') or \
         (player_move == 'P' and opponent_move == 'R') or \
         (player_move == 'S' and opponent_move == 'P'):
      player_wins += 1
    else:
      opponent_wins += 1
    prev_play = opponent_move

  player_win_percentage = player_wins / num_games * 100
  return player_win_percentage

# Define the opponent 

# Bot 1: Always plays rock
def bot1():
  return 'R'

# Bot 2: Always plays paper
def bot2():
  return 'P'

# Bot 3: Always plays scissors
def bot3():
  return 'S'

# Bot 4: Plays randomly
def bot4():
  return random.choice(['R', 'P', 'S'])

opponent_bots = [bot1, bot2, bot3, bot4]

# Play matches against each opponent bot
for i, opponent_bot in enumerate(opponent_bots):
  opponent_moves = []
  num_games = 100  # Adjust the number of games as needed

  win_percentage = play_match(player, opponent_bot, num_games)
  if win_percentage >= 60:
    print(f"Player wins {win_percentage}% of games against Bot {i+1} - Passed")
  else:
    print(f"Player wins {win_percentage}% of games against Bot {i+1} - Failed")