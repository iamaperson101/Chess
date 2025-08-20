import chess

def MakeMove(moveparts, board, turn):
        for square in range(64): # number of squares on chess board
            if (len(moveparts) == 3): # piece move
                if (str(board.piece_at(square)) == moveparts[0]):
                    destination = chess.parse_square(moveparts[1]+moveparts[2])
                    move = chess.Move(square, destination) 
                    if move in board.legal_moves:
                        board.push(move)
                        return
                    else:
                        continue
            elif (len(moveparts) == 2): # pawn move
                if (str(board.piece_at(square)) == ("P")):
                    moveparts[0]=moveparts[0].lower()
                    destination = chess.parse_square(moveparts[0]+moveparts[1])
                    move = chess.Move(square, destination) 
                    if move in board.legal_moves:
                        board.push(move)
                        return
                elif (str(board.piece_at(square)) == ("p")):
                    moveparts[0]=moveparts[0].lower()
                    destination = chess.parse_square(moveparts[0]+moveparts[1])
                    move = chess.Move(square, destination)
                    if move in board.legal_moves:
                        board.push(move)
                        return

                


def main():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print(board)
    moves = 0
    while (board.is_game_over(claim_draw=True) == False):
        if (moves % 2 == 1):
            turn = "black"
        elif (moves % 2 == 0):
            turn = "white"
            
        move = input("Enter your chess move(enter 'a' for instructions) ")
        
        if (move == "a"):
            print("\nEnter your chess move in algebraic chess notation without any extra characters (Case sensitive)\n")
        else:
            moveparts = list(move)
            # in python chess's board, white pieces are represented by uppercase letters, and vice versa 
            print(turn)
            if (turn == "white"):
                moveparts[0] = moveparts[0].upper()
            elif (turn == "black"):
                moveparts[0] = moveparts[0].lower()
            MakeMove(moveparts, board, turn)
            print(board)
            moves += 1
main()