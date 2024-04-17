package it.unical.demacs.informatica.completejavafxinterface.view;

import org.kordamp.ikonli.javafx.FontIcon;

public class CustomFontIcon extends FontIcon {

    public CustomFontIcon(String name) {
        super(name);
        this.getStyleClass().add("icons-color");
    }

    public CustomFontIcon(String name, int size) {
        super(name);
        this.getStyleClass().add("icons-color");
        this.setIconSize(size);
    }
}
