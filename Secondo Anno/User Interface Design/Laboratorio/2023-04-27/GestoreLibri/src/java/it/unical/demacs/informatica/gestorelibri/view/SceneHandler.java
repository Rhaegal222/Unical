package it.unical.demacs.informatica.gestorelibri.view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.text.Font;
import javafx.stage.Modality;
import javafx.stage.Stage;
import org.kordamp.ikonli.javafx.FontIcon;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class SceneHandler {
    private final static String RESOURCE_PATH = "/it/unical/demacs/informatica/gestorelibri/";
    private final static String CSS_PATH = RESOURCE_PATH + "css/";
    private final static String FONTS_PATH = RESOURCE_PATH + "fonts/";
    private Scene scene;
    private Stage stage;
    private String theme = "dark";
    private final Alert alert = new Alert(Alert.AlertType.INFORMATION);
    private static SceneHandler instance = null;
    private SceneHandler() {}
    public void init(Stage primaryStage) throws Exception {
        if(stage != null)
            return;
        stage = primaryStage;
        FXMLLoader loader = new FXMLLoader(getClass().getResource("Login.fxml"));
        scene = new Scene(loader.load(), 300, 200);
        loadFonts();
        changedTheme();
        stage.setScene(scene);
        stage.setTitle("Books");
        stage.setResizable(false);
        stage.show();
    }
    public static SceneHandler getInstance(){
        if(instance == null)
            instance = new SceneHandler();
        return instance;
    }
    public void setLoginScene() throws Exception {
        setCurrentRoot("Login.fxml");
        stage.hide();
        stage.setResizable(false);
        stage.setWidth(300);
        stage.setHeight(200);
        stage.show();
    }
    public void setBookScene() throws Exception {
        setCurrentRoot("Books.fxml");
        stage.hide();
        stage.setResizable(true);
        stage.setWidth(800);
        stage.setHeight(800);
        stage.show();
    }
    public void setAddBookScene() throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource(RESOURCE_PATH + "AddBook.fxml"));
        Stage stage = new Stage();
        stage.initModality(Modality.APPLICATION_MODAL);
        Scene scene = new Scene(loader.load(), 400, 400);
        setCSSForScene(scene);
        stage.setScene(scene);
        stage.showAndWait();
    }
    public void changeTheme() {
        if("dark".equals(theme))
            theme = "light";
        else
            theme = "dark";
        changedTheme();
    }
    private void loadFonts() {
        for (String font : List.of(FONTS_PATH + "Roboto/Roboto-Regular.ttf", FONTS_PATH + "Roboto/Roboto-Bold.ttf")) {
            Font.loadFont(Objects.requireNonNull(SceneHandler.class.getResource(font)).toExternalForm(), 10);
        }
    }
    private List<String> loadCSS() {
        List<String> resources = new ArrayList<>();
        for (String style : List.of(CSS_PATH + theme + ".css", CSS_PATH + "fonts.css", CSS_PATH + "style.css")) {
            String resource = Objects.requireNonNull(SceneHandler.class.getResource(style)).toExternalForm();
            resources.add(resource);
        }
        return resources;
    }
    private void setCSSForScene(Scene scene) {
        Objects.requireNonNull(scene, "Scene cannot be null");
        List<String> resources = loadCSS();
        scene.getStylesheets().clear();
        for(String resource : resources)
            scene.getStylesheets().add(resource);
    }
    private void setCSSForAlert(Alert alert) {
        Objects.requireNonNull(alert, "Alert cannot be null");
        List<String> resources = loadCSS();
        alert.getDialogPane().getStylesheets().clear();
        for(String resource : resources)
            alert.getDialogPane().getStylesheets().add(resource);
    }
    private void changedTheme() {
        setCSSForScene(scene);
        setCSSForAlert(alert);
    }
    public boolean isDarkTheme() {
        return "dark".equals(theme);
    }
    private void setCurrentRoot(String filename) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource(RESOURCE_PATH + filename));
        scene.setRoot(loader.load());
    }
    public void showError(String message) {
        FontIcon icon = new FontIcon("mdi2a-alert");
        icon.getStyleClass().add("icons-color");
        icon.setIconSize(40);
        alert.setGraphic(icon);
        alert.setTitle("Error");
        alert.setHeaderText("");
        alert.setContentText(message);
        alert.show();
    }
    public void showInfo(String message) {
        FontIcon icon = new FontIcon("mdi2i-information-outline");
        icon.getStyleClass().add("icons-color");
        icon.setIconSize(40);
        alert.setGraphic(icon);
        alert.setTitle("Info");
        alert.setHeaderText("");
        alert.setContentText(message);
        alert.show();
    }



}
