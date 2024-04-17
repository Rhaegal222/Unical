package it.unical.Composite;

import it.unical.Flyweight.ChessPiece;

public class ChessBoard {
    private final ChessPiece[][] board = new ChessPiece[8][8];

    public void placePiece(ChessPiece piece, int x, int y) {
        board[x][y] = piece;
        piece.display(x, y);
    }
}
