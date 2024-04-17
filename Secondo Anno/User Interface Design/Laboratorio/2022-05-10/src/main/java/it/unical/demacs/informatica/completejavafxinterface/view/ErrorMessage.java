package it.unical.demacs.informatica.completejavafxinterface.view;

import it.unical.demacs.informatica.completejavafxinterface.Main;
import it.unical.demacs.informatica.completejavafxinterface.Settings;
import javafx.scene.control.Alert;

import java.util.Objects;

public class ErrorMessage {

    private static ErrorMessage instance = new ErrorMessage();

    private final Alert alert;

    private ErrorMessage() {
        alert = new Alert(Alert.AlertType.ERROR);
        for (String style : Settings.styles)
            alert.getDialogPane().getStylesheets().add(Objects.requireNonNull(Main.class.getResource(style)).toExternalForm());
    }

    public static ErrorMessage getInstance() {
        return instance;
    }

    public void showErrorMessage(String text) {
        alert.setTitle("Errore");
        alert.setHeaderText(null);
        alert.setContentText(text);
        alert.showAndWait();
    }
}
