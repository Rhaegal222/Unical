package it.unical.demacs.informatica.downloadimages.controller;

import it.unical.demacs.informatica.downloadimages.model.DownloadHandler;
import it.unical.demacs.informatica.downloadimages.view.SceneHandler;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class MainController {

    @FXML
    private TextField searchBar;

    @FXML
    void search(ActionEvent event) {
        DownloadHandler.download(searchBar.getText());
    }

}
