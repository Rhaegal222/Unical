package it.unical.elcampeon.handler;

// Classe per la gestione dei percorsi
public class PathHandler {

    private static  PathHandler instance;

    public static PathHandler getInstance() {
        if(instance == null)
            instance = new PathHandler();
        return instance;
    }
    String pathOfView = "/it/unical/elcampeon/view/";
    String pathOfCSS = "/it/unical/elcampeon/css/";
    String pathOfFont = "/it/unical/elcampeon/font/";
    String pathOfLanguage = "/it/unical/elcampeon/language/LAN_";
    String pathOfLogo = "/it/unical/elcampeon/Logo/Logo.png";

    public String getPathOfView() {
        return pathOfView;
    }
    public String getPathOfCSS() {
        return pathOfCSS;
    }
    public String getPathOfLanguage() {
        return pathOfLanguage;
    }
    public String getPathOfFont(){
        return pathOfFont;
    }
    public String getPathOfLogo() { return pathOfLogo; }
}
