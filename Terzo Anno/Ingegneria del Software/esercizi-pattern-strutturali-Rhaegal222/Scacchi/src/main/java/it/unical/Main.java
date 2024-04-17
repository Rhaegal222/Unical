package it.unical;

import it.unical.Flyweight.ChessPieceFactory;
import it.unical.Composite.ChessBoard;

public class Main {
    public static void main(String[] args) {
        ChessPieceFactory factory = new ChessPieceFactory();
        ChessBoard chessBoard = new ChessBoard();

        // Piazzamento di alcuni pezzi utilizzando il Flyweight e il Composite Pattern.
        chessBoard.placePiece(factory.getChessPiece("Pedone", "Bianco"), 0, 1);
        chessBoard.placePiece(factory.getChessPiece("Torre", "Bianco"), 0, 0);
        chessBoard.placePiece(factory.getChessPiece("Cavallo", "Nero"), 7, 1);
        chessBoard.placePiece(factory.getChessPiece("Regina", "Nero"), 7, 3);
    }
}