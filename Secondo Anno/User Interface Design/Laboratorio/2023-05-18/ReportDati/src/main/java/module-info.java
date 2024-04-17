module informatica.unical.reportdati {
    requires javafx.controls;
    requires javafx.fxml;


    opens informatica.unical.reportdati to javafx.fxml;
    exports informatica.unical.reportdati;

    opens informatica.unical.reportdati.controller to javafx.fxml;
    exports informatica.unical.reportdati.controller;

    opens informatica.unical.reportdati.view to javafx.fxml;
    exports informatica.unical.reportdati.view;
}