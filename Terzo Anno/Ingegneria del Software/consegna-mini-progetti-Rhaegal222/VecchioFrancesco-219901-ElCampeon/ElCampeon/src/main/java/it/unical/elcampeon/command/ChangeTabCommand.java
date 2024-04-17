package it.unical.elcampeon.command;

import it.unical.elcampeon.handler.AlertHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.AnchorPane;

import it.unical.elcampeon.handler.PathHandler;

public class ChangeTabCommand implements Command {
    private final String nameFXML;
    private final AnchorPane pane;

    private final String pathOfView = PathHandler.getInstance().getPathOfView();

    public ChangeTabCommand(String nameFXML, AnchorPane pane) {
        this.nameFXML = nameFXML;
        this.pane = pane;
    }

    @Override
    public void execute() {
        pane.getChildren().clear();
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource(pathOfView + nameFXML));
            AnchorPane newPane = loader.load();

            pane.getChildren().add(newPane);

            // Imposta il colore di sfondo trasparente del pannello
            pane.setStyle("-fx-background-color: transparent; -fx-border-color: transparent;");
            newPane.setStyle("-fx-background-color: transparent; -fx-border-color: transparent;");


            // Ancora il contenuto al bordo del pannello
            AnchorPane.setTopAnchor(pane, 0.0);
            AnchorPane.setBottomAnchor(pane, 0.0);
            AnchorPane.setLeftAnchor(pane, 0.0);
            AnchorPane.setRightAnchor(pane, 0.0);

            // Ancora il contenuto al bordo del pannello
            AnchorPane.setTopAnchor(newPane, 0.0);
            AnchorPane.setBottomAnchor(newPane, 0.0);
            AnchorPane.setLeftAnchor(newPane, 0.0);
            AnchorPane.setRightAnchor(newPane, 0.0);

        } catch (Exception e) {
            AlertHandler.getInstance().createMenuLoadErrorAlert();
        }
    }
}
