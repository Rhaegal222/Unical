package it.unical.demacs.informatica.gestorelibri.controller;

import it.unical.demacs.informatica.gestorelibri.Message;
import it.unical.demacs.informatica.gestorelibri.view.SceneHandler;
import it.unical.demacs.informatica.gestorelibri.model.Book;
import it.unical.demacs.informatica.gestorelibri.model.BooksHandler;
import it.unical.demacs.informatica.gestorelibri.view.BooksHandlerView;
import javafx.beans.property.ReadOnlyStringWrapper;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
public class BookController {

    @FXML
    private TableView<Book> bookTable;

    @FXML
    private TableColumn<Book, String> author;

    @FXML
    private TableColumn<Book, String> isbn;

    @FXML
    private TableColumn<Book, String> year;

    @FXML
    private TableColumn<Book, String> publisher;

    @FXML
    private TableColumn<Book, String> title;

    @FXML
    private Button changeThemeButton;

    public void initialize() {
        bookTable.setItems(BooksHandlerView.getInstance().getBooks());
        initThemeButton();
        isbn.setCellValueFactory(s -> new ReadOnlyStringWrapper(s.getValue().isbn()));
        title.setCellValueFactory(s -> new ReadOnlyStringWrapper(s.getValue().title()));
        author.setCellValueFactory(s -> new ReadOnlyStringWrapper(s.getValue().author()));
        publisher.setCellValueFactory(s -> new ReadOnlyStringWrapper(s.getValue().publisher()));
        year.setCellValueFactory(s -> new ReadOnlyStringWrapper(s.getValue().year()));
    }

    @FXML
    void addBook(ActionEvent ignoredEvent) {
        try {
            SceneHandler.getInstance().setAddBookScene();
        } catch (Exception e) {
            SceneHandler.getInstance().showError(Message.ADD_BOOK_ERROR);
        }
    }

    @FXML
    void logout(ActionEvent ignoredEvent) {
        try {
            SceneHandler.getInstance().setLoginScene();
            BooksHandler.getInstance().logout();
        } catch (Exception e) {
            SceneHandler.getInstance().showError(Message.LOGOUT_ERROR);
        }
    }

    @FXML
    void changeTheme(ActionEvent event) {
        SceneHandler.getInstance().changeTheme();
        initThemeButton();
    }

    private void initThemeButton() {
        if(SceneHandler.getInstance().isDarkTheme())
            changeThemeButton.setText("Set light theme");
        else
            changeThemeButton.setText("Set dark theme");
    }
}
