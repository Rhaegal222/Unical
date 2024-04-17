module it.unical.informatica.chatjavafx {
    requires javafx.controls;
    requires javafx.fxml;


    opens it.unical.informatica.chatjavafx to javafx.fxml;
    exports it.unical.informatica.chatjavafx;
}