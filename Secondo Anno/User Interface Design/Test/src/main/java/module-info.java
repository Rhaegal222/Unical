module com.app.test {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.app.test to javafx.fxml;
    exports com.app.test;
}