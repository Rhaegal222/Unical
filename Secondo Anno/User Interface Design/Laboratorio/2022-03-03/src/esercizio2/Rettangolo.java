package esercizio2;

public class Rettangolo implements Disegnabile {

	private final int base;
	private final int altezza;
	
	public Rettangolo(int base, int altezza) {
		this.base = base;
		this.altezza = altezza;
	}
	
	@Override
	public void disegna() {
		System.out.println();
		for(int i = 0; i < altezza; i++) {
			for(int j = 0; j < base; j++)
				System.out.print("* ");
			System.out.println();
		}
		System.out.println();
	}

}
