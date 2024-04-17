package it.unical.demacs.informatica.gestorelibri;

import it.unical.demacs.informatica.gestorelibri.view.SceneHandler;
import javafx.application.Application;
import javafx.stage.Stage;


public class MainApplication extends Application {

    @Override
    public void start(Stage primaryStage) {
        try {
            SceneHandler.getInstance().init(primaryStage);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}