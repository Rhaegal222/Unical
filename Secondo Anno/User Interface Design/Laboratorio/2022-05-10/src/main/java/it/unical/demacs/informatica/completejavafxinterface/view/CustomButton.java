package it.unical.demacs.informatica.completejavafxinterface.view;

import javafx.scene.Node;
import javafx.scene.control.Button;

import java.util.Objects;

public class CustomButton extends Button {

    public CustomButton(Node graphic) {
        super();
        Objects.requireNonNull(graphic);
        setGraphic(graphic);
        this.setStyle("-fx-padding: 10 30 10 30;");
    }
}
