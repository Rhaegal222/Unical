package informatica.unical.reportdati.model;

public class Vaccinazione {
    private String data, area, d1, d2, n1, n2, reg;
    private int totale, m, f,  dpi, db1, db2, db3, istat;

    public Vaccinazione(String data, String area, String d1, String d2, String n1, String n2, String reg, int totale, int m, int f, int dpi, int db1, int db2, int db3, int istat) {
        this.data = data;
        this.area = area;
        this.d1 = d1;
        this.d2 = d2;
        this.n1 = n1;
        this.n2 = n2;
        this.reg = reg;
        this.totale = totale;
        this.m = m;
        this.f = f;
        this.dpi = dpi;
        this.db1 = db1;
        this.db2 = db2;
        this.db3 = db3;
        this.istat = istat;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public String getD1() {
        return d1;
    }

    public void setD1(String d1) {
        this.d1 = d1;
    }

    public String getD2() {
        return d2;
    }

    public void setD2(String d2) {
        this.d2 = d2;
    }

    public String getN1() {
        return n1;
    }

    public void setN1(String n1) {
        this.n1 = n1;
    }

    public String getN2() {
        return n2;
    }

    public void setN2(String n2) {
        this.n2 = n2;
    }

    public String getReg() {
        return reg;
    }

    public void setReg(String reg) {
        this.reg = reg;
    }

    public int getTotale() {
        return totale;
    }

    public void setTotale(int totale) {
        this.totale = totale;
    }

    public int getM() {
        return m;
    }

    public void setM(int m) {
        this.m = m;
    }

    public int getF() {
        return f;
    }

    public void setF(int f) {
        this.f = f;
    }

    public int getDpi() {
        return dpi;
    }

    public void setDpi(int dpi) {
        this.dpi = dpi;
    }

    public int getDb1() {
        return db1;
    }

    public void setDb1(int db1) {
        this.db1 = db1;
    }

    public int getDb2() {
        return db2;
    }

    public void setDb2(int db2) {
        this.db2 = db2;
    }

    public int getDb3() {
        return db3;
    }

    public void setDb3(int db3) {
        this.db3 = db3;
    }

    public int getIstat() {
        return istat;
    }

    public void setIstat(int istat) {
        this.istat = istat;
    }
}
