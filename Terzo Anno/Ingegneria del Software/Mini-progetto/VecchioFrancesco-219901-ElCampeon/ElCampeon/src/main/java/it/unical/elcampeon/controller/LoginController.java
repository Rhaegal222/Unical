package it.unical.elcampeon.controller;

import it.unical.elcampeon.command.ChangeSceneCommand;
import it.unical.elcampeon.command.Command;
import it.unical.elcampeon.command.LoginCommand;
import it.unical.elcampeon.handler.*;
import it.unical.elcampeon.model.Settings;
import it.unical.elcampeon.service.SqlService;
import it.unical.elcampeon.model.View;
import javafx.application.Platform;
import javafx.beans.binding.BooleanBinding;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.image.ImageView;
import javafx.scene.text.Font;

import java.util.HashMap;
import java.util.ResourceBundle;

public class LoginController {
    @FXML
    private Label eyeIcon, stayLoggedLabel, forgotPassLabel, loginLabel, registerLabel;
    @FXML
    private TextField usernameText, passwordText;
    @FXML
    private PasswordField passwordField;
    @FXML
    private Button loginButton = new Button();
    @FXML
    private CheckBox stayLogged;
    @FXML
    private MenuButton languageMenuButton;
    @FXML
    private ImageView logoImage;
    private boolean isGoodUsername;
    private boolean isGoodPassword;
    
    private final SqlService sqlService = SqlService.getInstance();
    private final SceneHandler sceneHandler = SceneHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final LoggedHandler loggedHandler = LoggedHandler.getInstance();
    private final String pathOfFont = PathHandler.getInstance().getPathOfFont();
    HashMap <String, String> languages = new HashMap<>() {{
        put("it", "Italiano");
        put("en", "English");
        put("fr", "Français");
        put("es", "Español");
    }};

    // Metodi FXML
    @FXML
    void onLoginButtonClick() {
        Command loginCommand = new LoginCommand(usernameText.getText(), passwordField.getText(), stayLogged.isSelected());
        loginCommand.execute();
    }

    @FXML
    void onForgotPasswordClick() {
        Command chageSceneCommand = new ChangeSceneCommand("send-email-view.fxml");
        chageSceneCommand.execute();
    }

    @FXML
    void onItalianClick(){
        languageMenuButton.setText("Italiano");
        Command changeSceneCommand = new ChangeSceneCommand("login-view.fxml", "it");
        changeSceneCommand.execute();
    }
    @FXML
    void onEnglishClick(){
        languageMenuButton.setText("English");
        Command changeSceneCommand = new ChangeSceneCommand("login-view.fxml", "en");
        changeSceneCommand.execute();
    }
    @FXML
    void onFrenchClick(){
        languageMenuButton.setText("Français");
        Command changeSceneCommand = new ChangeSceneCommand("login-view.fxml", "fr");
        changeSceneCommand.execute();
    }
    @FXML
    void onSpanishClick(){
        languageMenuButton.setText("Español");
        Command changeSceneCommand = new ChangeSceneCommand("login-view.fxml", "es");
        changeSceneCommand.execute();
    }

    @FXML
    void onRegisterButtonClick() {
        Command changeSceneCommand = new ChangeSceneCommand("register-view.fxml");
        changeSceneCommand.execute();
    }

    @FXML
    void showPassword() {
        eyeIcon.setText("\uF06E");
        passwordText.setText(passwordField.getText());
        passwordField.setVisible(false);
        passwordText.setVisible(true);
    }
    @FXML
    void hidePassword(){
        eyeIcon.setText("\uF070");
        passwordField.setText(passwordText.getText());
        passwordField.setVisible(true);
        passwordText.setVisible(false);
    }

    @FXML
    void initialize(){
        Font font = Font.loadFont(String.valueOf(getClass().getResource(pathOfFont+"fa-solid-900.ttf")), 16);
        eyeIcon.setText("\uF070");
        eyeIcon.setFont(font);
        loginButton.setDisable(true);
        loadText();
        languageMenuButton.setText(languages.get(settingsHandler.getLanguage()));
        checkLogged();
        listenerUsername();
        listenerPassword();
    }

    // Metodi
    private void checkLogged(){
        Platform.runLater(() -> {
            if (settingsHandler.isLogged()) {
                Settings settings = sqlService.getUserSettings(loggedHandler.getUsername());
                settingsHandler.updateSettings(settings);
                sceneHandler.loadScene(new View("menu-view.fxml"));
            }
        });
    }

    private void listenerUsername(){
        usernameText.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodUsername = newValue.length() >= 5;
            performBinding();
        });
    }

    private void listenerPassword(){
        passwordField.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodPassword = newValue.length() >= 8 || passwordText.getText().length() >= 8;
            performBinding();
        });

        passwordText.textProperty().addListener((observable, oldValue, newValue) -> {
            isGoodPassword = newValue.length() >= 8 || passwordField.getText().length() >= 8;
            performBinding();
        });
    }

    private void performBinding() {
        // Serve a disabilitare il button del login qualora non venissero introdotte credenziali valide
        // durante il login. Il runLater() serve ad assicuraci che questo codice venga eseguito
        // solamente dopo aver scritto nei vari textField.
        Platform.runLater(() -> {
            BooleanBinding bb = new BooleanBinding() {
                {
                    super.bind(
                            usernameText.textProperty(),
                            passwordText.textProperty(),
                            passwordField.textProperty()
                    );
                }

                @Override
                protected boolean computeValue() {
                    return !(isGoodUsername && isGoodPassword);
                }
            };

            loginButton.disableProperty().bind(bb);
        });
    }

    private void loadText(){
        ResourceBundle bundle = settingsHandler.getBundle();
        if(bundle!=null){
            stayLoggedLabel.setText(bundle.getString("staySignedLabel"));
            loginLabel.setText(bundle.getString("loginButton"));
            forgotPassLabel.setText(bundle.getString("forgotPassButton"));
            registerLabel.setText(bundle.getString("registerButton"));
        } else {
            System.out.println("Error in loading the language");
        }
    }
}
