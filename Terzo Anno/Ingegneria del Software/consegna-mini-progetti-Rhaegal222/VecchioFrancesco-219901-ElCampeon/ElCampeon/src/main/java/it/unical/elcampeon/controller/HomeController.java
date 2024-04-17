package it.unical.elcampeon.controller;

import com.rometools.rome.feed.synd.SyndCategory;
import com.rometools.rome.feed.synd.SyndEntry;
import com.rometools.rome.feed.synd.SyndFeed;
import it.unical.elcampeon.handler.*;
import it.unical.elcampeon.service.FeedRssService;
import javafx.application.Platform;
import javafx.concurrent.Task;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TitledPane;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.shape.Line;
import javafx.scene.shape.Rectangle;

import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;

public class HomeController {
    private final AlertHandler alertHandler = AlertHandler.getInstance();
    private final FeedRssService feedRssService = FeedRssService.getInstance();
    private final PathHandler pathHandler = PathHandler.getInstance();
    private final SettingsHandler settingsHandler = SettingsHandler.getInstance();
    private final ResourceBundle bundle = settingsHandler.getBundle();

    @FXML
    private TitledPane NewsPane, StandingPane;

    @FXML
    private ScrollPane NewsScrollPane, StandingScrollPane;

    @FXML
    void initialize() {
        updateLanguage();
        NewsScrollPane.setPrefHeight(600);
        NewsScrollPane.setPrefWidth(700);
        StandingPane.setVisible(false);

        Label loadingLabel = new Label("Loading");
        loadingLabel.getStyleClass().add("loading-label");
        loadingLabel.setPrefWidth(NewsScrollPane.getPrefWidth());
        loadingLabel.setPrefHeight(NewsScrollPane.getPrefHeight());
        loadingLabel.setAlignment(javafx.geometry.Pos.CENTER);
        NewsScrollPane.setContent(loadingLabel);

        // Crea un thread per animare il testo di caricamento
        new Thread(() -> {
            while (true) {
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    alertHandler.createGenericErrorAlert();
                }
                Platform.runLater(() -> {
                    if (loadingLabel.getText().endsWith("..."))
                        loadingLabel.setText("Loading");
                    else
                        loadingLabel.setText(loadingLabel.getText() + ".");
                });
            }
        }).start();


        if (feedRssService.getStatus().equals("empty"))
            manageFeedRSS(feedRssService.getFeedRSS());
        else {
            VBox mainVBox = feedRssService.getMainVBox();
            mainVBox.getStylesheets().clear();
            mainVBox.getStylesheets().add(String.valueOf(SceneHandler.class.getResource(pathHandler.getPathOfCSS() + settingsHandler.getTheme())));
            NewsScrollPane.setContent(mainVBox);
        }
    }

    private void updateLanguage(){
        if(bundle!=null) {
            NewsPane.setText(bundle.getString("news"));
            StandingPane.setText(bundle.getString("standing"));
        }
    }

    private String truncadeString(String string){
        if(string.length() > 300)
            return string.substring(0, 300)+"...";
        return string;
    }

    private String formatTitle(String title){
        if(title.startsWith("MotoGP | "))
            return title.substring(9);
        return title;
    }

    private String formatDate(String date){
        DateTimeFormatter originalFormatter = DateTimeFormatter.ofPattern("EEE MMM dd HH:mm:ss zzz yyyy", Locale.ENGLISH);
        DateTimeFormatter targetFormatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        ZonedDateTime zonedDateTime = ZonedDateTime.parse(date, originalFormatter);
        return targetFormatter.format(zonedDateTime);
    }

    private HBox createFooter(String date, String author , String link){
        HBox footer = new HBox(5);

        // Date
        Label dateLabel = new Label(formatDate(date));
        dateLabel.getStyleClass().add("label-class");

        // Author
        Label authorLabel = new Label(author);
        authorLabel.getStyleClass().add("label-class");

        // Button
        Button button = new Button();
        Label buttonLabel = new Label(bundle.getString("readMore"));
        buttonLabel.getStyleClass().add("label-class");
        button.setGraphic(buttonLabel);
        button.getStyleClass().add("news-button");
        button.setOnAction(e -> {
            try {
                java.awt.Desktop.getDesktop().browse(java.net.URI.create(link));
            } catch (java.io.IOException ioException) {
                alertHandler.createGenericErrorAlert();
            }
        });
        button.setOnMouseEntered(e -> button.setStyle("-fx-cursor: hand;"));
        button.setOnMouseExited(e -> button.setStyle("-fx-cursor: default;"));
        footer.setSpacing(35);
        footer.getChildren().addAll(dateLabel, authorLabel, button);
        // Aggiunge lo spazio tra il testo e il bottone
        footer.setMargin(button, new javafx.geometry.Insets(0, 0, 0, 50));
        // Allinea il bottone a destra
        footer.setAlignment(javafx.geometry.Pos.CENTER_RIGHT);
        return footer;
    }

    private HBox createNewsBody(String title, String description, Image image){
        HBox body = new HBox(5);

        // Aggiunge l'immagine
        ImageView photo = new ImageView(image);
        photo.setFitHeight(150);
        photo.setFitWidth(200);

        // Arrotonda i bordi dell'immagine
        Rectangle clip = new Rectangle(photo.getFitWidth(), photo.getFitHeight());
        clip.setArcWidth(20);
        clip.setArcHeight(20);
        photo.setClip(clip);

        VBox article = new VBox(5);

        // Title
        Label titleLabel = new Label(formatTitle(title));
        titleLabel.getStyleClass().add("news-title");
        titleLabel.setWrapText(true);

        // Description
        Label descriptionLabel = new Label(truncadeString(description));
        descriptionLabel.getStyleClass().add("label-class");
        descriptionLabel.setStyle("-fx-text-alignment: justify;");
        descriptionLabel.setWrapText(true);

        article.getChildren().addAll(titleLabel, descriptionLabel);

        body.setSpacing(30);
        body.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        body.getChildren().addAll(photo, article);

        return body;
    }

    private VBox createNews(String title, String description, String date, String author, String link, Image image){
        VBox newsVBox = new VBox(5);
        newsVBox.setPrefWidth(NewsScrollPane.getPrefWidth()-62);

        // Rimuove lo sfondo bianco
        newsVBox.setStyle("-fx-background-color: transparent; -fx-border-color: transparent;");

        newsVBox.setPadding(new javafx.geometry.Insets(0, 20, 0, 20)); //top, right, bottom, left

        HBox body = createNewsBody(title, description, image);
        HBox footer = createFooter(date, author, link);

        Line line = new Line(50, 50, NewsScrollPane.getPrefWidth()-62, 50); // x1, y1, x2, y2
        line.setStroke(javafx.scene.paint.Color.valueOf("#e0e0e0"));

        newsVBox.getChildren().addAll(body, footer, line);

        return newsVBox;
    }

    private void manageFeedRSS(SyndFeed feed) {
        if (feed == null) {
            //AlertHandler.createErrorAlert(bundle.getString("feedErrorAlert"));
            return;
        }

        VBox mainVBox = new VBox();
        mainVBox.setSpacing(20);
        mainVBox.setPadding(new javafx.geometry.Insets(20, 20, 20, 20)); //top, right, bottom, left

        Task<VBox> loadFeedTask = new Task<>() {
            @Override
            protected VBox call() {
                mainVBox.getStyleClass().add("news");
                // Assicurati di caricare il CSS nel thread dell'UI, non qui

                for (SyndEntry entry : feed.getEntries()) {
                    if (isCancelled()) {
                        break;
                    }
                    List<SyndCategory> categories = entry.getCategories();
                    for (SyndCategory category : categories) {
                        if (category.getName().equals("MotoGP")) {
                            String title = entry.getTitle();
                            String description = entry.getDescription().getValue();
                            String date = entry.getPublishedDate().toString();
                            String author = entry.getAuthor();
                            Image image = new Image(entry.getEnclosures().get(0).getUrl());
                            String link = entry.getLink();
                            VBox newsItemVBox = createNews(title, description, date, author, link, image);
                            Platform.runLater(() -> mainVBox.getChildren().add(newsItemVBox));
                        }
                    }
                }
                return mainVBox;
            }
        };

        loadFeedTask.setOnSucceeded(e -> {
            feedRssService.setMainVBox(mainVBox);
            NewsScrollPane.setContent(loadFeedTask.getValue());
            // Qui puoi anche applicare il CSS al VBox principale, poiché ora siamo nel thread dell'UI
            mainVBox.getStylesheets().add(String.valueOf(SceneHandler.class.getResource(pathHandler.getPathOfCSS() + settingsHandler.getTheme())));
        });

        loadFeedTask.setOnFailed(e -> NewsScrollPane.setContent(new Label(bundle.getString("feedError"))));

        // Avvia il Task in un nuovo Thread
        new Thread(loadFeedTask).start();
    }
}


