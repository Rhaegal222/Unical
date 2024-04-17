package it.unical.demacs.informatica.completejavafxinterface.controller;

import it.unical.demacs.informatica.completejavafxinterface.model.Conversation;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;

public class EmailPreviewController {

    @FXML
    private Label dateLabel;

    @FXML
    private Label senderLabel;

    @FXML
    private Label secondLine;

    @FXML
    private Label thirdLine;

    @FXML
    private VBox vBox;

    public void init(Conversation conversation) {
        senderLabel.setText(conversation.sender());
        dateLabel.setText(conversation.getLastEmail().date());
        secondLine.setText(conversation.subject());
        thirdLine.setText(conversation.getLastEmail().text());
        secondLine.setMaxWidth(vBox.getWidth());
        vBox.widthProperty().addListener((obs, oldValue, newValue) -> {
            secondLine.setMaxWidth(newValue.doubleValue());
            secondLine.setPrefWidth(newValue.doubleValue());
        });
    }
}
