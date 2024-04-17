package it.unical.demacs.informatica.gestorelibri.controller;

import it.unical.demacs.informatica.gestorelibri.Message;
import it.unical.demacs.informatica.gestorelibri.view.SceneHandler;
import it.unical.demacs.informatica.gestorelibri.model.Book;
import it.unical.demacs.informatica.gestorelibri.model.BooksHandler;
import it.unical.demacs.informatica.gestorelibri.view.BooksHandlerView;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class AddBookController {

    @FXML
    private TextField year;

    @FXML
    private TextField author;

    @FXML
    private TextField isbn;

    @FXML
    private TextField publisher;

    @FXML
    private TextField title;

    @FXML
    void addBook(ActionEvent ignoredEvent) {
        try {
            Book b = new Book(isbn.getText(), title.getText(), author.getText(), publisher.getText(), year.getText());
            if (BooksHandler.getInstance().addBook(b)) {
                BooksHandlerView.getInstance().addBook(b);
                SceneHandler.getInstance().showInfo(Message.ADDED_BOOK);
                isbn.setText("");
                author.setText("");
                publisher.setText("");
                title.setText("");
                year.setText("");
            } else {
                SceneHandler.getInstance().showError(Message.ADD_BOOK_ERROR);
            }
        } catch(IllegalArgumentException ignoredException) {
            SceneHandler.getInstance().showError(Message.ALL_FIELDS_ARE_MANDATORY);
        }

    }

}
