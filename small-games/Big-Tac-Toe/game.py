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
        # all valid moves that could be made
        self.valid_moves = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # how many pieces are on the board
        self.time_step = 0
        # the state of the game. can take four string literal values:
        # win, loss, tied, unresolved
        self.game_state = "unresolved"

    # checks if all field variables fulfill their required conditions.
    def class_invariant(self):
        # ONLY FOR TESTING
        if "<class 'set'>" != type(self.player_moves):
            raise Exception("player_moves is not of type set")
        for ele in self.player_moves:
            if ele not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                raise Exception(
                    "player_moves contains numeric values that are not bound between 1 and 9 inclusive.")
        if "<class 'set'>" != type(self.cpu_moves):
            raise Exception("cpu_moves is not of type set")
        for ele in self.cpu_moves:
            if ele not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                raise Exception(
                    "cpu_moves contains numeric values that are not bound between 1 and 9 inclusive.")
        if "<class 'set'>" != type(self.valid_moves):
            raise Exception("valid_moves is not of type set")
        for ele in self.valid_moves:
            if ele not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                raise Exception(
                    "valid_moves contains numeric values that are not bound between 1 and 9 inclusive.")
            if ele in self.cpu_moves:
                raise Exception(
                    "duplicate values found between valid_moves and cpu_moves")
            if ele in self.player_moves:
                raise Exception(
                    "duplicate values found between valid_movea and player_moves")
        if self.time_step < 0 or self.time_step > 9:
            raise Exception("invalid time step")
        match self.game_state:
            case "unresolved" | "win" | "loss" | "tied":
                pass
            case _:
                raise Exception("invalid value for game_state")

    def check_win(self, moves: set, win_cases: set[set], is_player_turn: bool):
        """
            checks to see if a win or loss occurred.

            Params:
                - moves: the move set we're checking in
                - win_cases: all possible win cases that could arise with the most recently placed pos
                - is_player_turn: is it the player turn or not
        """
        for set in win_cases:
            if set.issubset(moves):
                if is_player_turn:
                    self.game_state = "win"
                else:
                    self.game_state = "loss"
                break

    def check_update_game_state(self, pos: int, is_player_turn: bool):
        """
            checks to see if the RECENTLY PLACED pos parameter updates the game_state.
            makes corresponding changes if so.

            # Params: 
                - pos: position that was moved to 
                - is_player_turn: is it the player turn or not       

            NOTE: should ONLY BE CALLED by other methods -
            NEVER STANDALONE. SHOULD ONLY BE RUN AFTER self.time_step >= 5.
        """
        moves = None
        match is_player_turn:
            case True:
                moves = self.player_moves
            case False:
                moves = self.cpu_moves
        try:
            assert (pos > 0 and pos < 10)
        except:
            raise Exception(
                "pos parameter should be an int between 1 and 9 inclusive.")
        win_cases_dict = {1: {{2, 3}, {4, 7}, {5, 9}}, 2: {{1, 3}, {5, 8}},
                          3: {{1, 2}, {6, 9}, {5, 7}}, 4: {{1, 7}, {5, 6}},
                          5: {{1, 9}, {3, 7}, {4, 6}, {2, 8}}, 6: {{4, 5}, {3, 9}},
                          7: {{1, 4}, {8, 9}, {3, 5}}, 8: {{7, 9}, {2, 5}},
                          9: {{3, 6}, {7, 8}, {1, 5}}}
        self.check_win(moves, win_cases_dict[pos], is_player_turn)
        if self.time_step >= 9 and self.game_state == "unresolved":
            self.game_state = "tied"
        self.class_invariant()  # comment this out when done


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
