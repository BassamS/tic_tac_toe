class TicTacToe:
  def __init__(self):
    self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
    self.current_winner = None # keep track of winner!

  def print_board(self):
    # This is just getting the rows
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')

  @staticmethod
  def print_board_nums():
    # tell us what number corresponds to which box
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')

  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
      return ' ' in self.board

    def num_empty_squares(self):
      return self.board.count(' ')

    def make_move(self, square, letter):
      # if valid move, then make the move (assign square to letter)
      # then return true. If invalid, return false
      if self.board[square] == ' ':
        self.board[square] = letter
        if self.winner(square, letter):
          self.current_winner = letter
        return True
      return False

    # ######### other way of writing it!!!!!!!
    # moves = []
    # for (i, spot) in enumerate(self.board):

    #   if spot == ' ':
    #     moves.append(i)
    # return moves

    def play(game, x_player, o_player, print_game=True):
      if print_game:
        game.print_board_nums()

      letter = 'X' # starting letter

      while game.empty_squares():
        # get the move from the appropriate player
        if letter == '0':
          square = o_player.get_move(game)
        else:
          square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter):
          if print_game:
            print(letter + f' makes a move to square {square}')
            game.print_board()
            print('') # just empty line

          if game.current_winner:
            if print_game:
              print(letter + ' wins!')

          # after we made our move, we need to alternate letters
          letter = '0' if letter == 'X' else 'X' # switches player