package it.unical.demacs.informatica.downloadimages.view;

import it.unical.demacs.informatica.downloadimages.MainApplication;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class SceneHandler {
    private static SceneHandler instance = null;
    private Stage stage;
    private Scene scene;

    public SceneHandler(){}
    public static SceneHandler getInstance(){
        if(instance == null)
            instance = new SceneHandler();
        return instance;
    }
    public void init(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(MainApplication.class.getResource("view/main-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        stage.setTitle("Scaricatore di immagini");
        stage.setScene(scene);
        stage.show();
    }

    public Stage getStage() {
        return stage;
    }
}
