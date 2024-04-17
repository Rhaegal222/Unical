package it.unical.demacs.informatica.chatjavafx;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.VBox;

public class ChatController {

    @FXML
    private TextArea messageArea;

    @FXML
    private TextArea allMessages;

    @FXML
    private Button sendButton;
    
    @FXML
    private VBox contacts;

    private void sendMessage(String message) {
    	allMessages.appendText(message);
    	messageArea.setText("");
    }
    
    @FXML
    void sendMessage(ActionEvent event) {
    	sendMessage(messageArea.getText() + System.lineSeparator());
    }
    
    @FXML
    void onKeyPressed(KeyEvent event) {
    	if(event.getCode() == KeyCode.ENTER) {    		
    		sendMessage(messageArea.getText());
    	}
    }
    
    @FXML
    void initialize() {
    	for(int i = 0; i < 20; i++) {
    		Image img = new Image(getClass().getResourceAsStream("images/img"+(i%4+1)+".png"),50,50,true, true);
    		Label l = new Label("Contact " + i, new ImageView(img));
    		l.setMinSize(200, 50);
    		contacts.getChildren().add(l);
    	}
    }

}
