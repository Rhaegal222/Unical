package informatica.unical.reportdati.controller;

import javafx.fxml.FXML;
import javafx.scene.chart.BarChart;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;

public class AppController {

    @FXML
    private BarChart<?, ?> barChart;

    @FXML
    private DatePicker endDate;

    @FXML
    private Button processData;

    @FXML
    private TextField region;

    @FXML
    private DatePicker startDate;

}

