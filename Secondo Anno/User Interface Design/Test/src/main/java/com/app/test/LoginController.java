package com.app.test;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

public class LoginController {

    @FXML
    private PasswordField pass_label;

    @FXML
    private TextField user_label;

    @FXML
    void do_login(ActionEvent event) {
        System.out.println("Godo come un riccio");
    }

}
