package it.unical.demacs.informatica.completejavafxinterface.view;

import it.unical.demacs.informatica.completejavafxinterface.Main;
import it.unical.demacs.informatica.completejavafxinterface.Settings;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

public class MainApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(MainApplication.class.getResource("main.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 1024, 800);
        stage.setTitle("JavaFX Email");
        stage.setMinWidth(600);
        stage.setMinHeight(600);
        stage.setScene(scene);
        for (String font : Settings.fonts)
            Font.loadFont(Objects.requireNonNull(Main.class.getResource(font)).toExternalForm(), 10);
        for (String style : Settings.styles)
            scene.getStylesheets().add(Objects.requireNonNull(Main.class.getResource(style)).toExternalForm());
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}