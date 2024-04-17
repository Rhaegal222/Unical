package esercizio2;
import java.util.Scanner;

public class contaCifre {
    public static void main (String[] args) {
        Scanner in=new Scanner(System.in);
        int numero, cont = 0;
        System.out.print("Inserisci il numero: ");
        numero = in.nextInt();
        do{
            numero=numero/10;
            cont ++;
        }while(numero>0);
        System.out.println(cont);
    }
}
