module com.app.browser {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;


    opens com.app.browser to javafx.fxml;
    exports com.app.browser;
    exports com.app.browser.controller;
    opens com.app.browser.controller to javafx.fxml;
}