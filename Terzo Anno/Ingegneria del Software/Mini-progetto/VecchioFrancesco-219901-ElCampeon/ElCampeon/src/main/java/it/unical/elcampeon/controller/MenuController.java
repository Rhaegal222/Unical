package it.unical.elcampeon.controller;

import it.unical.elcampeon.command.ChangeTabCommand;
import it.unical.elcampeon.handler.*;
import it.unical.elcampeon.model.Settings;
import it.unical.elcampeon.service.SqlQuery;
import it.unical.elcampeon.service.SqlService;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.HBox;
import javafx.scene.text.Font;

import java.util.ResourceBundle;

public class MenuController {
    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    String pathOfFont = PathHandler.getInstance().getPathOfFont();
    private final LoggedHandler loggedHandler = LoggedHandler.getInstance();
    private final SqlService sqlService = SqlService.getInstance();
    private final SqlQuery sqlQuery = SqlQuery.getInstance();
    private final ResourceBundle bundle = settingsHandler.getBundle();
    private final Font font = Font.loadFont(getClass().getResourceAsStream(pathOfFont + "fa-solid-900.ttf"), 20);

    @FXML
    private AnchorPane anchorPane;
    @FXML
    private Label settingsLabel, userLabel, logoutLabel, homeLabel;
    @FXML
    private Label logoutIcon, settingIcon, userIcon, homeIcon;
    @FXML
    private HBox settingsButton, profileButton, logoutButton, homeButton;

    @FXML
    void onLogoutClick(){
        alertHandler.createLogoutAlert();
    }
    @FXML
    void onSettingsClick(){
        settingsButton.setDisable(true);
        profileButton.setDisable(false);
        logoutButton.setDisable(false);
        homeButton.setDisable(false);

        ChangeTabCommand changeTabCommand = new ChangeTabCommand("settings-view.fxml", anchorPane);
        changeTabCommand.execute();
    }

    @FXML
    void onAccountClick(){
        settingsButton.setDisable(false);
        profileButton.setDisable(true);
        logoutButton.setDisable(false);
        homeButton.setDisable(false);

        ChangeTabCommand changeTabCommand = new ChangeTabCommand("profile-view.fxml", anchorPane);
        changeTabCommand.execute();
    }

    @FXML
    void onHomeClick(){
        settingsButton.setDisable(false);
        profileButton.setDisable(false);
        logoutButton.setDisable(false);
        homeButton.setDisable(true);

        ChangeTabCommand changeTabCommand = new ChangeTabCommand("home-view.fxml", anchorPane);
        changeTabCommand.execute();
    }

    @FXML
    void initialize() {
        String username = loggedHandler.getUsername();
        Settings settings = sqlService.getUserSettings(username);
        settingsHandler.updateSettings(settings);
        updateLanguage();
        loadFont();
        loadNameUsername();
        homeButton.setDisable(true);

        ChangeTabCommand changeTabCommand = new ChangeTabCommand("home-view.fxml", anchorPane);
        changeTabCommand.execute();
    }

    private void loadFont(){
        // Icona per la home
        homeIcon.setText("\uF015");
        homeIcon.setFont(font);

        // Icona per l'utente
        userIcon.setText("\uF007");
        userIcon.setFont(font);

        // Icona del bottone dei settings
        settingIcon.setText("\uF013");
        settingIcon.setFont(font);

        //Icona del bottone del logout
        logoutIcon.setText("\uF2F5");
        logoutIcon.setFont(font);
    }

    private void loadNameUsername(){
        try{
            String[] nameSurname = sqlQuery.getNameSurname(LoggedHandler.getInstance().getUsername());
            String first = nameSurname[0];
            String last = nameSurname[1];
            userLabel.setText(" " + first + " " + last);
        } catch (Exception e){
            throw new RuntimeException();
        }
    }

    private void updateLanguage(){
        if(bundle!=null) {
            settingsLabel.setText(bundle.getString("settingsLabel"));
            logoutLabel.setText(bundle.getString("logoutLabel"));
        }
    }
}


