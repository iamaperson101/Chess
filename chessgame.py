import chess

def coordinateFinder(piece, file, row, board): # find the coordinate of the piece that will be moved
    # loop through squares on the chess board and check using a function if the piece that exists on the square matches the variable piece.
    # if it does, try to move the piece to the specified square using the file and row variables, if it fails, continue the loop until it suceeds.

    
    for i in range(64):
        if (str(board.piece_at(i)) == piece):
            destination = chess.parse_square(file+row)
            move = chess.Move(i, destination) 
            if move in board.legal_moves:
                board.push(move)
                return
            else:
                continue
        else:
            if (board.piece_at(i) == str(piece)): # debugging
                print("angry")
            print("board.piece_at(i): "+ str(board.piece_at(i)))
            print("piece: "+ piece)
    print("bananas")        
    return
    



def main():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print(board)
    while (board.is_game_over(claim_draw=True) == False):
        move = input("Enter your chess move(enter 'a' for instructions) ")
        
        if (move == "a"):
            print("\nEnter your chess move in algebraic chess notation without any extra characters (Case sensitive)\n")
        else:
            parts = list(move)
            coordinateFinder(parts[0], parts[1], parts[2], board)
            print(board)
    print(board)
main()