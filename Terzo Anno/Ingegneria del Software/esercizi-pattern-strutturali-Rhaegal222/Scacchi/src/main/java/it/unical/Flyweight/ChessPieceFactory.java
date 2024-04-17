package it.unical.Flyweight;

import java.util.HashMap;
import java.util.Map;

public class ChessPieceFactory {
    private final Map<String, ChessPiece> flyweights = new HashMap<>();

    public ChessPiece getChessPiece(String name, String color) {
        String key = name + "-" + color;
        flyweights.putIfAbsent(key, new ChessPiece(name, color));
        return flyweights.get(key);
    }
}
