module it.unical.demacs.informatica.completejavafxinterface {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;
    requires org.kordamp.ikonli.javafx;
    requires json;


    opens it.unical.demacs.informatica.completejavafxinterface to javafx.fxml;
    exports it.unical.demacs.informatica.completejavafxinterface;
    exports it.unical.demacs.informatica.completejavafxinterface.model;
    opens it.unical.demacs.informatica.completejavafxinterface.model to javafx.fxml;
    exports it.unical.demacs.informatica.completejavafxinterface.view;
    opens it.unical.demacs.informatica.completejavafxinterface.view to javafx.fxml;
    exports it.unical.demacs.informatica.completejavafxinterface.controller;
    opens it.unical.demacs.informatica.completejavafxinterface.controller to javafx.fxml;
}