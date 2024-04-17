package it.unical.demacs.informatica.chatjavafx;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.util.List;
import java.util.Objects;

public class ChatFrame extends Application {

	@Override
	public void start(Stage primaryStage) throws Exception {
		FXMLLoader loader = new FXMLLoader(ChatFrame.class.getResource("ChatFrame.fxml"));
		Scene scene = new Scene(loader.load(), 800, 800);
		primaryStage.setScene(scene);
		primaryStage.setTitle("ChatFrame");
		primaryStage.setMinHeight(400);
		primaryStage.setMinWidth(400);
		for (String font : List.of("fonts/Roboto/Roboto-Regular.ttf", "fonts/Roboto/Roboto-Bold.ttf"))
			Font.loadFont(Objects.requireNonNull(ChatFrame.class.getResource(font)).toExternalForm(), 10);
		String theme = "css/dark.css";
		//String theme = "css/light.css";
		for (String style : List.of(theme, "css/fonts.css", "css/style.css"))
			scene.getStylesheets().add(Objects.requireNonNull(ChatFrame.class.getResource(style)).toExternalForm());
		primaryStage.show();		
	}
	
	public static void main(String[] args) {
		launch(args);
	}

}
