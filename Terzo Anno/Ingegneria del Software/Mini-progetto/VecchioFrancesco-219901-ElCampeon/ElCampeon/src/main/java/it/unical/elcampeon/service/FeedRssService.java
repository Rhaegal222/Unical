package it.unical.elcampeon.service;

import com.rometools.rome.feed.synd.SyndFeed;
import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;
import it.unical.elcampeon.handler.AlertHandler;
import javafx.scene.layout.VBox;

import java.net.URL;

public class FeedRssService {

    private SyndFeed feed;
    private VBox mainVBox;
    private String status = "empty";
    private static FeedRssService instance;

    private static final AlertHandler alertHandler = AlertHandler.getInstance();

    private FeedRssService(){}

    public static FeedRssService getInstance(){
        if(instance==null)
            instance = new FeedRssService();
        return instance;
    }

    private void setFeed(){
        try {
            URL feedUrl = new URL("https://it.motorsport.com/rss/category/moto/news/");
            SyndFeedInput input = new SyndFeedInput();
            this.feed = input.build(new XmlReader(feedUrl));
        } catch (Exception e) {
            alertHandler.createGenericErrorAlert();
        }
    }

    public void setMainVBox(VBox mainVBox){
        this.mainVBox = mainVBox;
        setStatus("ok");
    }

    public SyndFeed getFeedRSS(){
        if (this.feed == null)
            setFeed();
        return this.feed;
    }

    public String getStatus(){
        return this.status;
    }

    public VBox getMainVBox(){
        return this.mainVBox;
    }

    public void setStatus(String status){
        this.status = status;
    }
}
