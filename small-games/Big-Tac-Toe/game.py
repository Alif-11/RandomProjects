"""
Possible states:
    - None: No move has been made
    - "X": An X has been dropped in this spot
    - "O": An O has been dropped in this spot
"""


class TicTacToe:
    """ 
        TYPES: 
        * moves - [a set that can contain only the numbers 1 through 9, representing 
                   the 9 squares present on a Tic Tac Toe Board]

    """

    def __init__(self):
        # records all moves the user makes
        self.player_moves = set()
        # records all moves the cpu makes
        self.cpu_moves = set()

    def class_invariant(self, moves):
        if "<class 'set'>" != type(moves):
            raise Exception("all moves-type variables should be of type set")
        for ele in moves:
            if ele not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                raise Exception(
                    "moves contains numeric values that are not bound between 1 and 9 inclusive.")


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
