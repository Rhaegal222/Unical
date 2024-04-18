package it.unical.elcampeon.handler;

import it.unical.elcampeon.model.View;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.input.KeyCode;
import javafx.stage.Stage;

import java.io.IOException;

// Classe per la gestione delle scene
public class SceneHandler {
    private Stage stage;
    private Scene scene;
    private static final String css = PathHandler.getInstance().getPathOfCSS();
    private static final AlertHandler alertHandler = AlertHandler.getInstance();
    private static final SettingsHandler settingsHandler = SettingsHandler.getInstance();

    private static SceneHandler instance;
    public static SceneHandler getInstance() {
        if(instance == null)
            instance = new SceneHandler();
        return instance;
    }

    private <T> T loadRootFromFXML(String resourceName) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource(resourceName));
        return fxmlLoader.load();
    }

    public void init(Stage stage){
        // Crea lo stage iniziale
        try {
            if (this.stage == null) {
                this.stage = stage;
                this.stage.setTitle("El Campeon");

                loadScene(new View("login-view.fxml"));

                stage.setResizable(true);
                stage.setScene(scene);

                stage.setMinWidth(800);
                stage.setMinHeight(650);
                stage.setWidth(1300);
                stage.setHeight(780);

                stage.show();
                scene.setOnKeyPressed(key -> {
                    if (key.getCode().equals(KeyCode.F11))
                        stage.setFullScreen(!stage.isFullScreen());
                });

                stage.setOnCloseRequest(event -> {
                    event.consume();
                    alertHandler.createExitAlert();
                });
            }
        } catch (Exception e){
            alertHandler.createGenericErrorAlert();
        }
    }

    public void loadTheme(){
        if(scene == null) return;

        scene.getStylesheets().clear();

        String theme = settingsHandler.getTheme();
        String [] themes = settingsHandler.getThemes();

        for(String i: themes)
            scene.getStylesheets().remove(String.valueOf(SceneHandler.class.getResource(css + i)));

        scene.getStylesheets().add(String.valueOf(SceneHandler.class.getResource(css + theme)));
    }

    public void loadScene(View view){
        try {
            Parent root = loadRootFromFXML(view.getPathOfView());
            if(scene == null) scene = new Scene(root);
            else scene.setRoot(root);
            loadTheme();
        } catch (Exception e) {
            alertHandler.createGenericErrorAlert();
        }
    }
}
