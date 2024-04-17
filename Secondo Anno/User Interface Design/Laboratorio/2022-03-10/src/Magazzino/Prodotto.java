package Magazzino;

import java.util.Objects;

public class Prodotto {

    String id;
    String type;
    String brand;
    String model;
    Integer year;
    Double price;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Prodotto prodotto = (Prodotto) o;
        return Objects.equals(id, prodotto.id);//  Objects.equals(type, prodotto.type) && Objects.equals(brand, prodotto.brand) && Objects.equals(model, prodotto.model) && Objects.equals(year, prodotto.year) && Objects.equals(productionYear, prodotto.productionYear) && Objects.equals(price, prodotto.price);
    }

    public String getId() {
        return id;
    }

    public String getType() {
        return type;
    }

    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public Integer getYear() {
        return year;
    }

    public Double getPrice() {
        return price;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, type, brand, model, year, price);
    }

    public Prodotto(String id, String type, String brand, String model, Integer year, Double price) {
        this.id = id;
        this.type = type;
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.price = price;
    }

}
