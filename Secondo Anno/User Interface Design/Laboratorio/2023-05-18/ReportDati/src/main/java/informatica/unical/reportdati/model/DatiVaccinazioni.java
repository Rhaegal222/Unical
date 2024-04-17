package informatica.unical.reportdati.model;

import java.util.ArrayList;

public class DatiVaccinazioni {
    private ArrayList<Vaccinazione> dati = new ArrayList<>();
    public boolean addVaccinazione(Vaccinazione vax){
        if(vax!=null) {
            dati.add(vax);
            return true;
        }
        else return false;
    }

}
