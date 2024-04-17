package store;

import java.util.Objects;

public record Product (String id, String type, String brand, String model, int year, double price) implements Comparable<Product> {
	public Product(String id, String type, String brand, String model, int year, double price) {
		Objects.requireNonNull(id);
		Objects.requireNonNull(type);
		Objects.requireNonNull(brand);
		Objects.requireNonNull(model);
		if(year < 1900 || year > 2050)
			throw new IllegalArgumentException("Year is not in valid range");
		if(price < 0.0)
			throw new IllegalArgumentException("Price cannot be negative");		
		this.id = id;
		this.type = type;
		this.brand = brand;
		this.model = model;
		this.year = year;
		this.price = price;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Product other = (Product) obj;
		return Objects.equals(id, other.id);
	}

	@Override
	public int compareTo(Product o) {
		if(price < o.price)
			return -1;
		return price > o.price ? 1 : 0;
	}

	@Override
	public String toString() {
		return id + ";" + type + ";" + brand + ";" + model + ";" + year + ";" + price;
	}	
}
