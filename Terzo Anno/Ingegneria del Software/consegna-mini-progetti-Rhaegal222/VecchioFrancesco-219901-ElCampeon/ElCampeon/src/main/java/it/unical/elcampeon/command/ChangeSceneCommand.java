package it.unical.elcampeon.command;

import it.unical.elcampeon.handler.SettingsHandler;
import it.unical.elcampeon.model.View;

public class ChangeSceneCommand implements Command {
    View view;

    SettingsHandler settingsHandler = SettingsHandler.getInstance();

    public ChangeSceneCommand(String nameOfView) {
        this.view = new View(nameOfView);
        this.view.setLanguage(settingsHandler.getLanguage());
        this.view.setNameOfCSS(settingsHandler.getTheme());
    }

    public ChangeSceneCommand(String nameOfView, String language) {
        settingsHandler.setLanguage(language);
        this.view = new View(nameOfView);
        this.view.setLanguage(settingsHandler.getLanguage());
        this.view.setNameOfCSS(settingsHandler.getTheme());
    }

    @Override
    public void execute() {
        view.loadScene();
    }
}
