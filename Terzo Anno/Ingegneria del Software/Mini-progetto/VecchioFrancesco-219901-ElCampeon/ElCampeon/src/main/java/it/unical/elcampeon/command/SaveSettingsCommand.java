package it.unical.elcampeon.command;

import it.unical.elcampeon.model.Settings;

public class SaveSettingsCommand implements Command{

    private final Settings settings;

    public SaveSettingsCommand(Settings settings) {
        this.settings = settings;
    }

    @Override
    public void execute() {
        settings.saveSettings();
    }
}
