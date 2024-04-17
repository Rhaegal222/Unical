module it.unical.demacs.informatica.chatjavafx {
    requires javafx.controls;
    requires javafx.fxml;


    opens it.unical.demacs.informatica.chatjavafx to javafx.fxml;
    exports it.unical.demacs.informatica.chatjavafx;
}