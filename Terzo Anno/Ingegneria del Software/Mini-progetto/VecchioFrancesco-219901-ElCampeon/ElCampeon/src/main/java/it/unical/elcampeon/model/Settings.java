package it.unical.elcampeon.model;

import it.unical.elcampeon.handler.LoggedHandler;
import it.unical.elcampeon.handler.SettingsHandler;
import it.unical.elcampeon.service.FeedRssService;
import it.unical.elcampeon.service.SqlService;

public class Settings {
    private String theme;
    private String language;
    private boolean logged = false;

    FeedRssService feedRssService = FeedRssService.getInstance();
    private final LoggedHandler loggedHandler = LoggedHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final SqlService sqlService = SqlService.getInstance();

    public Settings(){}

    public Settings(String theme, String language) {
        this.theme = theme;
        this.language = language;
    }
    public Settings(String theme, String language, Boolean logged) {
        this.theme = theme;
        this.language = language;
        this.logged = logged;
    }

    // Getters
    public String getTheme() {
        return theme;
    }
    public String getLanguage() {
        return language;
    }
    public boolean isLogged() {
        return logged;
    }

    // Setters
    public void setTheme(String theme) {
        this.theme = theme;
    }
    public void setLanguage(String language) {
        this.language = language;
    }
    public void setLogged(boolean logged) { this.logged = logged; }

    public void saveSettings(){

        feedRssService.setStatus("empty");

        settingsHandler.setLanguage(this.language);
        settingsHandler.setTheme(this.theme);
        settingsHandler.setLogged(this.logged);

        if (this.logged) loggedHandler.stayLoggedWriting(loggedHandler.getUsername());
        else loggedHandler.stayLoggedWriting("null");

        sqlService.updateUserSettings(loggedHandler.getUsername(), language, theme);
    }
}
