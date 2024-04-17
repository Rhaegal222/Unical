package Es1;

public class Prodotto implements Comparable<Prodotto>{
    private String id, type, brand, model;

    private int dop;

    private double price;

    public Prodotto(){}

    public Prodotto(String id, String type, String brand, String model, int dop, double price){
        if(dop>=1900 && dop<=2050){
            this.dop = dop;
        }
        else{
            System.out.println("Data di produzione non valida");
            return;
        }
        if(price>0.0){
            this.price = price;
        }
        else{
            System.out.println("Prezzo non valido");
            return;
        }
        this.id = id; this.type = type; this.brand = brand; this.model = model;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getDop() {
        return dop;
    }

    public void setDop(int dop) {
        if(dop>=1900 && dop<=2050){
            this.dop = dop;
        }
        else{
            System.out.println("Data di produzione non valida");
        }
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if(price>0.0){
            this.price = price;
        }
        else{
            System.out.println("Prezzo non valido");
        }
    }

    @Override
    public int compareTo(Prodotto o) {
        return String.valueOf(this.getPrice()).compareTo(String.valueOf(o.getPrice()));
    }

    @Override
    public String toString(){
        String s = "";
        s+=(this.getId()+" ");
        s+=(this.getType()+" ");
        s+=(this.getBrand()+" ");
        s+=(this.getModel()+" ");
        s+=(this.getDop()+" ");
        s+=(this.getPrice()+" ");
        s+="\n";
        return s;
    }
}
