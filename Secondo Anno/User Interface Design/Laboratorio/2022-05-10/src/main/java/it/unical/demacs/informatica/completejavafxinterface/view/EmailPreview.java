package it.unical.demacs.informatica.completejavafxinterface.view;

import it.unical.demacs.informatica.completejavafxinterface.Main;
import it.unical.demacs.informatica.completejavafxinterface.controller.EmailPreviewController;
import it.unical.demacs.informatica.completejavafxinterface.model.Conversation;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;

import java.util.Objects;

public class EmailPreview extends StackPane {

    private final Conversation conversation;

    public EmailPreview(Conversation conversation) {
        this.conversation = Objects.requireNonNull(conversation);
        FXMLLoader loader = new FXMLLoader(Main.class.getResource("view/email_preview.fxml"));
        try {
            VBox root = loader.load();
            EmailPreviewController controller = loader.getController();
            controller.init(conversation);
            this.getChildren().add(root);
            root.prefWidthProperty().bind(this.widthProperty());
        } catch(Exception ignoredException) {
        }
    }

    public Conversation getConversation() {
        return conversation;
    }
}
