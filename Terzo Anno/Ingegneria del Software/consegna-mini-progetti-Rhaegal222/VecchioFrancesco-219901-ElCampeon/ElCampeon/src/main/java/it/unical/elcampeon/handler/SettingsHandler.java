package it.unical.elcampeon.handler;

import it.unical.elcampeon.model.Settings;

import java.util.Locale;
import java.util.ResourceBundle;

// Classe che serve a gestire le impostazioni
public class SettingsHandler {
    public static Settings settings;
    private static final String [] themes = {"dark.css","light.css","blue.css", "elcampeon.css"};
    private String theme = "light.css";
    private String language = "en";
    private boolean logged = true;
    private ResourceBundle bundle;

    private static SettingsHandler instance;

    private SettingsHandler(){}
    public static SettingsHandler getInstance(){
        if(instance == null)
            instance = new SettingsHandler();
        return instance;
    }

    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private static final LoggedHandler loggedHandler = LoggedHandler.getInstance();

    // Setters
    public void setTheme(String theme) { this.theme = theme; }
    public void setLanguage(String language) { this.language = language; }
    public void setLogged(boolean logged) { this.logged = logged; }

    public boolean isLogged() {
        this.logged = !loggedHandler.stayLoggedReading().equals("null");
        return logged;
    }

    // Getters
    public String getTheme() { return theme; }
    public String [] getThemes() { return themes; }
    public String getLanguage() { return language; }

    public void updateSettings(Settings settings){
        this.theme = settings.getTheme();
        this.logged = settings.isLogged();
        this.language = settings.getLanguage();
    }

    public ResourceBundle getBundle() {
        if (bundle == null || !language.equals(bundle.getLocale().getLanguage())) {
            try {
                Locale locale = new Locale(language);
                String path = PathHandler.getInstance().getPathOfLanguage();
                bundle = ResourceBundle.getBundle(path + locale);
            } catch (Exception e) {
                alertHandler.createGenericErrorAlert();
            }
        }
        return bundle;
    }
}
