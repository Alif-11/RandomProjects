"""
Possible states:
    - None: No move has been made
    - "X": An X has been dropped in this spot
    - "O": An O has been dropped in this spot
"""
gameUL = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameUM = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameUR = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameML = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameMM = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameMR = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameLL = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameLM = [[None, None, None],
          [None, None, None],
          [None, None, None]]
gameLR = [[None, None, None],
          [None, None, None],
          [None, None, None]]
every_game = [[gameUL, gameUM, gameUR],
              [gameML, gameMM, gameMR],
              [gameLL, gameLM, gameLR]]
