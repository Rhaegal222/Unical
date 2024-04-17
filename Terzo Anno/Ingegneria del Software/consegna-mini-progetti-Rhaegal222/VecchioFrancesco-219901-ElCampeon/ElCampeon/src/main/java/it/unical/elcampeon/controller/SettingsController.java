package it.unical.elcampeon.controller;

import it.unical.elcampeon.command.ChangeSceneCommand;
import it.unical.elcampeon.command.Command;
import it.unical.elcampeon.command.SaveSettingsCommand;
import it.unical.elcampeon.handler.*;
import it.unical.elcampeon.model.Settings;
import javafx.fxml.FXML;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.MenuButton;

import java.util.HashMap;
import java.util.ResourceBundle;

public class SettingsController {
    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final ResourceBundle bundle = settingsHandler.getBundle();

    HashMap<String, String> languages = new HashMap<>() {{
        put("it", "Italiano");
        put("en", "English");
        put("fr", "Français");
        put("es", "Español");
    }};

    HashMap<String, String> themes = new HashMap<>() {{
        put("elcampeon.css", "El Campeón");
        put("dark.css", "Dark");
        put("light.css", "Light");
        put("blue.css", "Blue");
    }};

    @FXML
    private CheckBox stayLogged;
    @FXML
    private Label languageLabel, themeLabel, signedLabel;
    @FXML
    private Label applyLabel, cancelLabel;

    @FXML private MenuButton languageMenuButton, themeMenuButton;

    /* Click per cambiare tema*/
    @FXML
    void onDarkClick() { themeMenuButton.setText("Dark"); }
    @FXML
    void onLightClick() { themeMenuButton.setText("Light"); }
    @FXML
    void onElCampeonClick() { themeMenuButton.setText("El Campeón"); }
    @FXML
    void onBlueClick() { themeMenuButton.setText("Blue"); }

    /* Click per cambiare lingua */
    @FXML
    void onItalianClick(){ languageMenuButton.setText("Italiano"); }
    @FXML
    void onEnglishClick(){ languageMenuButton.setText("English"); }
    @FXML
    void onFrenchClick() { languageMenuButton.setText("Français"); }
    @FXML
    void onSpanishClick() { languageMenuButton.setText("Español"); }
    @FXML
    void onSaveClick(){
        try{
            Command saveSettingsCommand = new SaveSettingsCommand(getSettings());
            saveSettingsCommand.execute();

            Command changeSceneCommand = new ChangeSceneCommand("menu-view.fxml");
            changeSceneCommand.execute();

        }catch (Exception e){
            alertHandler.createChangeSettingsErrorAlert();
        }
    }

    @FXML
    void onCancelClick(){
        Command changeSceneCommand = new ChangeSceneCommand("menu-view.fxml");
        changeSceneCommand.execute();
    }

    @FXML
    void initialize(){
        loadText();
        loadSettings();
    }

    private void loadSettings(){
        stayLogged.setSelected(settingsHandler.isLogged());
        themeMenuButton.setText(themes.get(settingsHandler.getTheme()));
        languageMenuButton.setText(languages.get(settingsHandler.getLanguage()));
    }

    private Settings getSettings(){
        Settings settings = new Settings();

        settings.setLogged(stayLogged.isSelected());

        switch (themeMenuButton.getText()){
            case "El Campeón" -> settings.setTheme("elcampeon.css");
            case "Dark" -> settings.setTheme("dark.css");
            case "Light" -> settings.setTheme("light.css");
            case "Blue" -> settings.setTheme("blue.css");
            default -> settings.setTheme(settingsHandler.getTheme());
        }

        switch (languageMenuButton.getText()){
            case "Italiano" -> settings.setLanguage("it");
            case "English" -> settings.setLanguage("en");
            case "Español" -> settings.setLanguage("es");
            case "Français" -> settings.setLanguage("fr");
            default -> settings.setLanguage(settingsHandler.getLanguage());
        }

        return settings;
    }

    private void loadText(){
        if(bundle!=null){
            languageLabel.setText(bundle.getString("languageLabel"));
            themeLabel.setText(bundle.getString("themeLabel"));
            signedLabel.setText(bundle.getString("staySignedLabel"));
            applyLabel.setText(bundle.getString("applyButton"));
            cancelLabel.setText(bundle.getString("backButton"));
        }
    }
}