#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

beats = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

while True:
    player1_play = input('First player play: ')
    player2_play = input('Second player play: ')

    if any(play not in beats for play in (player1_play, player2_play)):
        print("Incorrect input! :angry:")
        continue

    print("Player 1 wins") if beats[player1_play] == player2_play else print("Player 2 wins")
    print()
