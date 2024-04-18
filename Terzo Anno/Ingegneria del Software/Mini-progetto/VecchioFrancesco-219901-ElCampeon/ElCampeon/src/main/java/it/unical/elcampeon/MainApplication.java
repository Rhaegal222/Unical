package it.unical.elcampeon;

import it.unical.elcampeon.handler.PathHandler;
import it.unical.elcampeon.handler.SceneHandler;

import javafx.application.Application;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import java.io.IOException;
import java.util.Objects;

public class MainApplication extends Application {
    SceneHandler sceneHandler = SceneHandler.getInstance();

    @Override
    public void start(Stage stage) throws IOException {
        String PathOfLogo = PathHandler.getInstance().getPathOfLogo();
        Image icon = new Image(Objects.requireNonNull(getClass().getResource(PathOfLogo)).openStream());
        stage.getIcons().add(icon);
        sceneHandler.init(stage);
    }

    public static void main(String[] args) {
        launch();
    }
}
