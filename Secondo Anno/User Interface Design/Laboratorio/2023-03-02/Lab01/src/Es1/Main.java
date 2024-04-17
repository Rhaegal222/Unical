package Es1;

public class Main { //la classe main piglia solo una funzione e ogni classe deve avere il suo file cit. YanMark

    static int[] v = new int[10];
    public static void Stampa() {
        for (int j : v) System.out.print(j + " ");
        System.out.println();
    }

    public static int getMax() {
        Ordina(false);
        return v[0];
    }

    public static int getMin() {
        Ordina();
        return v[0];
    }

    public static void Ordina(boolean c) {
        if (!c) { //decrescente
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (i != j) if (v[i] > v[j]) {
                        int temp = v[i];
                        v[i] = v[j];
                        v[j] = temp;
                    }
                }
            }
        } else {
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (i != j) if (v[i] < v[j]) {
                        int temp = v[i];
                        v[i] = v[j];
                        v[j] = temp;
                    }
                }
            }
        }
    }

    public static void Ordina() { //crescente
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (i != j) if (v[i] < v[j]) {
                    int temp = v[i];
                    v[i] = v[j];
                    v[j] = temp;
                }
            }
        }
    }

    public static int getSomma() {
        int somma = 0;
        for (int n : v) somma += n;
        return somma;
    }

    public static Double getMedia() {
        double somma = getSomma();
        return somma / v.length;
    }

    public static boolean isPrimo(int n) {
        boolean c = n > 1;
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return c;
    }

    public static void printPrimo() {
        for (int n : v) {
            if (isPrimo(n)) System.out.print(n + " ");
        }
    }

        public static void main (String[]args){


            for (int i = 0; i < 10; ++i) v[i] = i;

            //2
            System.out.print("Array: ");
            Stampa();

            //3
            System.out.println("Massimo: " + getMax());

            //4
            System.out.println("Minimo: " + getMin());

            //5
            System.out.println("Media: " + getMedia());

            //6
            Ordina();
            System.out.print("Array crescente: ");
            Stampa();

            //7
            Ordina(false);
            System.out.print("Array decrescente: ");
            Stampa();

            //8
            System.out.print("Numeri primi: ");
            printPrimo();

        }
}