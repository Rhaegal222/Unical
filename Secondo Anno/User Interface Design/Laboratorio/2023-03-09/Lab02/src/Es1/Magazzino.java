package Es1;

import java.util.*;

public class Magazzino {
    private List<Prodotto> warehouse = new ArrayList<>();

    public int searchProduct(String id){
        if(warehouse.isEmpty()) return 0;
        for(Prodotto item:warehouse){
            if(item.getId().equals(id)) return warehouse.indexOf(item);
        }
        return warehouse.size();
    }

    public void searchProductByBrand(String brand){
        for(Prodotto item:warehouse){
            if(item.getBrand().equals(brand)) {
                System.out.print(item);
            }
        }
    }

    public void searchProductByModel(String model){
        for(Prodotto item:warehouse){
            if(item.getModel().equals(model)) {
                System.out.print(item);
            }
        }
    }

    public void searchProductByDot(int dop){
        for(Prodotto item:warehouse){
            if(item.getDop()==dop){
                System.out.print(item);
            }
        }
    }

    public boolean addProduct(String id, String type, String brand, String model, int dop, double price){
        if(searchProduct(id)==warehouse.size()){
            Prodotto item = new Prodotto(id, type, brand, model, dop, price);
            warehouse.add(item);
            return true;
        }
        return false;
    }

    public boolean addProduct(Prodotto item){
        if(searchProduct(item.getId())==warehouse.size()){
            warehouse.add(item);
            return true;
        }
        return false;
    }

    public void addProduct() {
        Scanner input = new Scanner(System.in);
        System.out.print("Inserisci l'id del prodotto: ");
        String id = input.next();
        while(searchProduct(id)!=warehouse.size()){
            System.out.print("Id già presente, inserisci un id diverso");
                id = input.next();
            }
        System.out.print("Inserisci la tipologia del prodotto: ");
        String type = input.next();
        System.out.print("Inserisci la marca del prodotto: ");
        String brand = input.next();
        System.out.print("Inserisci il modello del prodotto: ");
        String model = input.next();
        System.out.print("Inserisci l'anno di produzione del prodotto (compreso fra 1900 e 2050): ");
        int dop = input.nextInt();
        while (dop < 1900 || dop > 2050) {
            System.out.print("La data deve essere compresa fra 1900 e 2050");
            dop = input.nextInt();
        }
        System.out.print("Inserisci il prezzo del prodotto: ");
        double price = input.nextDouble();

        Prodotto p = new Prodotto(id, type, brand, model, dop, price);
        warehouse.add(p);
        System.out.println("Prodotto aggiunto.");
    }

    public boolean removeProduct(String id){
        int index = searchProduct(id);
        if(index!=warehouse.size()){
            warehouse.remove(index);
            return true;
        }
        return false;
    }

    public void sortByAscendingPrice(){
        Collections.sort(warehouse);
    }

    public void sortByDescendingPrice(){
        Collections.sort(warehouse,Collections.reverseOrder());
    }

    public void printAllProducts(){
        for(Prodotto item:warehouse){
            System.out.print(item);
        }
    }
}
