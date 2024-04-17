package it.unical.demacs.informatica.gestorelibri.controller;

import it.unical.demacs.informatica.gestorelibri.Message;
import it.unical.demacs.informatica.gestorelibri.model.Book;
import it.unical.demacs.informatica.gestorelibri.view.BooksHandlerView;
import it.unical.demacs.informatica.gestorelibri.view.SceneHandler;
import it.unical.demacs.informatica.gestorelibri.model.BooksHandler;
import it.unical.demacs.informatica.gestorelibri.model.User;
import it.unical.demacs.informatica.gestorelibri.model.UsersReader;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

import java.util.List;

public class LoginController {

    @FXML
    private PasswordField password;

    @FXML
    private TextField username;

    @FXML
    void checkUsername(ActionEvent ignoredEvent) {
        String user = username.getText();
        String pass = password.getText();
        if(UsersReader.getInstance().checkAccess(user, pass)) {
            List<Book> booksList = BooksHandler.getInstance().login(new User(user));
            for(Book book : booksList)
                BooksHandlerView.getInstance().addBook(book);
            try {
                SceneHandler.getInstance().setBookScene();
            } catch (Exception e) {
                SceneHandler.getInstance().showError(Message.LOAD_BOOKS_ERROR);
            }
        }
        else {
            SceneHandler.getInstance().showError(Message.WRONG_USER_PASS);
        }
    }

}
