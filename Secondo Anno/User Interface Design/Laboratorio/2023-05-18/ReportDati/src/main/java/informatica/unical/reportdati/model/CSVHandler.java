package informatica.unical.reportdati.model;

import javafx.concurrent.Service;
import javafx.concurrent.Task;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.net.URL;

public class CSVHandler extends Service<DatiVaccinazioni> {

    @Override
    protected Task<DatiVaccinazioni> createTask() {
        return new Task<DatiVaccinazioni>() {
            @Override
            protected DatiVaccinazioni call() throws Exception {
                String data = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv";
                URL csvData = new URL(data);
                BufferedReader reader = new BufferedReader(new InputStreamReader(csvData.openStream()));

                String line = null;

                while(line == reader.readLine() && line != null){
                    System.out.println(line);
                }
                return null;
            }
        };
    }
}
