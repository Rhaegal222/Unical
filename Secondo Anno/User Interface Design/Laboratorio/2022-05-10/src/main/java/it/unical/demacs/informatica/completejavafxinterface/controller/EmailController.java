package it.unical.demacs.informatica.completejavafxinterface.controller;

import it.unical.demacs.informatica.completejavafxinterface.model.Email;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

import java.util.Objects;

public class EmailController {

    @FXML
    private Label dateLabel;

    @FXML
    private Label senderLabel;

    @FXML
    private Label subjectLabel;

    @FXML
    private Label textLabel;

    @FXML
    private Label toLabel;

    public void init(String sender, String receiver, String subject, Email email) {
        Objects.requireNonNull(email);
        senderLabel.setText(Objects.requireNonNull(sender));
        dateLabel.setText(email.date());
        subjectLabel.setText(Objects.requireNonNull(subject));
        toLabel.setText("To: " + Objects.requireNonNull(receiver));
        textLabel.setText(email.text());
    }
}
