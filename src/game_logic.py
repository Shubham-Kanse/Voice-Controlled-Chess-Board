import chess

board = chess.Board()  # Initialize a chessboard

def validate_move(move_command):
    """ Validates the move using chess rules """
    try:
        start, end = move_command.split()  # Example: "A2 B6"
        chess_move = chess.Move.from_uci(start.lower() + end.lower())  # Convert to UCI format

        if chess_move in board.legal_moves:
            board.push(chess_move)  # Execute the move in memory
            return True
        else:
            print("❌ Invalid move according to chess rules.")
            return False
    except Exception as e:
        print(f"❌ Move validation error: {e}")
        return False
