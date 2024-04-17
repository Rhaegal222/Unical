package store;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	private final static String ID = "l'id";
	private final static String BRAND = "la marca";
	private final static String MODEL = "il modello";
	private final static String TYPE = "il tipo";

	private Scanner scanner = new Scanner(System.in);
	private Store store = new Store();

	private int readYear() {
		int anno;
		do {
			System.out.println("Inserisci l'anno del prodotto (compreso tra 1900 e 2050)");
			anno = scanner.nextInt();
		} while (anno < 1900 || anno > 2050);
		return anno;
	}

	private double readPrice() {
		double prezzo;
		do {
			System.out.println("Inserisci il prezzo del prodotto (>= 0.0)");
			prezzo = scanner.nextDouble();
		} while (prezzo < 0.0);
		return prezzo;
	}

	private String read(String name) {
		System.out.println("Inserisci " + name + " del prodotto");
		return scanner.next();
	}

	private void addProduct() {
		String id = read(ID);
		String type = read(TYPE);
		String brand = read(BRAND);
		String model = read(MODEL);
		int year = readYear();
		double price = readPrice();
		Product p = new Product(id, type, brand, model, year, price);
		if (store.addProduct(p))
			System.out.println("Prodotto inserito");
		else
			System.out.println("Prodotto già presente");
	}

	private void removeProduct() {
		String id = read("l'id");
		if (store.removeProduct(id))
			System.out.println("Eliminazione riuscita");
		else
			System.out.println("Prodotto non trovato");
	}

	private void findBy(String str) {
		List<Product> res =
		switch(str) {
		case BRAND -> store.searchByBrand(read(str));
		case MODEL -> store.searchByModel(read(str));
		case TYPE -> store.searchByType(read(str));
		default -> new ArrayList<Product>();
		};		
		System.out.println("Risultato della ricerca:");
		for(Product p : res) {
			System.out.println(p);
		}
	}	

	private void readFromFile() {
		System.out.println("Inserisci il percorso e il nome del file");
		String name = scanner.next();
		try {
			store.readFromFile(name);
			System.out.println("Lettura completata");
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
	}
	
	private void saveToFile() {
		System.out.println("Inserisci il percorso e il nome del file");
		String name = scanner.next();
		try {
			store.saveToFile(name);
			System.out.println("Salvataggio completato");
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}		
	}

	private void printMenu() {
		String menu = """
				***********************
				Premi 1 per aggiungere un prodotto.
				Premi 2 per rimuovere un prodotto.
				Premi 3 per cercare tutti i prodotti di una marca.
				Premi 4 per cercare tutti i prodotti di un modello.
				Premi 5 per cercare tutti i prodotti di un tipo.
				Premi 6 per ordinare i prodotti per prezzo (dal più economico al più caro).
				Premi 7 per ordinare i prodotti per prezzo (dal più caro al più economico).
				Premi 8 per stampare tutti i prodotti.
				Premi 9 per leggere da file.
				Premi 10 per salvare su file.
				Premi 0 per uscire.
				***********************

				""";
		System.out.println(menu);
	}

	public void launch() {
		int i;
		do {
			printMenu();
			i = scanner.nextInt();
			switch (i) {
			case 1 -> addProduct();
			case 2 -> removeProduct();
			case 3 -> findBy(BRAND);
			case 4 -> findBy(MODEL);
			case 5 -> findBy(TYPE);
			case 6 -> { store.sortAscending(); System.out.println("Ordinamento effettuato"); }
			case 7 -> { store.sortDescending(); System.out.println("Ordinamento effettuato"); }
			case 8 -> store.print();
			case 9 -> readFromFile();
			case 10 -> saveToFile();
			case 0 -> System.out.println("Arrivederci!");
			default -> {
				System.err.println("Attenzione scelta non valida");
				printMenu();
			}
			}
		} while (i != 0);
	}

	public static void main(String[] args) {
		Main m = new Main();
		m.launch();
	}
}
