package informatica.unical.reportdati.view;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class SceneHandler {
    private Scene scene;
    private Stage stage;
    private final String RESOURCE_PATH = "/informatica/unical/reportdati/";
    private static SceneHandler instance = new SceneHandler();
    private SceneHandler(){

    }
    public static SceneHandler getInstance(){
        if(instance == null) {
            instance = new SceneHandler();
        }
        return instance;
    }
    public void init(Stage primaryStage){
        if(stage != null){
            return;
        }
        stage = primaryStage;
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource(RESOURCE_PATH+"view/appView.fxml"));
            scene = new Scene(loader.load(),1100, 700);
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}
