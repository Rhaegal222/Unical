package it.unical.elcampeon.handler;

import it.unical.elcampeon.command.ChangeSceneCommand;
import it.unical.elcampeon.command.Command;
import it.unical.elcampeon.model.View;
import javafx.application.Platform;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonBar;
import javafx.scene.control.ButtonType;
import javafx.scene.paint.Paint;
import org.kordamp.ikonli.javafx.FontIcon;

import java.util.Optional;
import java.util.ResourceBundle;

// Classe per la gestione degli alerts
public class AlertHandler {
    private static final LoggedHandler loggedHandler = LoggedHandler.getInstance();
    private static final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private static final SceneHandler sceneHandler = SceneHandler.getInstance();

    private AlertHandler(){}
    private static AlertHandler instance;
    public static AlertHandler getInstance(){
        if(instance == null)
            instance = new AlertHandler();
        return instance;
    }

    private Alert setupAlert(Alert.AlertType type, String title, String contentText, String iconName, String iconColor) {

        Alert alert = new Alert(type);

        if (type == Alert.AlertType.CONFIRMATION){
            ResourceBundle bundle = settingsHandler.getBundle();
            ButtonType okButton = new ButtonType(bundle.getString("yesButton"), ButtonBar.ButtonData.OK_DONE);
            ButtonType cancelButton = new ButtonType(bundle.getString("noButton"), ButtonBar.ButtonData.CANCEL_CLOSE);
            alert.getButtonTypes().setAll(okButton, cancelButton);
        }

        FontIcon icon = new FontIcon(iconName);
        icon.setIconColor(Paint.valueOf(iconColor));
        icon.getStyleClass().add("icons-color");
        icon.setIconSize(45);

        alert.setGraphic(icon);
        alert.setHeaderText("");
        alert.setTitle(title);
        alert.setContentText(contentText);

        return alert;
    }

    // Errore generico
    public void createGenericErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("genericError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Username o Email già in uso
    public void createAlreadyUsedAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("usernameOrEmailExistsError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Username o password errati
    public void createWrongCredentialsAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("incorrectUsernameOrPasswordError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Email non presente nel database
    public void createEmailNotExistsAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("emailNotFoundError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Errore nel cambio password
    public void createChangePassErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("passwordChangeError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Errore nel cambio delle impostazioni
    public void createChangeSettingsErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("settingsChangeError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Errore di connessione al server
    public void createDatabaseConnectionErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("serverConnectionError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Errore nel cambio del nome
    public void createChangeNameErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("nameChangeError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Errore nel cambio del cognome
    public void createChangeSurnameErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("surnameChangeError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Errore nel caricamento del menu
    public void createMenuLoadErrorAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.ERROR, bundle.getString("errorTitle"), bundle.getString("menuLoadError"), "mdi2a-alert", "#ff3333");
        alert.show();
    }

    // Conferma di logout
    public void createLogoutAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.CONFIRMATION, bundle.getString("logoutTitle"), bundle.getString("logoutConfirmation"), "mdi2p-progress-question", "#ff3333");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get().getButtonData() == ButtonBar.ButtonData.OK_DONE) {
            loggedHandler.stayLoggedWriting("null");
            Command changeSceneCommand = new ChangeSceneCommand("login-view.fxml");
            changeSceneCommand.execute();
        }
    }

    // Conferma di uscita dall'applicazione
    public void createExitAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.CONFIRMATION, bundle.getString("exitTitle"), bundle.getString("exitAppConfirmation"), "mdi2p-progress-question", "#ff3333");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get().getButtonData() == ButtonBar.ButtonData.OK_DONE) {
            Platform.exit();
            System.exit(0);
        }
    }

    // Password cambiata con successo
    public void createPasswordChangedAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.INFORMATION, bundle.getString("changePasswordTitle"), bundle.getString("passwordChangedSuccess"), "mdi2e-email-send", "#4d79ff");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get() == ButtonType.OK) {
            sceneHandler.loadScene(new View("login-view.fxml"));
        }
    }

    // Dati personali cambiati con successo
    public void createPersonalDataChangedAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.INFORMATION, bundle.getString("changeTitle"), bundle.getString("personalDataChangedSuccess"), "mdi2s-send-check", "#4d79ff");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get() == ButtonType.OK) {
            sceneHandler.loadScene(new View("settings-view.fxml"));
        }
    }

    // Registrazione avvenuta con successo
    public void createRegistrationSuccessAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.INFORMATION, bundle.getString("informationTitle"), bundle.getString("registrationSuccess"), "mdi2s-send-check", "#4d79ff");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get() == ButtonType.OK) {
            sceneHandler.loadScene(new View("login-view.fxml"));
        }
    }

    // Login avvenuto con successo
    public void createLoginSuccessAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.INFORMATION, bundle.getString("informationTitle"), bundle.getString("loginSuccess"), "mdi2c-check-circle-outline", "#4d79ff");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get() == ButtonType.OK) {
            try {
                sceneHandler.loadScene(new View("menu-view.fxml"));
            } catch (Exception e) {
                createMenuLoadErrorAlert();
            }
        }
    }

    // Token inviato con successo
    public void createTokenSentAlert() {
        ResourceBundle bundle = settingsHandler.getBundle();
        Alert alert = setupAlert(Alert.AlertType.INFORMATION, bundle.getString("changePasswordTitle"), bundle.getString("tokenSentSuccess"), "mdi2e-email-send", "#4d79ff");
        Optional<ButtonType> result = alert.showAndWait();
        if(result.isPresent() && result.get() == ButtonType.OK) {
            sceneHandler.loadScene(new View("token-view.fxml"));
        }
    }
}
