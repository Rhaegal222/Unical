package esercizio2;

public class LibreriaGrafica {
	
	private Disegnabile[] elementi;
	private int size;
	
	public LibreriaGrafica() {
		elementi = new Disegnabile[1];
		size = 0;
	}
	
	public void aggiungi(Disegnabile d) {
		if(size == elementi.length) {
			Disegnabile[] tmp = new Disegnabile[elementi.length*2];
			System.arraycopy(elementi, 0, tmp, 0, elementi.length);
			elementi = tmp;
		}
		elementi[size]=d;
		size++;
	}
	
	public void rimuovi(Disegnabile d) {
		int j = 0;
		for(int i = 0; i < size; i++) {
			elementi[j] = elementi[i];
			if(d != elementi[i]) //Controlliamo il riferimento
				j++;
		}
		for(int i = size; i < elementi.length; i++)
			elementi[i] = null;
		size = j;
	}
	
	public void disegnaElementi() {
		for(int i = 0; i < size; i++) {
			elementi[i].disegna();
		}
	}
	
	public static void main(String[] args) {
		LibreriaGrafica lib = new LibreriaGrafica();
		Quadrato q1 = new Quadrato(4);
		Disegnabile d1 = new Quadrato(8);
		Rettangolo r1 = new Rettangolo(4, 5);
		lib.aggiungi(q1);
		lib.aggiungi(d1);
		lib.aggiungi(r1);
		lib.aggiungi(d1);
		lib.disegnaElementi();
		lib.rimuovi(d1);
		lib.disegnaElementi();		
	}
}
