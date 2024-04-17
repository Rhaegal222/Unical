package com.app.browser.controller;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class BrowserController{

    @FXML
    private Button backButton;

    @FXML
    private MenuItem fileClose;

    @FXML
    private MenuItem fileNewTab;

    @FXML
    private MenuItem fileNewWindow;

    @FXML
    private Button forwardButton;

    @FXML
    private Button homeButton;

    @FXML
    private Button refreshButton;

    @FXML
    private Button searchButton;

    @FXML
    private TabPane tabBar;

    @FXML
    private TextField textField;

    @FXML
    private WebView webView;

    private WebView currentWebView;

    /* Fundamentals */
    public void closeBrowser(){
        Platform.exit();
    }

    /*Page manager*/
    public void returnHome(){
        currentWebView.getEngine().load("http://www.google.it");
    }

    public void searchPage(){
        String search = textField.getText();
        if (search.contains("www.")){
            currentWebView.getEngine().load("http://"+search);
        }
        else {
            currentWebView.getEngine().load("http://www.google.it/search?q="+URLEncoder.encode(search, StandardCharsets.UTF_8));
        }
        textField.setText(currentWebView.getEngine().getLocation());
    }

    public void refreshPage(){
        currentWebView.getEngine().reload();
    }

    /*Tab Bar*/
    public void addTab(){
        WebView webView = new WebView();
        Tab tab = new Tab("Empty", webView);
        tab.setOnSelectionChanged(event -> {
            currentWebView = webView;
        });
        webView.getEngine().locationProperty().addListener(e -> textField.setText(webView.getEngine().getLocation()));
        webView.getEngine().titleProperty().addListener(e -> tab.setText(webView.getEngine().getTitle()));
        webView.getEngine().load("http://www.google.it/");
        tab.setOnCloseRequest(e ->{
            if (tabBar.getTabs().size() == 1){
                e.consume();
            }
        });
        currentWebView = webView;
        tabBar.getTabs().add(tab);
    }

    @FXML
    void initialize(){
        addTab();
    }
}
