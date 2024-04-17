module demacs.informatica.unical.it.gestorelibri {
    requires javafx.controls;
    requires javafx.fxml;
    requires org.kordamp.ikonli.javafx;


    exports it.unical.demacs.informatica.gestorelibri.controller;
    opens it.unical.demacs.informatica.gestorelibri.controller to javafx.fxml;
    exports it.unical.demacs.informatica.gestorelibri;
    opens it.unical.demacs.informatica.gestorelibri to javafx.fxml;
}