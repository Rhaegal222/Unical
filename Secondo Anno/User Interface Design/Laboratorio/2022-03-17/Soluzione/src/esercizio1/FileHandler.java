package esercizio1;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Random;
import java.util.regex.Pattern;

public class FileHandler {
	
	private Random random = new Random();
	public FileHandler() {
	}

	private String generateRandomString(int maxLength) {
		if(maxLength <= 0)
			maxLength = 1;
		int length = random.nextInt(1, maxLength+1);
		/* Metodo alternativo per generare un carattere
		 String characters = "abcdefghijklmnopqrstuvwxyz0123456789";
		 int index = random.nextInt(characters.length());
		 char c = characters.charAt(index);
		 */
		StringBuilder builder = new StringBuilder();		
		for (int i = 0; i < length; i++) {
			char c;
			if(random.nextInt() % 3 == 0) //generiamo numeri con una probabilità maggiore
				c = (char)(random.nextInt(26) + 'a');
			else
				c = (char)(random.nextInt(10) + '0');					
			builder.append(c);
		}
		return builder.toString();
	}

	public void generateFile(String nomeFile) throws IOException {
		int numberOfLines = random.nextInt(10, 30);
		BufferedWriter writer = new BufferedWriter(new FileWriter(nomeFile));
		for (int i = 0; i < numberOfLines; i++) {
			writer.append(generateRandomString(6));
			// Non stampiamo il fine linea per l'ultimo elemento
			if (i != numberOfLines - 1)
				writer.newLine();
		}
		writer.close();		
	}

	private List<String> read(String filename) throws IOException {
		return Files.readAllLines(Path.of(filename));		
	}

	//stampaLineeNumeriche
	public void printLinesWithOnlyNumbers(String filename) throws IOException {
		read(filename).stream()
	      .filter(e -> Pattern.matches("\\d+", e)) //filter elements that are numbers
	      .forEach(System.out::println); //print lines
	}
	
	//stampaLineeConNumero
	public void printLinesWithAtLeastOneNumber(String filename) throws IOException {
		read(filename).stream()
	      .filter(e -> Pattern.matches("(\\D)*\\d+(\\D)*", e)) //filter elements with at least one number
	      .forEach(System.out::println); //print lines
	}
	
	//stampaLineeConLetterePari
	public void printLinesWithEvenOccurrencesOfLetter(String filename, char letter) throws IOException {
		read(filename).stream()
	      .filter(e -> Pattern.matches("(%s%s)+".formatted(letter, letter), e))
	      .forEach(System.out::println); //print lines
		}
	
	private long occurrences(String word, char letter) {
		return word.chars().filter(x -> x == letter).count();
	}
	
	//stampaLineeConNumeroUguale
	public void printLinesWithTheSameNumberOfOccurrences(String filename, char letter1, char letter2) throws IOException {
		read(filename).stream()
			.filter(word -> occurrences(word, letter1) == occurrences(word, letter2))
			.forEach(System.out::println);		
	} 
	
	public static void main(String[] args) {
		FileHandler g = new FileHandler();
		try {
			String filename = "file.txt";
			g.generateFile(filename);			
//			g.printLinesWithOnlyNumbers(filename);
//			g.printLinesWithAtLeastOneNumber(filename);
//			g.printLinesWithEvenOccurrencesOfLetter(filename, 'a');
//			g.printLinesWithTheSameNumberOfOccurrences(filename, 'a', 'b');
		} catch(IOException e) {
			System.err.println("Errore nella lettura del file.");
		}
	}
}
