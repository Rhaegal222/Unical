package it.unical.demacs.informatica.completejavafxinterface.view;

import it.unical.demacs.informatica.completejavafxinterface.Main;
import it.unical.demacs.informatica.completejavafxinterface.controller.EmailController;
import it.unical.demacs.informatica.completejavafxinterface.model.Conversation;
import it.unical.demacs.informatica.completejavafxinterface.model.Email;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;

public class EmailView extends StackPane {

    public EmailView(Conversation conversation, Email email) {
        FXMLLoader loader = new FXMLLoader(Main.class.getResource("view/email.fxml"));
        try {
            VBox root = loader.load();
            EmailController controller = loader.getController();
            controller.init(conversation.sender(), conversation.receiver(), conversation.subject(), email);
            this.getChildren().add(root);
        } catch (Exception ignoredException) {
        }
    }
}
