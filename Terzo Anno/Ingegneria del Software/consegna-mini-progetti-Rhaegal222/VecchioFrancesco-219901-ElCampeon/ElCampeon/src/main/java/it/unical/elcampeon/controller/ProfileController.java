package it.unical.elcampeon.controller;

import it.unical.elcampeon.command.ChangeSceneCommand;
import it.unical.elcampeon.command.ChangeTabCommand;
import it.unical.elcampeon.command.Command;
import it.unical.elcampeon.handler.*;
import it.unical.elcampeon.service.SqlQuery;
import it.unical.elcampeon.service.SqlService;
import it.unical.elcampeon.model.View;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;

import java.util.ResourceBundle;

public class ProfileController {

    boolean  isGoodName, isGoodSurname;
    private final RegexHandler regexHandler = RegexHandler.getInstance();
    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private final SceneHandler sceneHandler = SceneHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final ResourceBundle bundle = settingsHandler.getBundle();
    private final SqlQuery sqlQuery = SqlQuery.getInstance();
    private final SqlService sqlService = SqlService.getInstance();
    String [] profileInfoArray = sqlQuery.getProfileInfo(LoggedHandler.getInstance().getUsername());

    @FXML
    AnchorPane centerPage;
    @FXML
    private Label nameLabel, surnameLabel, birthdayLabel, changePassLabel, applyLabel, cancelLabel;
    @FXML
    private TextField usernameTextField, firstTextField, lastTextField,emailTextField,birthdayTextField;
    @FXML
    private Button saveButton;

    @FXML
    void onChangePasswordClick(){
        ChangeTabCommand changeTabCommand = new ChangeTabCommand("changepass-view.fxml", centerPage);
        changeTabCommand.execute();
    }
    @FXML
    void onCancelClick(){
        Command changeSceneCommand = new ChangeSceneCommand("menu-view.fxml");
        changeSceneCommand.execute();
    }
    @FXML
    void onSaveClick() {
        if (sqlService.changeUserName(firstTextField.getText(), usernameTextField.getText())) {
            sceneHandler.loadScene(new View("settings-view.fxml"));
        } else  alertHandler.createChangeNameErrorAlert();
        if (sqlService.changeUserSurname(lastTextField.getText(), usernameTextField.getText())) {
            sceneHandler.loadScene(new View("settings-view.fxml"));
        } else  alertHandler.createChangeSurnameErrorAlert();
        alertHandler.createPersonalDataChangedAlert();
    }

    @FXML
    void initialize() {
        updateLanguage();
        saveButton.setDisable(true);
        birthdayTextField.setDisable(true);
        emailTextField.setDisable(true);
        usernameTextField.setDisable(true);
        usernameTextField.setText(LoggedHandler.getInstance().getUsername());
        firstTextField.setText(profileInfoArray[0]);
        lastTextField.setText(profileInfoArray[1]);
        emailTextField.setText(profileInfoArray[2]);
        birthdayTextField.setText(profileInfoArray[3]);
        addListenerName();
        addListenerSurname();
    }


    private void addListenerName(){
        firstTextField.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodName =  newValue.matches(regexHandler.regexFirstLast) && !firstTextField.getText().equals(profileInfoArray[0]) ;
            if(firstTextField.getText().length()>=2 && lastTextField.getText().length()>=2) {
                saveButton.setDisable(!isGoodName && !isGoodSurname);
            }else{
                saveButton.setDisable(true);
            }
        });
    }
    private void addListenerSurname(){
        lastTextField.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodSurname = newValue.matches(regexHandler.regexFirstLast) && !lastTextField.getText().equals(profileInfoArray[1]) ;
            if(firstTextField.getText().length()>=2 && lastTextField.getText().length()>=2) {

                saveButton.setDisable(!isGoodName && !isGoodSurname);
            }else{
                saveButton.setDisable(true);
            }
        });
    }


    private void updateLanguage(){
        if(bundle!=null) {
            applyLabel.setText(bundle.getString("applyButton"));
            cancelLabel.setText(bundle.getString("backButton"));
            changePassLabel.setText(bundle.getString("changePasswordButton"));
            nameLabel.setText(bundle.getString("nameLabel"));
            surnameLabel.setText(bundle.getString("surnameLabel"));
            birthdayLabel.setText(bundle.getString("birthdayLabel"));
        }
    }
}
