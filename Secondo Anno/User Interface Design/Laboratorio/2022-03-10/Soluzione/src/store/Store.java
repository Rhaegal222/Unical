package store;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Store {

	private List<Product> products;
	
	public Store() {
		products = new ArrayList<>();
	}	

	public boolean addProduct(Product p) {
		if (products.contains(p))
			return false;
		products.add(p);
		return true;
	}

	public boolean removeProduct(String id) {		
		return products.remove(new Product(id, "", "", "", 2020, 1.0));
	}

	public List<Product> searchByBrand(String brand) {		
		List<Product> tmp = new ArrayList<>();
		for(Product p : products) {
			if(p.brand().equals(brand))
				tmp.add(p);
		}
		return tmp;
	}
	
	public List<Product> searchByModel(String model) {		
		List<Product> tmp = new ArrayList<>();
		for(Product p : products) {
			if(p.model().equals(model))
				tmp.add(p);
		}
		return tmp;
	}
	
	public List<Product> searchByType(String type) {		
		List<Product> tmp = new ArrayList<>();
		for(Product p : products) {
			if(p.type().equals(type))
				tmp.add(p);
		}
		return tmp;
	}
	
	public void sortAscending() {
		products.sort(Comparator.naturalOrder());
	}
	
	public void sortDescending() {
		products.sort(Comparator.reverseOrder());
	}

	public void print() {
		System.out.println("Tutti i prodotti:");
		for (Product p : products) {
			System.out.println(p);
		}
	}

	public void readFromFile(String name) throws IOException {
		List<String> lines;
		try {
			lines = Files.readAllLines(Path.of(name));
			for(String line : lines) {
				String[] splitLine = line.split(";");
				addProduct(new Product(splitLine[0], splitLine[1], splitLine[2], splitLine[3], Integer.parseInt(splitLine[4]), Double.parseDouble(splitLine[5])));
			}
		}
		catch(FileNotFoundException e) {
			throw new IOException("File " + name + " non esiste");
		}
		catch(IOException e) {
			throw new IOException("Impossibile leggere il file " + name);
		}
		catch(Exception e) {
			throw new IOException("File " + name + "non conforme alle specifiche");
		}
	}

	public void saveToFile(String name) throws IOException {
		StringBuilder builder = new StringBuilder();
		for(Product p : products) {
			builder.append(p.toString());
		}
		try {			
			Files.writeString(Path.of(name), builder.toString());
		} catch(IOException e) {
			e.printStackTrace();
			throw new IOException("Impossibile scrivere sul file " + name);
		}
	}
}
