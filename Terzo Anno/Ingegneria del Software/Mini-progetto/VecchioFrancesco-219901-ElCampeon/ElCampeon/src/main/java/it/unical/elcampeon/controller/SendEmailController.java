package it.unical.elcampeon.controller;

import it.unical.elcampeon.handler.AlertHandler;
import it.unical.elcampeon.handler.SceneHandler;
import it.unical.elcampeon.handler.SettingsHandler;
import it.unical.elcampeon.service.EmailService;
import it.unical.elcampeon.service.SqlService;
import it.unical.elcampeon.model.View;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

import java.util.ResourceBundle;
import java.util.Timer;
import java.util.TimerTask;
import java.util.UUID;

public class SendEmailController {
    public static String token;
    public static String email;
    private final SceneHandler sceneHandler = SceneHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private final SqlService sqlService = SqlService.getInstance();
    private final EmailService emailService = EmailService.getInstance();
    private final ResourceBundle bundle =settingsHandler.getBundle();

    @FXML
    private Label recoverPasswordLabel, submitLabel, cancelLabel;

    @FXML
    private TextField emailTextField;

    @FXML
    void onNewPasswordClick() {

        // Una volta premuto il button genera una nuova password, controlla se la mail esiste, manda la nuova password
        // via mail, esegue una query per cambiare password e infine esce un popup come avviso.

        if(sqlService.verifyEmailAvailability(emailTextField.getText())){
            email = emailTextField.getText();
            emailService.sendEmailPasswordRecover(emailTextField.getText(),
                    bundle.getString("forgotPassEmailTitle"),
                    bundle.getString("forgotPassEmailText1"), " " + token + " \n" +
                            bundle.getString("forgotPassEmailText2"));
            alertHandler.createTokenSentAlert();
        }
        else alertHandler.createEmailNotExistsAlert();
    }

    @FXML
    void onCancelButtonClick(){
        sceneHandler.loadScene(new View("login-view.fxml"));
    }


    @FXML
    void initialize(){
        updateLanguage();
        generateToken();
    }

    private void generateToken(){
        final long duration = 309000; // 5 minuti + 15 secondi
        Timer timer = new Timer();
        token = UUID.randomUUID().toString();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                token = UUID.randomUUID().toString();
            }
        },duration);
    }

    private void updateLanguage() {
        if (bundle != null) {
            submitLabel.setText(bundle.getString("submitButton"));
            cancelLabel.setText(bundle.getString("backButton"));
            recoverPasswordLabel.setText(bundle.getString("recoverPasswordLabel"));
        }
    }
}
