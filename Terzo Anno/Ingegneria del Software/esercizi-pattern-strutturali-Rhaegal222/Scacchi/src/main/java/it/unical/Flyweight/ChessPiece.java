package it.unical.Flyweight;

public class ChessPiece {
    private final String name; // Nome del pezzo (es. Pedone, Torre)
    private final String color; // Colore del pezzo (Bianco o Nero)

    public ChessPiece(String name, String color) {
        this.name = name;
        this.color = color;
    }

    public void display(int x, int y) {
        // Metodo per visualizzare il pezzo sulla scacchiera
        System.out.println("Collocamento " + name + " di colore " + color + " in posizione (" + x + "," + y + ")");
    }
}
