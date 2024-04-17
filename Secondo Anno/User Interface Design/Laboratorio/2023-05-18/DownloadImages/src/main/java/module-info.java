module it.unical.demacs.informatica.downloadimages {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;


    opens it.unical.demacs.informatica.downloadimages to javafx.fxml;
    exports it.unical.demacs.informatica.downloadimages;
    exports it.unical.demacs.informatica.downloadimages.controller;
    opens it.unical.demacs.informatica.downloadimages.controller to javafx.fxml;
}