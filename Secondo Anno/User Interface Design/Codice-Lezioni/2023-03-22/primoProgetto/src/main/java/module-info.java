module it.unical.demacs.informatica.primoprogetto {
    requires javafx.controls;
    requires javafx.fxml;


    opens it.unical.demacs.informatica.primoprogetto to javafx.fxml;
    exports it.unical.demacs.informatica.primoprogetto;
}