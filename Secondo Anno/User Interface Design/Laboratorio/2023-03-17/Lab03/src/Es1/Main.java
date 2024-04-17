package Es1;

import Es1.FileManager;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        FileManager file = new FileManager();
        file.generaFile("prova");
        file.stampaLineeConLetterePari("prova",'c');
        file.stampaLineeConLetterePari("prova",'h');
        file.stampaLineeConNumeroUguale("prova",'c','h');
        file.stampaLineeNumeriche("prova");

    }
}