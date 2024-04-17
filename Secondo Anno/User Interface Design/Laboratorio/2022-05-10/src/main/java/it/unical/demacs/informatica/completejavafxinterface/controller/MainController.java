package it.unical.demacs.informatica.completejavafxinterface.controller;

import it.unical.demacs.informatica.completejavafxinterface.model.Conversation;
import it.unical.demacs.informatica.completejavafxinterface.model.Email;
import it.unical.demacs.informatica.completejavafxinterface.model.MailDownloader;
import it.unical.demacs.informatica.completejavafxinterface.view.*;
import javafx.beans.binding.Bindings;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TitledPane;
import javafx.scene.control.ToolBar;

import java.util.List;
import java.util.Objects;

public class MainController {

    @FXML
    private TitledPane allInboxes;

    @FXML
    private TitledPane allSent;

    @FXML
    private TitledPane archive;

    @FXML
    private ListView<EmailView> conversationListView;

    @FXML
    private ListView<EmailPreview> emailsListView;

    @FXML
    private ToolBar toolbar;

    @FXML
    private TitledPane trash;

    private final MailDownloader mailDownloader = new MailDownloader();

    @FXML
    public void initialize() {
        allInboxes.setGraphic(new CustomFontIcon("mdi2i-inbox-multiple"));
        ListView<Label> listView = new ListView<>();
        Label unical = new Label("Mail Unical", new CustomFontIcon("mdi2i-inbox"));
        Label google = new Label("Google", new CustomFontIcon("mdi2i-inbox"));
        listView.getItems().add(unical);
        listView.getItems().add(google);
        listView.prefHeightProperty().bind(Bindings.size(listView.getItems()).multiply(35));
        allInboxes.setContent(listView);

        allSent.setGraphic(new CustomFontIcon("mdi2s-send"));
        ListView<Label> listView2 = new ListView<>();
        Label unical2 = new Label("Mail Unical", new CustomFontIcon("mdi2i-inbox"));
        Label google2 = new Label("Google", new CustomFontIcon("mdi2i-inbox"));
        listView2.getItems().add(unical2);
        listView2.prefHeightProperty().bind(Bindings.size(listView.getItems()).multiply(35));
        listView2.getItems().add(google2);
        allSent.setContent(listView2);
        archive.setGraphic(new CustomFontIcon("mdi2a-archive"));
        trash.setGraphic(new CustomFontIcon("mdi2t-trash-can"));

        toolbar.getItems().add(new CustomButton(new CustomFontIcon("mdi2e-email", 20)));
        toolbar.getItems().add(new CustomButton(new CustomFontIcon("mdi2e-email-edit", 20)));
        toolbar.getItems().add(new CustomButton(new CustomFontIcon("mdi2a-archive", 20)));
        toolbar.getItems().add(new CustomButton(new CustomFontIcon("mdi2e-email-search", 20)));

        mailDownloader.start();
        mailDownloader.setOnSucceeded(ev -> {
            if (ev.getSource().getValue() instanceof String jsonText) {
                List<Conversation> conversations = Objects.requireNonNull(Conversation.createFromJsonFile(jsonText));
                for (Conversation conversation : conversations) {
                    EmailPreview emailPreview = new EmailPreview(conversation);
                    emailsListView.getItems().add(emailPreview);
                    emailPreview.prefWidthProperty().bind(emailsListView.widthProperty().subtract(40.0));
                }

                emailsListView.setOnMousePressed(event -> {
                    EmailPreview emailPreview = emailsListView.getSelectionModel().getSelectedItem();
                    if (emailPreview != null) {
                        conversationListView.getItems().clear();
                        Conversation conversation = emailPreview.getConversation();
                        for (Email email : conversation.emails()) {
                            conversationListView.getItems().add(new EmailView(conversation, email));
                        }
                    }
                });
            }
        });

        mailDownloader.setOnFailed(event -> ErrorMessage.getInstance().showErrorMessage("Cambiare messaggio qui."));
    }

}
