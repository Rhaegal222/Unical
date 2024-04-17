package it.unical.elcampeon.controller;

import it.unical.elcampeon.command.ChangeSceneCommand;
import it.unical.elcampeon.command.Command;
import it.unical.elcampeon.handler.*;
import it.unical.elcampeon.service.SqlQuery;
import it.unical.elcampeon.service.SqlService;
import it.unical.elcampeon.model.View;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.text.Font;

import java.util.ResourceBundle;

public class ChangePassController {
    private final SceneHandler sceneHandler = SceneHandler.getInstance();
    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private final SqlService sqlService = SqlService.getInstance();
    private final RegexHandler regexHandler = RegexHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final ResourceBundle bundle = settingsHandler.getBundle();
    private final String pathOfFont = PathHandler.getInstance().getPathOfFont();
    private boolean isGoodOldPassword = false;
    private boolean isGoodPassword = false;

    @FXML
    private Button changeButton;
    @FXML
    private Label eyeIconOldPassword, eyeIconNewPassword;
    @FXML
    private Label newPasswordLabel, oldPasswordLabel, changeButtonLabel, backButtonLabel;
    @FXML
    private PasswordField oldPassPasswordField, newPassPasswordField;
    @FXML
    private TextField oldPasswordTextField, newPasswordTextField;

    @FXML
    void onCancelClick() {
        Command changeSceneCommand = new ChangeSceneCommand("menu-view.fxml");
        changeSceneCommand.execute();
    }

    @FXML
    void onChangeClick() {
        if (sqlService.changeUserPassword(newPasswordTextField.getText(), LoggedHandler.getInstance().getUsername())) {
            alertHandler.createPasswordChangedAlert();
            sceneHandler.loadScene(new View("settings-view.fxml"));
        }
        else {
            alertHandler.createChangePassErrorAlert();
        }
    }

    @FXML
    void initialize() {
        uploadLanguage();
        changeButton.setDisable(true);
        addListenerOldPassword();
        addListenerNewPassword();
        Font font = Font.loadFont(String.valueOf(getClass().getResource(pathOfFont+"fa-solid-900.ttf")), 16);
        eyeIconOldPassword.setFont(font);
        eyeIconOldPassword.setText("\uF070");
        eyeIconNewPassword.setFont(font);
        eyeIconNewPassword.setText("\uF070");
    }

    @FXML
    void showNewPassword() {
        eyeIconNewPassword.setText("\uF06E");
        newPasswordTextField.setText(newPassPasswordField.getText());
        newPassPasswordField.setVisible(false);
        newPasswordTextField.setDisable(false);
    }
    @FXML
    void hideNewPassword(){
        eyeIconNewPassword.setText("\uF070");
        newPasswordTextField.setText(newPassPasswordField.getText());
        newPassPasswordField.setVisible(true);
        newPasswordTextField.setDisable(true);
    }
    @FXML
    void showOldPassword() {
        eyeIconOldPassword.setText("\uF06E");
        oldPasswordTextField.setText(oldPassPasswordField.getText());
        oldPassPasswordField.setVisible(false);
    }
    @FXML
    void hideOldPassword(){
        eyeIconOldPassword.setText("\uF070");
        oldPasswordTextField.setText(oldPassPasswordField.getText());
        oldPassPasswordField.setVisible(true);
    }

    private void addListenerOldPassword(){
        oldPassPasswordField.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodOldPassword = SqlQuery.getInstance().checkPassword(LoggedHandler.getInstance().getUsername(), oldPassPasswordField.getText());
            if (isGoodOldPassword && isGoodPassword){
                newPassPasswordField.setDisable(false);
                eyeIconNewPassword.setDisable(false);
                changeButton.setDisable(false);
            } else if (isGoodOldPassword){
                newPassPasswordField.setDisable(false);
                eyeIconNewPassword.setDisable(false);
                changeButton.setDisable(true);
            } else {
                newPassPasswordField.setText("");
                newPasswordTextField.setText("");
                newPassPasswordField.setDisable(true);
                eyeIconNewPassword.setDisable(true);
                changeButton.setDisable(true);
            }
        });
    }

    private void addListenerNewPassword(){
        newPassPasswordField.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodPassword = newValue.matches(regexHandler.regexPassword) && (!newPassPasswordField.getText().equals(oldPassPasswordField.getText()));
            changeButton.setDisable(!isGoodPassword || !isGoodOldPassword);
        });
    }

    private void uploadLanguage(){
        backButtonLabel.setText(bundle.getString("backButton"));
        changeButtonLabel.setText(bundle.getString("applyButton"));
        oldPasswordLabel.setText(bundle.getString("oldPassLabel"));
        newPasswordLabel.setText(bundle.getString("newPassLabel"));
        newPasswordTextField.setTooltip(new Tooltip(bundle.getString("tooltipPassword")));
    }

}