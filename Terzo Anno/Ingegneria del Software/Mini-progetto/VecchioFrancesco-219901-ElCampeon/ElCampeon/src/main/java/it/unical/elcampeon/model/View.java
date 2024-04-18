package it.unical.elcampeon.model;

import it.unical.elcampeon.handler.PathHandler;
import it.unical.elcampeon.handler.SceneHandler;

import java.util.ResourceBundle;

public class View {
    private ResourceBundle bundle;
    private String nameOfView;
    private String nameOfCSS = "dark.css";
    private String language = "en";
    private final String pathOfView = PathHandler.getInstance().getPathOfView();
    private final String pathOfCSS = PathHandler.getInstance().getPathOfCSS();
    private final String pathOfLanguage = PathHandler.getInstance().getPathOfLanguage();

    // Costruttore
    public View(String name) {
        this.nameOfView = name;
    }

    // Getters
    public ResourceBundle getBundle() { return bundle; }
    public String getNameOfView() { return nameOfView; }
    public String getNameOfCSS() { return nameOfCSS; }
    public String getLanguage() { return language; }
    public String getPathOfView() { return pathOfView+nameOfView; }
    public String getPathOfCSS() { return pathOfCSS; }
    public String getPathOfLanguage() { return pathOfLanguage; }

    // Setters
    public void setBundle(ResourceBundle bundle) { this.bundle = bundle; }
    public void setNameOfView(String nameOfView) { this.nameOfView = nameOfView; }
    public void setNameOfCSS(String nameOfCSS) { this.nameOfCSS = nameOfCSS; }
    public void setLanguage(String language) { this.language = language; }
    public void loadScene() {
        SceneHandler.getInstance().loadScene(this);
    }
}
